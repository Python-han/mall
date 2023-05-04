#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :cart.py
@说明    :PC购物车视图
@时间    :2023/05/04 14:00:09
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.urls import reverse
from django.http.response import HttpResponseRedirect

from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from baykeshop.api.cart import BaykeCartViewSet
from baykeshop.pagination import PageNumberPagination


class BaykeCartPagination(PageNumberPagination):
    """ 购物车列表分页 """
    page_size = 50


class BaykeCartListView(BaykeCartViewSet):
    """ 购物车列表 """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    pagination_class = BaykeCartPagination
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to="/")
        return super().dispatch(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/cart.html"
        for res in response.data['results']:
            res['detailurl'] = reverse('baykeshop:cart-detail', args=[res['id']])
        return response
    
