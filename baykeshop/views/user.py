#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :user.py
@说明    :pc user相关视图
@时间    :2023/05/04 17:22:40
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.views.generic import FormView
from django.db.models import Sum
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from baykeshop.api.generics import BaykeUserRegisterAPIView

from baykeshop.forms import LoginForm


class LoginView(SuccessMessageMixin, BaseLoginView):
    """ 登录 """
    next_page = "/"
    form_class = LoginForm
    redirect_field_name = 'redirect_to'
    template_name = "baykeshop/user/login.html"
    success_message = "%(username)s 登录成功！"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=cleaned_data['username'],
        )
        

class LogoutView(BaseLogoutView):
    """ 登出 """
    template_name = 'baykeshop/user/logout.html'


class BaykeRegisterView(BaykeUserRegisterAPIView):
    """ 用户注册 """
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):

        return Response({}, template_name="baykeshop/user/register.html")