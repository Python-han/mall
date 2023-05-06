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

from decimal import Decimal

from django.conf import settings
from django.urls import reverse
from django.db.models import F

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from baykeshop.pagination import PageNumberPagination
from baykeshop.api.filters import BaykeOrderFilter
from baykeshop.permissions import IsOwnerAuthenticated
from baykeshop.api.cart import BaykeCartSKUSerializer
from baykeshop.models import (
    BaykeProductSKU, BaykeCart, BaykeOrder, BaykeOrderSKU, BaykeUser, BaykeUserBalanceLog
)
from baykeshop.conf import bayke_settings
from baykeshop.payment.payMony import OrderPayMony, computed


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
        datas = self.get_data(serializer)
        count = sum([sku['count'] for sku in datas])
        total = round(sum([sku['count'] * Decimal(sku['price']) for sku in datas]), 2)
        freight = sum([Decimal(sku['spu']['freight']) for sku in datas])
        total_amount = total + freight
        return Response({'skus': datas, 'count': count, 'total': total, 'freight': freight, 'total_amount': total_amount})
    
    def get_data(self, serializer):
        skuids = []
        if serializer.data['skuid']:
            skuids.append(serializer.data['skuid'])
            skus = BaykeCartSKUSerializer(BaykeProductSKU.objects.filter(id__in=skuids), many=True)
            for sku in skus.data:
                sku['count'] = serializer.data['count']
                sku['totalPrice'] = serializer.data['count'] * Decimal(sku['price'])
        elif serializer.data['cartids']:
            cart_ids = serializer.data['cartids'].split(',')
            carts = BaykeCart.objects.filter(id__in=cart_ids)
            skuids = list(carts.values_list('sku__id', flat=True))
            skus = BaykeCartSKUSerializer(BaykeProductSKU.objects.filter(id__in=skuids), many=True)
            for sku in skus.data:
                sku['count'] = carts.filter(sku__id=sku['id']).first().count
                sku['totalPrice'] = sku['count'] * Decimal(sku['price'])
        return skus.data


class BaykeOrderSKUSerializer(serializers.ModelSerializer):
    
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    skus = serializers.SerializerMethodField()
    
    class Meta:
        model = BaykeOrderSKU
        fields = "__all__"

    def get_skus(self, obj):
        return BaykeCartSKUSerializer(obj.sku, many=False).data
    

class BaykeOrderSerializer(serializers.ModelSerializer):
    
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    baykeordersku_set = BaykeOrderSKUSerializer(many=True)
    
    class Meta:
        model = BaykeOrder
        fields = "__all__"
        
    def create(self, validated_data):
        baykeordersku_set = validated_data.pop('baykeordersku_set')
        validated_data['total_amount'] = sum([osku['count'] * osku['sku'].price for osku in baykeordersku_set])
        order = super().create(validated_data)
        for osku in baykeordersku_set:
            ordersku = BaykeOrderSKU(
                order=order,
                title=osku['sku'].spu.title,
                options=list(osku['sku'].options.values('spec__name', 'name')),
                price=osku['sku'].price,
                content=osku['sku'].spu.content,
                count=osku['count'],
                sku=osku['sku']
            )
            ordersku.save()
            BaykeCart.objects.filter(owner=self.context['request'].user, sku=osku['sku']).delete()
            
        return order
   
    
class BaykeOrderGeneratedViewset(mixins.ListModelMixin, 
                                 mixins.RetrieveModelMixin, 
                                 mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    """ 生成订单信息 """
    
    serializer_class = BaykeOrderSerializer
    permission_classes = [IsOwnerAuthenticated, ]
    authentication_classes = [SessionAuthentication, JWTAuthentication,]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BaykeOrderFilter
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return BaykeOrder.objects.filter(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['paymethod_url'] = reverse("baykeshop:checkpay", args=[response.data['id']])
        return response
    
    @action(detail=True, methods=['GET'])
    def checkpay(self, request, pk=None):
        """ 订单确认 """
        order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def pay(self, request, pk=None):
        """ 获取支付方式 """
        order = self.get_object()
        data = request.data
        if not data.get('method'):
            raise serializers.ValidationError("请选择支付方式！")
        
        if data.get('method') == 2:
            from baykeshop.payment.pay import alipay
            params = alipay.client_api(
                api_name="alipay.trade.page.pay",
                biz_content={
                    "out_trade_no": order.order_sn,
                    "total_amount": order.total_amount.to_eng_string(),
                    "subject": order.order_sn,
                    "product_code": "FAST_INSTANT_TRADE_PAY",
                },
                return_url=f"{request.scheme}://{request.get_host()}{reverse(bayke_settings.ALIPAY_RETURN_URL)}",
            )
            
            if settings.DEBUG:
                url = "https://openapi-sandbox.dl.alipaydev.com/gateway.do?{data}".format(data=params)
            else:
                url = "https://openapi.alipay.com/gateway.do?{data}".format(data=params)
            return Response({'alipayapi': url, 'method': 2})
             
        elif data.get('method') == 4:
            try:
                baykeuser = request.user.baykeuser
                if baykeuser.balance < order.total_amount:
                    raise serializers.ValidationError("当前用户余额不足，请充值！")
                baykeuser.balance = F("balance") - order.total_amount
                baykeuser.owner = request.user
                baykeuser.save()
                # 修改订单状态
                order.pay_status = 2
                order.save()
                # 记录余额变动日志
                BaykeUserBalanceLog.objects.create(
                    owner=request.user, 
                    amount=order.total_amount, 
                    change_status=2,
                    change_way=3
                )
                return Response({'code':'ok', 'message':'支付成功', 'method': 4})
            except BaykeUser.DoesNotExist:
                raise serializers.ValidationError("当前用户余额不足，请充值！")
            
        else:
            raise serializers.ValidationError("暂不支持该支付方式！")
        
    @action(detail=True, methods=['POST'])
    def confirmproduct(self, request, pk=None):
        """ 确认收货接口 """
        order = self.get_object()
        if order.pay_status != 3:
            raise serializers.ValidationError("该订单状态下不支持确认收货！")
        order.pay_status = 4
        order.save()
        return Response({'code': 'ok', 'message': '确认收货成功！'})

