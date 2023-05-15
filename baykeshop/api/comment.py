#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :comment.py
@说明    :评论相关接口
@时间    :2023/05/06 13:41:55
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''


from rest_framework import serializers


from baykeshop.models import BaykeOrderComments
from baykeshop.api.serializers import UserSerializer


class BaykeOrderCommentsSerializer(serializers.ModelSerializer):
    """ 详情页展示的商品评论 """
    owner = UserSerializer(many=False, read_only=True)
    
    class Meta:
        model = BaykeOrderComments
        fields = "__all__"
    
