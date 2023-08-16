from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
from baykeshop.common.permission import BaykePermissionOrReadOnly
from baykeshop.api.shop.viewsets import BaykeShopCategoryViewSet, BaykeShopSPUViewSet
from baykeshop.apps.shop.models import BaykeShopSPU
from baykeshop.common import utils


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
    

class BaykeShopSPUView(BaykeShopSPUViewSet):
    """ 商品 """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [BaykePermissionOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/list.html"
        return response
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/detail.html"
        return response