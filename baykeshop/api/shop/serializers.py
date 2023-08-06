from rest_framework import serializers
from baykeshop.common.serializers import ModelSerializer
from baykeshop.apps.shop.models import BaykeShopCategory, BaykeshopBrand


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