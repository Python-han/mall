from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from baykeshop.common import viewsets, mixins, pagination, utils, permission
from baykeshop.apps.badmin.models import (
    BaykeDepartment, BaykeFrontedMenus, BaykeRoles, BaykeUser, 
    BaykePermissionAction, BaykeDictKey, BaykeDictValue, BaykeImage,
    BaykeSystem, BaykeEmailConf, BaykeSystemExtend
)
from .serializers import (
    BaykeDepartmentSerializer, BaykeFrontedMenusSerializer, BaykeUserSerializer,
    BaykePermissionActionSerializer, BaykeRolesSerializer, UserCreateSerializer,
    BaykeUserModelSerializer, PermissionSerializer, BaykeDictValueSerializer, 
    BaykeDictKeySerializer, BaykeImageSerializer, BaykeEmailConfSerializer,
    BaykeSystemSerializer, BaykeSystemExtendSerializer, ContentTypeSerializer
)
from .filters import (
    BaykeDepartmentFilterSet, BaykeUserFilterSet, BaykeDictValueFilterSet
)


class BaykeFrontedMenusViewSet(viewsets.ModelViewSet):
    """ 前端菜单增删改查
    """
    queryset = BaykeFrontedMenus.objects.all()
    serializer_class = BaykeFrontedMenusSerializer
    search_fields = ("name", )
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = utils.generate_tree(response.data, None)
        return response
    
    
class BaykeDepartmentViewSet(viewsets.ModelViewSet):
    """ 部门增删改查
    """
    queryset = BaykeDepartment.objects.all()
    serializer_class = BaykeDepartmentSerializer
    pagination_class = pagination.PageNumberPagination
    filterset_class = BaykeDepartmentFilterSet
    search_fields = ("name", "mark")
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = utils.generate_tree(response.data['results'], None)
        return response


class BaykeUserRetrieveAPIView(RetrieveAPIView):
    """ 获取当前登录用户信息 """
    serializer_class = BaykeUserSerializer
    permission_classes = [permission.IsOwnerAuthenticated]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    queryset = BaykeUser.objects.all()
    
    def get_object(self):
        return self.request.user.baykeuser
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        from baykeshop.common.utils import generate_tree
        response.data['menus'] = generate_tree(response.data['menus'], None)
        return response


class UserCreateViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ 创建用户 """
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]


class BaykeUserViewset(viewsets.ModelViewSet):
    """ 用户增删改查 """
    queryset = BaykeUser.objects.all()
    serializer_class = BaykeUserModelSerializer
    pagination_class = pagination.PageNumberPagination
    filterset_class = BaykeUserFilterSet
    search_fields = ('name', )
    

class BaykeRolesViewSet(viewsets.ModelViewSet):
    """ 角色增删改查 """
    queryset = BaykeRoles.objects.all()
    serializer_class = BaykeRolesSerializer
    pagination_class = pagination.PageNumberPagination
    search_fields = ("group__name", "codename")


class BaykePermissionActionViewSet(viewsets.ModelViewSet):
    """ 菜单权限关系分配 """
    queryset = BaykePermissionAction.objects.all()
    serializer_class = BaykePermissionActionSerializer
    pagination_class = pagination.PageNumberPagination
    
    def perform_destroy(self, instance):
        # 重写删除
        instance.permission.delete()
        
    def perform_batch_destroy(self, serializer):
        # 重写批量删除
        ids = serializer.data.get('ids', [])
        actions = self.get_queryset().filter(id__in=ids)
        for action in actions:
            action.permission.delete()

    
class PermissionListAPIView(ListAPIView):
    """ 权限列表 
    get:
        权限list
    """
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    permission_classes = [permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]


class BaykeDictKeyViewSet(viewsets.ModelViewSet):
    """ 字典键增删改查 
    list:
        字典列表
    create:
        添加字典
    retrieve:
        字典详情
    update:
        修改字典
    partial_update:
        局部修改
    destroy:
        删除单个数据
    batch_destroy:
        批量删除
    """
    queryset = BaykeDictKey.objects.all()
    serializer_class = BaykeDictKeySerializer
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = utils.generate_tree(response.data, None)
        return response
    

class BaykeDictValueViewSet(viewsets.ModelViewSet):
    """ 字典值增删改查 
    list:
        字典值列表
    create:
        添加字典
    retrieve:
        字典详情
    update:
        修改字典
    partial_update:
        局部修改
    destroy:
        删除单个数据
    batch_destroy:
        批量删除
    """
    queryset = BaykeDictValue.objects.all()
    serializer_class = BaykeDictValueSerializer
    filterset_class = BaykeDictValueFilterSet
    pagination_class = pagination.PageNumberPagination


class BaykeImageViewset(viewsets.ModelViewSet):
    """ 图片管理增删改查 
    list:
        字典值列表
    create:
        添加字典
    retrieve:
        字典详情
    update:
        修改字典
    partial_update:
        局部修改
    destroy:
        删除单个数据
    batch_destroy:
        批量删除
    """
    queryset = BaykeImage.objects.all()
    serializer_class = BaykeImageSerializer
    

class BaykeSystemViewset(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    """站点配置 """
    queryset = BaykeSystem.objects.all()
    serializer_class = BaykeSystemSerializer
    permission_classes = [permission.BaykePermissionAuthReadOnly]
    
    def get_object(self):
        cache.set('SYSTEM', self.get_queryset().first())
        if not self.get_queryset().exists():
            system = BaykeSystem.objects.create(
                site_title="baykeshop商城系统",
                logo_url="",
                copyright="baykeshop版权所有"
            )
            cache.set('SYSTEM', system)
        cache_system = cache.get('SYSTEM')
        return cache_system
    
    def readsystem(self, request, field_name=None):
        data = self.get_serializer(self.get_object()).data
        return Response({field_name: data.get(field_name, "")})
    
    
class BaykeEmailConfViewset(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    """ 邮箱配置 """
    queryset = BaykeEmailConf.objects.all()
    serializer_class = BaykeEmailConfSerializer
    
    def get_object(self):
        cache.set('EMAIL_CONF', self.get_queryset().first())
        if not self.get_queryset().exists():
            email_conf = BaykeEmailConf.objects.create(
                email_host = 'smtp.qq.com',
                email_host_user= 'baykeshop@qq.com',
                email_host_password = '123456',
                email_port = 465,
                email_use_ssl = True
            )
            cache.set('EMAIL_CONF', email_conf)
        cache_email_conf = cache.get('EMAIL_CONF')
        return cache_email_conf
    

class BaykeSystemExtendViewset(viewsets.ModelViewSet):
    """ 站点扩展配置 """
    queryset = BaykeSystemExtend.objects.all()
    serializer_class = BaykeSystemExtendSerializer
    permission_classes = [IsAdminUser]
        
    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            from .serializers import BaykeSystemExtendUpdateSerializer
            return BaykeSystemExtendUpdateSerializer
        return super().get_serializer_class()
    
class ContentTypeViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 应用接口视图 """
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return response