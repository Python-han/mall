#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :pay.py
@说明    :
@时间    :2023/05/04 16:53:15
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.urls import reverse
from rest_framework.renderers import TemplateHTMLRenderer

from baykeshop.api.order import BaykeOrderConfirmAPIView, BaykeOrderGeneratedViewset
from baykeshop.api.pay import AliPayNotifyAPIView
from baykeshop.models import BaykeOrder



class BaykeOrderConfirmView(BaykeOrderConfirmAPIView):
    """ 订单确认 """
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.template_name = "baykeshop/order/order_confirm.html"
        return response
    

class BaykeOrderPayMethodView(BaykeOrderGeneratedViewset):
    """ 订单支付，收银台 """
    
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def checkpay(self, request, pk=None):
        response = super().checkpay(request, pk)
        response.template_name = "baykeshop/order/order_paymethod.html"
        response.data['paymethods'] = self.get_paymethods()
        response.data['payapi'] = reverse("baykeshop:order-pay", args=[response.data['id']])
        return response
    
    def get_paymethods(self):
        pay_methods = BaykeOrder.get_pay_method()
        pay_list = [
            { 
                'value': 1,
                'name': pay_methods[1],
                'icon': "/static/baykeshop/img/hdpay.svg",
                'is_default': False
            },
            { 
                'value': 2,
                'name': pay_methods[2],
                'icon': "/static/baykeshop/img/alipay.svg",
                'is_default': True
            },
            { 
                'value': 3,
                'name': pay_methods[3],
                'icon': "/static/baykeshop/img/wxpay.svg",
                'is_default': False
            },
            { 
                'value': 4,
                'name': pay_methods[4],
                'icon': "/static/baykeshop/img/ye.svg",
                'is_default': False
            }
        ]
        return pay_list
    

class BaykeAlipayNotifyView(AliPayNotifyAPIView):
    
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def returner(self, request, *args, **kwargs):
        response = super().returner(request, *args, **kwargs)
        response.template_name = "baykeshop/payok.html"
        print(response.data)
        return response