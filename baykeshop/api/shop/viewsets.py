from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.utils.serializer_helpers import ReturnDict
from baykeshop.common import viewsets, pagination, utils, mixins, permission
from baykeshop.apps.shop.models import (
    BaykeShopCategory, BaykeshopBrand, BaykeShopSPU, BaykeShopSKU,
    BaykeShopSpec, BaykeShopSpecValue, BaykeShopOrder, BaykeShopCart,
    BaykeAddress
)
from baykeshop.api.shop.serializers import (
    BaykeShopCategorySerializer, BaykeshopBrandSerializer,
    BaykeShopSPUSerializer, BaykeShopSKUSerializer, BaykeShopSpecSerializer,
    BaykeShopSpecValueSerializerCRUD, BaykeShopOrderSerializer, BaykeShopCartSerializer,
    BaykeAddressSerializer
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
        if isinstance(response.data, (OrderedDict, ReturnDict)):
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
                          mixins.UpdateModelMixin,
                          mixins.BatchDestroyModelMixin,
                          viewsets.GenericViewSet):
    """SKU规格商品增删改查
    list:
        列表
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
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)
    

class BaykeShopSKUViewSet(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.BatchDestroyModelMixin,
                          viewsets.GenericViewSet):
    """商品增删改查
    list:
        列表
    retrieve:
        详情
    destroy:
        删除单个数据
    batch_destroy:
        批量删除
    """
    queryset = BaykeShopSKU.objects.all()
    serializer_class = BaykeShopSKUSerializer
    permission_classes = [permission.BaykePermissionOrReadOnly]
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)
    

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
    
    def perform_destroy(self, instance):
        is_exists = BaykeShopSKU.objects.filter(spec_values=instance).exists()
        if is_exists:
            raise serializers.ValidationError("当前规格已关联商品，不允许删除")
        return super().perform_destroy(instance)
    
    
class BaykeShopSPUCreateOrUpdateAPIView(APIView):
    """ 商品的增加和修改 """
    permission_classes = [IsAdminUser, permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        baykeshopsku_set = data.get('baykeshopsku_set', [])
        # 编辑
        if data.get('id'):
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
        # 新增
        else:
            spu = BaykeShopSPU.objects.create(
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
                sku_obj = BaykeShopSKU.objects.create(
                    spu=spu, vol = sku.get('vol', 0),
                    price=sku.get('price', 0), stock = sku.get('stock', 0),
                    sales = sku.get('sales', 0), img = sku.get('img', ''),
                    retail_price = sku.get('retail_price', 0), cost_price = sku.get('cost_price', 0),
                    item = sku.get('item', ''), weight = sku.get('weight', 0)
                )
                sku_obj.spec_values.set(sku.get('spec_values', []))
        
        return Response({'code': 'ok'})
    

class BaykeShopOrderViewSet(mixins.ListModelMixin, 
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.BatchDestroyModelMixin,
                            viewsets.GenericViewSet
                        ):
    """ 订单管理 """
    queryset = BaykeShopOrder.objects.all()
    serializer_class = BaykeShopOrderSerializer
    pagination_class = pagination.PageNumberPagination
    filterset_class = filters.BaykeShopOrderFilterSet
    search_fields = ("order_sn", "name", "phone")
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)


class BaykeShopCartViewSet(mixins.ListModelMixin, 
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.BatchDestroyModelMixin, 
                           viewsets.GenericViewSet):
    """ 购物车 """
    permission_classes = [permission.IsOwnerAuthenticated]
    serializer_class = BaykeShopCartSerializer
    queryset = BaykeShopCart.objects.all()
    
    def get_queryset(self):
        # 仅允许查看自己的购物车信息
        return super().get_queryset().filter(owner=self.request.user)
    
    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)
    

class BaykeAddressViewSet(viewsets.ModelViewSet):
    """ 地址增删改查 """
    
    serializer_class = BaykeAddressSerializer
    permission_classes = [permission.IsOwnerAuthenticated]

    def get_queryset(self):
        return BaykeAddress.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        self.save_only_default(serializer)
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        self.save_only_default(serializer)
        return super().perform_update(serializer)
    
    def save_only_default(self, serializer):
        # 处理默认收货地址只能有一个
        if serializer.validated_data['is_default']:
            self.get_queryset().filter(is_default=True).update(is_default=False)