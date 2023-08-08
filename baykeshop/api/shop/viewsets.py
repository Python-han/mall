from baykeshop.common import viewsets, pagination, utils
from baykeshop.apps.shop.models import (
    BaykeShopCategory, BaykeshopBrand, BaykeShopSPU, BaykeShopSKU,
    BaykeShopSpec, BaykeShopSpecValue
)
from baykeshop.api.shop.serializers import (
    BaykeShopCategorySerializer, BaykeshopBrandSerializer,
    BaykeShopSPUSerializer, BaykeShopSKUSerializer, BaykeShopSpecSerializer,
    BaykeShopSpecValueSerializer
)
from . import filters


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
    

class BaykeshopBrandViewSet(viewsets.ModelViewSet):
    """商品品牌增删改查
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
    queryset = BaykeshopBrand.objects.all()
    serializer_class = BaykeshopBrandSerializer
    pagination_class = pagination.PageNumberPagination
    search_fields = ("name", )
    

class BaykeShopSPUViewSet(viewsets.ModelViewSet):
    """SKU规格商品增删改查
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
    queryset = BaykeShopSPU.objects.all()
    serializer_class = BaykeShopSPUSerializer
    pagination_class = pagination.PageNumberPagination
    filterset_class = filters.BaykeShopSPUFilterSet
    search_fields = ("title", "subtitle")


class BaykeShopSKUViewSet(viewsets.ModelViewSet):
    """商品增删改查
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
    queryset = BaykeShopSKU.objects.all()
    serializer_class = BaykeShopSKUSerializer
    

class BaykeShopSpecViewSet(viewsets.ModelViewSet):
    """商品规格增删改查
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
    queryset = BaykeShopSpec.objects.all()
    serializer_class = BaykeShopSpecSerializer
    pagination_class = pagination.PageNumberPagination
    search_fields = ("name", )


class BaykeShopSpecValueViewSet(viewsets.ModelViewSet):
    """商品规格值增删改查
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
    queryset = BaykeShopSpecValue.objects.all()
    serializer_class = BaykeShopSpecValueSerializer
    # pagination_class = pagination.PageNumberPagination
    # search_fields = ("name", )