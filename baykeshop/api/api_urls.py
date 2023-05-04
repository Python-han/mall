#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :api_urls.py
@说明    :api url
@时间    :2023/05/04 13:18:53
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.urls import path

from rest_framework.routers import DefaultRouter
from . import cart, product, public, user, order


router = DefaultRouter()

# public
router.register('banners', public.BaykeBannerViewset, basename='banners')

# address
router.register('address', user.BaykeAddressViewSet, basename='address')

# 购物车【增删改查】
router.register('cart', cart.BaykeCartViewSet, basename='cart')

# 商品
router.register('product', product.BaykeProductSPUViewSet, basename='product')

urlpatterns = [
    path('order/confirm/', order.BaykeOrderConfirmAPIView.as_view(), name='order-confirm'),
        
] + router.urls
