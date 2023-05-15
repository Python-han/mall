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

from baykeshop.models import (
    BaykeProductSPU, BaykeProductSpec, 
    BaykeOrderComments, BaykeOrderSKU
)


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
    comments = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = BaykeProductSPU
        fields = "__all__"
    
    def get_specs(self, obj):
        spec_ids = obj.baykeproductsku_set.filter(is_release=True).values_list('options__spec__id', flat=True)
        specs = BaykeProductSpecSerializer(BaykeProductSpec.objects.filter(id__in=list(set(spec_ids))), many=True)
        return specs.data
    
    def get_comments_queryset(self, obj):
        """ 评论的queryset """
        from django.contrib.contenttypes.models import ContentType
        baykeordersku = ContentType.objects.get_for_model(BaykeOrderSKU)
        sku_ids = obj.baykeproductsku_set.values_list('id', flat=True)
        osku_ids = BaykeOrderSKU.objects.filter(sku__id__in=list(sku_ids)).values_list('id', flat=True)
        queryset = BaykeOrderComments.objects.filter(content_type=baykeordersku, object_id__in=list(osku_ids))
        return queryset
    
    def get_comments(self, obj):
        """ 当前商品的评论数据 """
        from baykeshop.api.comment import BaykeOrderCommentsSerializer
        queryset = self.get_comments_queryset(obj)
        return BaykeOrderCommentsSerializer(queryset, many=True).data
    
    def get_rate(self, obj):
        """ 好评率 """
        queryset = self.get_comments_queryset(obj)
        rate_gte_3 = queryset.filter(comment_choices__gte=3).count() if queryset.exists() else 0
        return (rate_gte_3 / queryset.count() if queryset.exists() else 0.98) * 100
    
    def get_score(self, obj):
        """ 平均分 """
        from django.db.models import Avg
        queryset = self.get_comments_queryset(obj)
        return queryset.aggregate(Avg("comment_choices"))['comment_choices__avg'] if queryset.exists() else 4.8


class BaykeProductSPUViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ 商品 SPU 
    retrieve:
        商品详情
    """
    queryset = BaykeProductSPU.objects.all()
    serializer_class = BaykeProductSPUSerializer
    
    
   


