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

class BaykeShopSKUSerializer(ModelSerializer):
    """ 商品SKU管理 """
    class Meta:
        model = BaykeShopSKU
        fields = "__all__"

class BaykeShopSPUSerializer(ModelSerializer):
    """ 商品管理 """
    stock = serializers.SerializerMethodField()
    sales = serializers.SerializerMethodField()
    baykeshopsku_set = BaykeShopSKUSerializer(many=True, read_only=True)
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


class BaykeShopSpecValueSerializer(ModelSerializer):
    """ 商品规格 """
    spec = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BaykeShopSpecValue
        fields = "__all__"

class BaykeShopSpecSerializer(ModelSerializer):
    """ 商品规格 """
    baykeshopspecvalue_set = BaykeShopSpecValueSerializer(many=True)
    class Meta:
        model = BaykeShopSpec
        fields = "__all__"
        
    def create(self, validated_data):
        baykeshopspecvalue_set = validated_data.pop('baykeshopspecvalue_set')
        instance = BaykeShopSpec.objects.create(**validated_data)
        # 批量存储
        BaykeShopSpecValue.objects.bulk_create(
            [BaykeShopSpecValue(spec=instance, value=v['value']) for v in baykeshopspecvalue_set]
        )
        return instance
    
    def update(self, instance, validated_data):
        baykeshopspecvalue_set = validated_data.pop('baykeshopspecvalue_set')
        BaykeShopSpec.objects.filter(id=instance.id).update(**validated_data)
        objs = instance.baykeshopspecvalue_set.all()
        # 先批量修改
        for index, obj in enumerate(objs):
            obj.value = baykeshopspecvalue_set[index].get('value')
        BaykeShopSpecValue.objects.bulk_update(objs, ["value"])
        
        # 比较是否存在，不存在新增
        for v in baykeshopspecvalue_set:
            objs.update_or_create(spec=instance, value=v['value'], defaults={'value': v['value']})    
        return instance