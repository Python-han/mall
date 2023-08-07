from django.db.models import Sum
from rest_framework import serializers
from baykeshop.common.serializers import ModelSerializer
from baykeshop.apps.shop.models import (
    BaykeShopCategory, BaykeshopBrand, BaykeShopSPU, BaykeShopSKU,
    BaykeShopSpec, BaykeShopSpecValue, BaykeShopOrder, BaykeShopOrderSKU
)


class BaykeShopCategorySerializer(ModelSerializer):
    """ 商品分类 """
    class Meta:
        model = BaykeShopCategory
        fields = "__all__"


class BaykeshopBrandSerializer(ModelSerializer):
    """ 商品品牌 """
    class Meta:
        model = BaykeshopBrand
        fields = "__all__"


class BaykeShopSPUSerializer(ModelSerializer):
    """ 商品管理 """
    stock = serializers.SerializerMethodField()
    sales = serializers.SerializerMethodField()
    class Meta:
        model = BaykeShopSPU
        fields = "__all__"
    
    def get_stock(self, obj):
        _stock = self.get_skus(obj).aggregate(Sum('stock'))
        return _stock.get('stock__sum') if _stock.get('stock__sum') else 0
    
    def get_sales(self, obj):
        _sales = self.get_skus(obj).aggregate(Sum('sales'))
        return _sales.get('sales__sum') if _sales.get('sales__sum') else 0

    def get_skus(self, obj):
        return BaykeShopSKU.objects.filter(spu=obj)
    
class BaykeShopSKUSerializer(ModelSerializer):
    """ 商品SKU管理 """
    class Meta:
        model = BaykeShopSKU
        fields = "__all__"