from django.db.models import Sum, F
from django.db.utils import IntegrityError

from rest_framework import serializers
from baykeshop.common.serializers import ModelSerializer, Serializer
from baykeshop.apps.shop.models import (
    BaykeShopCategory, BaykeshopBrand, BaykeShopSPU, BaykeShopSKU,
    BaykeShopSpec, BaykeShopSpecValue, BaykeShopOrder, BaykeShopOrderSKU,
    BaykeShopCart, BaykeAddress, BaykeUserBalanceLog, BaykeShopBanner
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
    skuSpecs = serializers.SerializerMethodField()
    specs = serializers.SerializerMethodField()
    # detailurl = serializers.SerializerMethodField()
    
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
    
    def get_skuSpecs(self, obj):
        sku_specs = BaykeShopSKUSerializer(obj.baykeshopsku_set.all(), many=True).data
        for spec in sku_specs:
            # spec['img'] = f"{self.context['request'].scheme}://{self.context['request'].get_host()}{spec['img']}"
            spec['specops'] = [BaykeShopSpecValueSerializer(BaykeShopSpecValue.objects.get(id=v), many=False).data for v in spec['spec_values']]
        return sku_specs

    def get_specs(self, obj):
        specs = []
        ids = obj.baykeshopsku_set.values_list('spec_values__spec__id', flat=True)
        specs_queryset = BaykeShopSpec.objects.filter(id__in=set(ids))
        for spec in specs_queryset:
            spec_dict = {
                "id": spec.id,
                "name": spec.name,
                "baykeshopspecvalue_set": BaykeShopSpecValueSerializer(spec.baykeshopspecvalue_set.all(), many=True).data
            }
            specs.append(spec_dict)
        return specs


class BaykeShopSpecValueSerializerCRUD(ModelSerializer):
    """ 商品规格增删改查 """
    class Meta:
        model = BaykeShopSpecValue
        fields = "__all__"

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


class BaykeShopOrderSKUSerializer(ModelSerializer):
    """ 订单商品 """
    class Meta:
        model = BaykeShopOrderSKU
        fields = "__all__"


class BaykeShopOrderSerializer(ModelSerializer):
    """ 订单 """
    owner_data = serializers.SerializerMethodField()
    baykeshopordersku_set = BaykeShopOrderSKUSerializer(many=True, read_only=True)
    pay_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = BaykeShopOrder
        fields = "__all__"
        read_only_fields = ('status', 'order_sn')
        
    def get_owner_data(self, obj):
        return f"{obj.owner.username}|{obj.owner.id}|(uid:{obj.owner.baykeuser.id})"
        


class BaykeShopCartSerializer(ModelSerializer):
    """ 购物车 """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = BaykeShopCart
        fields = "__all__"
        
    def create(self, validated_data):
        try:
            instance = super().create(validated_data)
        except IntegrityError:
            carts = BaykeShopCart.objects.filter(owner=self.context['request'].user, sku=validated_data.get('sku'))
            if carts.exists():
                carts.update(num=F("num")+validated_data["num"])
                instance = carts.first()
        return instance
    

class BaykeAddressSerializer(ModelSerializer):
    """ 地址序列化 """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = BaykeAddress
        fields = "__all__"


class BaykeShopBannerSerializer(ModelSerializer):
    """ 轮播图序列 """
    class Meta:
        model = BaykeShopBanner
        fields = "__all__"
        
        
class BalanceRechargeSerializer(Serializer):
    """ 给自己充值余额 """
    
    total = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=True, min_value=1)
    
