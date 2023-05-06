#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :cart.py
@说明    :购物车相关
@时间    :2023/05/04 13:10:31
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.db.models import F
from django.db.utils import IntegrityError

from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from baykeshop.permissions import IsOwnerAuthenticated
from baykeshop.models import BaykeCart
from . import product


class BaykeCartSKUTSPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = product.BaykeProductSPU
        fields = ("id", "title", "pic", "freight")


class BaykeCartSKUSerializer(product.BaykeProductSKUSerializer):
    spu = BaykeCartSKUTSPUSerializer(many=False)


class BaykeCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaykeCart
        fields = "__all__"
        

class BaykeCartListSerializer(BaykeCartSerializer):
    sku = BaykeCartSKUSerializer(many=False)
    

class BaykeCartCreateSerializer(BaykeCartSerializer):
    """ 购物车序列化 """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            carts = BaykeCart.objects.filter(owner=self.context['request'].user, sku=validated_data.get('sku'))
            if carts.exists():
                carts.update(count=F("count")+validated_data["count"])
                return carts.first()
            
    def update(self, instance, validated_data):
        instance.count = validated_data['count']
        instance.save()
        return instance


class BaykeCartViewSet(viewsets.ModelViewSet):
    """ 购物车接口 
    list:
        购物车列表
    create:
        添加到购物车
    update:
        修改购物车数量
    retrieve:
        购物车详情
    destroy:
        删除购物车
    """
    serializer_class = BaykeCartSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsOwnerAuthenticated,]

    def get_queryset(self):
        return BaykeCart.objects.filter(sku__is_release=True, owner=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BaykeCartListSerializer
        elif self.action in ['create', 'update', 'partial']:
            return BaykeCartCreateSerializer
        return super().get_serializer_class()
