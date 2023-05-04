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

from django.views.generic import TemplateView


class BaykeOrderConfirmView(TemplateView):
    
    template_name = "baykeshop/pay.html"