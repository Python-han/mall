#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :order.py
@说明    :
@时间    :2023/02/13 16:22:10
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

import json
from django.db.models import F
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.contrib.auth import get_user_model
from django.utils import timezone

from baykeCore.common.mixin import LoginRequiredMixin
from baykeShop.models import BaykeShopOrderInfo, BaykeUserInfo


User = get_user_model()


class BaykeShopOrderPayView(LoginRequiredMixin, View):
    
    template_name = None
    
    def get(self, request, *args, **kwargs):
          
        order_id = request.GET.get('orderID', 0)
        code = ""
        error = None
        extra_context = {}
        try:
            order = BaykeShopOrderInfo.objects.get(id=int(order_id))
            extra_context = {
                "order_sn": order.order_sn,
                "total_amount": order.total_amount,
                "address": order.address,
                "name": order.name,
                "phone": order.phone,
                "desc": order.baykeshopordersku_set.first().desc,
                "paymethod": order.pay_method,
                "pay_time": order.pay_time
            }
        except BaykeShopOrderInfo.DoesNotExist:
            error = "该订单不存在，请先去挑选商品！"
            
        if order.pay_status != 1:
            code = "ok"
            error = "支付成功！"

        context = {
            "code": code,
            "error": error,
            **extra_context,
            **kwargs
        }
        
        return TemplateResponse(
            request, 
            [ self.template_name or 'baykeShop/order_pay.html'],
            context
        )

    def post(self, request, *args, **kwargs):
        data = request.POST
        paymethod = json.loads(data.get('paymethod'))
        order_sn = data.get('order_sn')
        orders = BaykeShopOrderInfo.objects.filter(order_sn=order_sn)
        userinfo = BaykeUserInfo.objects.filter(owner=request.user)
        # 余额支付
        if orders.exists() and userinfo.exists() and paymethod.get('value') == 4:
            order = orders.first()
            user = userinfo.first()
            if user.balance < order.total_amount:
                return JsonResponse({'code':'error', 'message': '余额不足！'})
            
            userinfo.update(balance=F('balance')-order.total_amount-order.freight)
            orders.update(pay_status=2, trade_sn=f"YE{order_sn}", pay_method=4, pay_time=timezone.now())
            context = {"code": "ok", "message": "支付成功！"}
            return JsonResponse(context)
        else:
            return JsonResponse({'code':'error', 'message': '暂不支持该支付方式或支付信息有误！'})

