#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :generics.py
@说明    :接口视图组合
@时间    :2023/04/22 17:00:42
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.generics import (
    RetrieveAPIView, CreateAPIView, GenericAPIView,
    ListAPIView, RetrieveUpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter

from baykeshop.permissions import IsOwnerAuthenticated


class BaykeUserRetrieveAPIView(RetrieveAPIView):
    """ 当前登录用户仅可查看自己的个人信息 """
    from .serializers import UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)
    

class BaykeVerifyCodeObtainAPIView(CreateAPIView):
    """ 获取验证码接口 """
    from .serializers import ObtainEmailCodeSerializer
    serializer_class = ObtainEmailCodeSerializer
    
    def get_queryset(self):
        from baykeshop.models import BaykeVerifyCode
        return BaykeVerifyCode.objects.all()
    

from .mixins import CheckVerifyCodeMixin  
class BaykeVerifyCodeCheckAPIView(CheckVerifyCodeMixin, GenericAPIView):
    """ 邮箱验证码验证是否过期或是否存在
    该接口存在的目的仅用作证明邮箱是一个可用的真实邮箱
    其他登录注册如需要邮箱验证功能仅需要在你的序列化期中
    继承CheckEmailCodeSerializer序列化器即可
    """
    from .serializers import CheckEmailCodeSerializer
    serializer_class = CheckEmailCodeSerializer
    
    def post(self, request, *args, **kwargs):
        return self.verify(request, *args, **kwargs)


class BaykeUserRegisterAPIView(mixins.CreateModelMixin, GenericAPIView):
    
    """ 用户注册接口 
    这个用到了邮箱验证码验证
    """
    from .serializers import RegisterSerializer
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
