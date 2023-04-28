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

from . import views

app_name = "baykeshop"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path('goods/', views.BaykeProductSPUListView.as_view(), name='goods'),
    path('cates/<int:pk>/', views.BaykeProductCategoryListView.as_view(), name='cate-detail'),
    
    path('api/', include('baykeshop.api.urls')),
]
