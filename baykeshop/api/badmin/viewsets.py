from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

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
    BaykeSystemSerializer, BaykeSystemExtendSerializer
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
    permission_classes = [permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    queryset = BaykeUser.objects.all()
    
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
    """ 用户列表 """
    queryset = BaykeUser.objects.all()
    serializer_class = BaykeUserModelSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter) # DRF自带的过滤器
    search_fields = ('name', )
    ordering_fields = "__all__"
    filterset_class = BaykeUserFilterSet
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)
    

class BaykeRolesViewSet(viewsets.ModelViewSet):
    """ 角色增删改查 """
    queryset = BaykeRoles.objects.all()
    serializer_class = BaykeRolesSerializer
    pagination_class = pagination.PageNumberPagination
    search_fields = ("group__name", "codename")
    
    # def partial_update(self, request, *args, **kwargs):
    #     print('patch')
    #     return super().partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        menus = validated_data.get('menus', [])
        perm_ids = []
        for menu in menus:
            perm_ids.extend(list(menu.baykepermissionaction_set.values_list("permission__id", flat=True)))
        # 向权限组同步权限
        self.get_object().group.permissions.set(perm_ids)
        return super().perform_update(serializer)

class BaykePermissionActionViewSet(viewsets.ModelViewSet):
    """ 菜单权限关系分配 """
    queryset = BaykePermissionAction.objects.all()
    serializer_class = BaykePermissionActionSerializer
    
    
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
