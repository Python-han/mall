#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :order.py
@说明    :订单相关操作
@时间    :2023/05/04 21:49:00
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from baykeshop.api.cart import BaykeCartSKUSerializer
from baykeshop.models import BaykeProductSKU, BaykeCart


class BaykeOrderConfirmSerializer(serializers.Serializer):
    skuid = serializers.IntegerField(min_value=1, allow_null=True, required=False)
    count = serializers.IntegerField(min_value=1, allow_null=True, required=False)
    cartids = serializers.CharField(allow_null=True, required=False)
    
    def validate(self, attrs):
        if not attrs.get('skuid') and not attrs.get('cartids'):
            raise serializers.ValidationError("skuid与cartids参数必须存在其中一个")
        elif attrs.get('skuid') and not attrs.get('count'):
            raise serializers.ValidationError("skuid必须与count参数同时存在")
        elif attrs.get('cartids') and not isinstance(attrs.get('cartids').split(','), (list, tuple)):
            raise serializers.ValidationError("cartids必须为购物车id用英文,分割")
        elif attrs.get('skuid') and attrs.get('cartids'):
            raise serializers.ValidationError("skuid与cartids参数必须存在其中一个,不可同时存在")
        return attrs


class BaykeOrderConfirmAPIView(APIView):
    """ 订单确认接口 """
    permission_classes = [IsAuthenticated, ]
    serializer_class = BaykeOrderConfirmSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    
    def get(self, request, *args, **kwargs):
        serializer = BaykeOrderConfirmSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return Response({'skus': self.get_data(serializer)})
    
    def get_data(self, serializer):
        skuids = []
        if serializer.data['skuid']:
            skuids.append(serializer.data['skuid'])
            skus = BaykeCartSKUSerializer(BaykeProductSKU.objects.filter(id__in=skuids), many=True)
            for sku in skus.data:
                sku['count'] = serializer.data['count']
        elif serializer.data['cartids']:
            cart_ids = serializer.data['cartids'].split(',')
            carts = BaykeCart.objects.filter(id__in=cart_ids)
            skuids = list(carts.values_list('sku__id', flat=True))
            skus = BaykeCartSKUSerializer(BaykeProductSKU.objects.filter(id__in=skuids), many=True)
            for i, cart in enumerate(carts):
                skus.data[i]['count'] = cart.count
        return skus.data

        
    
