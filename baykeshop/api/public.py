#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :public.py
@说明    :公用视图
@时间    :2023/05/04 16:10:39
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework import serializers
from rest_framework import mixins
from rest_framework import viewsets


from baykeshop.models import BaykeBanner


class BaykeBannerSerializer(serializers.ModelSerializer):
    """ 轮播图序列化 """
    class Meta:
        model = BaykeBanner
        fields = "__all__"


class BaykeBannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 轮播图接口 """
    from baykeshop.models import BaykeBanner
    queryset = BaykeBanner.objects.all()
    serializer_class = BaykeBannerSerializer