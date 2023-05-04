#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :product.py
@说明    :商品相关接口
@时间    :2023/05/04 13:38:23
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import serializers

from baykeshop.models import BaykeProductSPU, BaykeProductSpec


class BaykeProductBannerSerializer(serializers.ModelSerializer):
    """ 商品轮播图列化 """
    
    class Meta:
        from baykeshop.models import BaykeProductBanner
        model = BaykeProductBanner
        fields = ("id", "img")


class BaykeProductCategorySerializer(serializers.ModelSerializer):
    """ 商品分类序列化 """
    
    sub_cates = serializers.SerializerMethodField()
    
    class Meta:
        from baykeshop.models import BaykeProductCategory
        model = BaykeProductCategory
        exclude = ("site", "desc", "keywords", "is_del")
    
    def get_sub_cates(self, obj):
        if obj.parent is None:
            return BaykeProductCategorySerializer(obj.baykeproductcategory_set.all(), many=True).data


class BaykeProductSpecOptionSerializer(serializers.ModelSerializer):
    """ 商品spec option序列化 """
    
    spec = serializers.StringRelatedField()
    
    class Meta:
        from baykeshop.models import BaykeProductSpecOption
        model = BaykeProductSpecOption
        fields = ('id', 'name', 'spec')


class BaykeProductSpecSerializer(serializers.ModelSerializer):
    """ 商品spec序列化 """
    
    baykeproductspecoption_set = BaykeProductSpecOptionSerializer(many=True)
    
    class Meta:
        from baykeshop.models import BaykeProductSpec
        model = BaykeProductSpec
        fields = "__all__"


class BaykeProductSKUSerializer(serializers.ModelSerializer):
    """ 商品sku序列化 """
    
    options = BaykeProductSpecOptionSerializer(many=True)
    
    class Meta:
        from baykeshop.models import BaykeProductSKU
        model = BaykeProductSKU
        exclude = ("site", "add_date", "pub_date", "is_del")


class BaykeProductSPUSerializer(serializers.ModelSerializer):
    """ spu序列化 """
    
    cates = BaykeProductCategorySerializer(many=True, read_only=True)
    baykeproductbanner_set = BaykeProductBannerSerializer(many=True, read_only=True)
    baykeproductsku_set = BaykeProductSKUSerializer(many=True, read_only=True)
    specs = serializers.SerializerMethodField()

    class Meta:
        model = BaykeProductSPU
        fields = "__all__"
    
    def get_specs(self, obj):
        spec_ids = obj.baykeproductsku_set.filter(is_release=True).values_list('options__spec__id', flat=True)
        specs = BaykeProductSpecSerializer(BaykeProductSpec.objects.filter(id__in=list(set(spec_ids))), many=True)
        return specs.data


class BaykeProductSPUViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ 商品 SPU 
    retrieve:
        商品详情
    """
    queryset = BaykeProductSPU.objects.all()
    serializer_class = BaykeProductSPUSerializer
   


