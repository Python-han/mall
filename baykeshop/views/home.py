#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :home.py
@说明    :首页
@时间    :2023/04/28 13:59:42
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''


from django.views.generic import TemplateView
# Create your views here.
from baykeshop.conf import bayke_settings
from baykeshop.models import BaykeProductCategory, BaykeProductSPU


class HomeTemplateView(TemplateView):
    """ 商城首页 """
    template_name = "baykeshop/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = self.get_queryset()
        return context
    
    def get_queryset(self):
        queryset = BaykeProductCategory.get_cates()
        for cate in queryset:
            cate.spus = BaykeProductSPU.objects.filter(
                cates__in=cate.sub_cates
            ).distinct()[:bayke_settings.HOME_NAV_COUNT]
        return queryset
