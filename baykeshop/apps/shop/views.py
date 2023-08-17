from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from baykeshop.common.permission import BaykePermissionOrReadOnly
from baykeshop.api.auth.views import BaykeUserRegisterAPIView
from baykeshop.api.shop.viewsets import BaykeShopCategoryViewSet, BaykeShopSPUViewSet
from baykeshop.apps.shop.models import BaykeShopSPU
from baykeshop.common import utils
from baykeshop.apps.shop.form import LoginForm


class BaykeShopCategoryView(BaykeShopCategoryViewSet):
    """ 实例化一个分类接口
    重写权限属性 取消分页
    permission_classes, get请求不受权限控制
    """
    permission_classes = [BaykePermissionOrReadOnly]
    pagination_class = None


class HomeTemplateView(TemplateView):
    """ 商城首页 """
    template_name = "baykeshop/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = self.get_spus(self.request)
        return context
    
    def get_spus(self, request):
        cates = utils.generate_tree(BaykeShopCategoryView.as_view({"get": "list"})(request).data, None) 
        for cate in cates:
            subcate_ids = [subcate['id'] for subcate in cate['children']]
            cate['spus'] = BaykeShopSPU.objects.filter(category__id__in=subcate_ids).distinct()
        return cates


class BaykeShopSPUOrderingFilter(OrderingFilter):
    """ 商品排序过滤器 """
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        if ordering:
            qs = []
            for q in queryset.order_by(*ordering):
                if q not in qs:
                    qs.append(q)
            return qs

        return queryset


class BaykeShopSPUView(BaykeShopSPUViewSet):
    """ 商品 """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [BaykePermissionOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter, BaykeShopSPUOrderingFilter) # DRF自带的过滤器
    ordering_fields = ("baykeshopsku__price", "baykeshopsku__sales", "add_date")
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/list.html"
        return response
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/detail.html"
        return response


class LoginView(SuccessMessageMixin, BaseLoginView):
    """ 登录 """
    next_page = "/"
    form_class = LoginForm
    redirect_field_name = 'redirect_to'
    template_name = "baykeshop/login.html"
    success_message = "%(username)s 登录成功！"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=cleaned_data['username'],
        )
        

class LogoutView(BaseLogoutView):
    """ 登出 """
    template_name = 'baykeshop/logout.html'
    

class BaykeRegisterView(BaykeUserRegisterAPIView):
    """ 用户注册 """
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response({}, template_name="baykeshop/register.html")