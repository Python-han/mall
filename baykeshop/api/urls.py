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
from . import cart, product, public, user, order, pay, generics, token


router = DefaultRouter()

# public
router.register('banners', public.BaykeBannerViewset, basename='banners')

# address 地址
router.register('address', user.BaykeAddressViewSet, basename='address')

# 购物车【增删改查】
router.register('cart', cart.BaykeCartViewSet, basename='cart')

# 商品
router.register('product', product.BaykeProductSPUViewSet, basename='product')

# order 订单
router.register('order', order.BaykeOrderGeneratedViewset, basename='order')

urlpatterns = [
    # 支付宝支付回调
    path('alipay/api/', pay.AliPayNotifyAPIView.as_view(), name='alipay-api'),
    # 订单确认接口
    path('order/confirm/', order.BaykeOrderConfirmAPIView.as_view(), name='order-confirm'),
    # 当前登录用户详情
    path('user/<int:pk>/', generics.BaykeUserRetrieveAPIView.as_view(), name='user-detail'),
    # 获取邮箱验证码 post
    path('obtain/code/', generics.BaykeVerifyCodeObtainAPIView.as_view(), name='obtain-code'),
    # 效验邮箱验证码 post
    path('check/code/', generics.BaykeVerifyCodeCheckAPIView.as_view(), name='check-code'),
    # 获取token post
    path("token/", token.TokenObtainPairView.as_view(), name="token"),
    # 刷新token post
    path("refresh/", token.TokenRefreshView.as_view(), name="refresh"),
    # 验证token post 
    path("verify/", token.TokenVerifyView.as_view(), name="verify"),
    # 注册接口 post
    path("register/", generics.BaykeUserRegisterAPIView.as_view(), name="register-api"),
        
] + router.urls
