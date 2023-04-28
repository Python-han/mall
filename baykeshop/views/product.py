#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :product.py
@说明    :商品相关视图
@时间    :2023/04/28 14:00:05
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from typing import Any
from django.db import models
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from baykeshop.models import BaykeProductCategory, BaykeProductSPU


class BaykeProductSPUListView(ListView):
    """ 全部商品 """
    model = BaykeProductSPU
    template_name = "baykeshop/product/list.html"
    paginate_by = 15


class BaykeProductCategoryListView(SingleObjectMixin, BaykeProductSPUListView):
    """ 点击分类显示商品视图 """
    
    model = BaykeProductCategory
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=BaykeProductCategory.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cate"] = self.object
        return context

    def get_queryset(self):
        queryset = self.object.baykeproductspu_set.all()
        if self.object.parent is None:
            queryset = BaykeProductSPU.objects.filter(cates__in=self.object.baykeproductcategory_set.all()).distinct()
        return queryset
    
