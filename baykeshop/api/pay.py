#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :pay.py
@说明    :支付相关
@时间    :2023/04/25 11:11:49
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers
from rest_framework.response import Response


from baykeshop.permissions import IsOwnerAuthenticated
from baykeshop.models import BaykeOrder
from .order import BaykeOrderSerializer
from baykeshop.payment.pay import alipay


class NotifyMixin:
    """ 支付宝post回调 """
    def notify(self, request, *args, **kwargs):
        datas = request.data.dict()
        signature = datas.pop("sign")
        order_sn = datas.get('out_trade_no')
        trade_no = datas.get('trade_no')
        orders = self.get_queryset().filter(order_sn=order_sn)
        
        success = alipay.verify(datas, signature)
        from django.utils import timezone
        if success:
            orders.update(
                pay_status=2, 
                trade_sn=trade_no, 
                pay_time=timezone.now(),
                pay_method=2
            )
       
        return Response("success")
    

class ReturnMixin:
    """ get回调 """
    def returner(self, request, *args, **kwargs):
        datas = request.query_params.dict()
        signature = datas.pop("sign")
        order_sn = datas.get('out_trade_no')
        trade_no = datas.get('trade_no')
        orders = self.get_queryset().filter(order_sn=order_sn)
        success = alipay.verify(datas, signature)
        from django.utils import timezone
        if success:
            orders.update(
                pay_status=2, 
                trade_sn=trade_no, 
                pay_time=timezone.now(),
                pay_method=2
            )
        
        instance = orders.first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class AliPayNotifyAPIView(NotifyMixin, ReturnMixin, GenericAPIView):
    """ 支付宝支付回调 """
    serializer_class = BaykeOrderSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    # permission_classes = [IsOwnerAuthenticated]
    queryset = BaykeOrder.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.returner(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.notify(request, *args, **kwargs)