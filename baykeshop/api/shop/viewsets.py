from rest_framework.views import APIView
from rest_framework.response import Response
from baykeshop.common import viewsets, pagination, utils, mixins
from baykeshop.apps.shop.models import (
    BaykeShopCategory, BaykeshopBrand, BaykeShopSPU, BaykeShopSKU,
    BaykeShopSpec, BaykeShopSpecValue
)
from baykeshop.api.shop.serializers import (
    BaykeShopCategorySerializer, BaykeshopBrandSerializer,
    BaykeShopSPUSerializer, BaykeShopSKUSerializer, BaykeShopSpecSerializer,
    BaykeShopSpecValueSerializer, BaykeShopSpecValueSerializerCRUD
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
    

class BaykeShopSPUViewSet(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.BatchDestroyModelMixin,
                          viewsets.GenericViewSet):
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
    

class BaykeShopSKUViewSet(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.BatchDestroyModelMixin,
                          viewsets.GenericViewSet):
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
    serializer_class = BaykeShopSpecValueSerializerCRUD
    # pagination_class = pagination.PageNumberPagination
    # search_fields = ("name", )
    
    
class BaykeShopSPUCreateAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        baykeshopsku_set = data.get('baykeshopsku_set', [])
        # 多规格编辑
        if data.get('skutype') and data.get('id'):
            spu_queryset = BaykeShopSPU.objects.filter(id=data['id'])
            spu = spu_queryset.first()
            # 修改spu信息
            spu_queryset.update(
                title=data.get('title', ''), subtitle=data.get('subtitle', ''), 
                keywords=data.get('keywords', ''), desc=data.get('desc', ''),
                content=data.get('content', ''), unit=data.get('unit', ''),
                images=data.get('images', ''), skutype=data.get('skutype'),
                freighttype=data.get('freighttype'), expresstype=data.get('expresstype'),
                freight=data.get('freight', 0), sort=data.get('sort', 1),
                status=data.get('status', True),
                brand=BaykeshopBrand.objects.get(id=int(data.get('brand'))) if data.get('brand') else None,
            )
            spu.category.set(data.get('category', []))
            for sku in baykeshopsku_set:
                # 编辑sku
                if (sku.get('id')):
                    sku_obj = BaykeShopSKU.objects.get(id=int(sku.get('id')))
                    sku_obj.price = sku.get('price', 0)
                    sku_obj.stock = sku.get('stock', 0)
                    sku_obj.sales = sku.get('sales', 0)
                    sku_obj.img = sku.get('img', '')
                    sku_obj.retail_price = sku.get('retail_price', 0)
                    sku_obj.cost_price = sku.get('cost_price', 0)
                    sku_obj.item = sku.get('item', '')
                    sku_obj.weight = sku.get('weight', 0)
                    sku_obj.vol = sku.get('vol', 0)
                    sku_obj.spec_values.set(sku.get('spec_values', []))
                    sku_obj.save()
                else:
                    # 多出来的添加
                    sku_obj = BaykeShopSKU.objects.create(
                        spu=spu, vol = sku.get('vol', 0),
                        price=sku.get('price', 0), stock = sku.get('stock', 0),
                        sales = sku.get('sales', 0), img = sku.get('img', ''),
                        retail_price = sku.get('retail_price', 0), cost_price = sku.get('cost_price', 0),
                        item = sku.get('item', ''), weight = sku.get('weight', 0)
                    )
                    sku_obj.spec_values.set(sku.get('spec_values', []))
        
        return Response({'code': 'ok'})