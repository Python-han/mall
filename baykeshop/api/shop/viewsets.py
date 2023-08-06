from baykeshop.common import viewsets, pagination, utils
from baykeshop.apps.shop.models import BaykeShopCategory
from baykeshop.api.shop.serializers import BaykeShopCategorySerializer


class BaykeShopCategoryViewSet(viewsets.ModelViewSet):
    """商品分类增删改查
    list:
        列表
    create:
        添加
    retrieve:
        详情
    update:
        修改
    partial_update:
        局部修改
    destroy:
        删除单个数据
    batch_destroy:
        批量删除
    """
    queryset = BaykeShopCategory.objects.all()
    serializer_class = BaykeShopCategorySerializer
    pagination_class = pagination.PageNumberPagination
    search_fields = ("name", )
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = utils.generate_tree(response.data['results'], None)
        return response