#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :urls.py
@说明    :接口url
@时间    :2023/04/22 20:32:35
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''


from django.urls import path, include
from baykeshop.conf import bayke_settings

from . import views

app_name = "baykeshop"

urlpatterns = [
    # 首页
    path("", views.HomeTemplateView.as_view(), name="home"),
    # 全部商品
    path('goods/', views.BaykeProductSPUListView.as_view(), name='goods'),
    # 分类页
    path('cates/<int:pk>/', views.BaykeProductCategoryListView.as_view(), name='cate-detail'),
    # 搜索页
    path('search/', views.BaykeSearchView.as_view(), name='search'),
    # 商品详情页
    path('product/<int:pk>/', views.BaykeProductSPUDetailView.as_view({'get': 'retrieve'}), name='product-retrieve'),
    # 购物车列表页
    path('carts/', views.BaykeCartListView.as_view({'get': 'list'}), name='carts'),
    # 订单确认页
    path('order/confirm/', views.BaykeOrderConfirmView.as_view(), name='confirm'),
    # 订单支付方式选择
    path('order/pay/<int:pk>/', views.BaykeOrderPayMethodView.as_view({'get': 'checkpay'}), name='checkpay'),
    # 支付宝支付后回调
    path('alipay/notify/', views.BaykeAlipayNotifyView.as_view(), name='alipaypc'),
    # 登录
    path('login/', views.LoginView.as_view(), name='login'),
    # 退出
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # 注册
    path('register/', views.BaykeRegisterView.as_view(), name='register'),
    # 用户中心
    path('menmber/<int:pk>/', views.BaykeUserMenmberView.as_view({'get':'retrieve'}), name='menmber'),
    # 余额
    path('menmber/<int:pk>/balance/', views.BaykeUserMenmberView.as_view({'get':'balance'}), name='balance'),
    # 地址管理
    path('menmber/address/', views.BaykeAddressView.as_view({'get':'list'}), name='menmber-address'),
    # 订单列表
    path('menmber/orders/', views.BaykeOrderView.as_view({'get':'list'}), name='menmber-orders'),
    # 订单详情
    path('menmber/orders/<int:pk>/', views.BaykeOrderView.as_view({'get':'retrieve'}), name='menmber-orders-retrieve'),
    # 订单评价
    path('menmber/orders/<int:pk>/comment/', views.BaykeOrderView.as_view({'get':'ordercomment'}), name='menmber-orders-comment'),
    # 文章列表
    path('article/', views.BaykeArticleView.as_view({'get': 'list'}), name='article-list-pc'),
    # 文章详情
    path('article/<int:pk>/', views.BaykeArticleView.as_view({'get': 'retrieve'}), name='article-detail-pc'),
    # 分类详情
    path('article/cate/<int:pk>/', views.BaykeArticleCategoryView.as_view({'get': 'retrieve'}), name='article-cate-pc'),
    # 标签详情
    path('article/tag/<int:pk>/', views.BaykeArticleTagView.as_view({'get': 'retrieve'}), name='article-tag-pc'),
    
    # 接口
    path('api/', include('baykeshop.api.urls')),
]
