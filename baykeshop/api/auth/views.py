#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :token.py
@说明    :JWT登录token相关
@时间    :2023/04/23 11:35:06
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.contrib.auth import logout, get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView
)
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework.generics import CreateAPIView, GenericAPIView

from baykeshop.apps.badmin.models import BaykeVerifyCode
from baykeshop.common.mixins import CheckVerifyCodeMixin, CreateModelMixin


def get_tokens_for_user(user):
    """ 手动获取令牌 """
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'access_expire': refresh.access_token.payload['exp']   # token过期时间戳
    }


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):  
    """ 登录获取令牌 """
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['access_expire'] = refresh.access_token.payload['exp']   # token过期时间戳
        data['refresh_expire'] = self.get_refresh_expire()            # 刷新taoken的过期时间
        data['baykeuser_id'] = self.user.baykeuser.id
        return data
    
    def get_refresh_expire(self):
        import time
        from django.utils import timezone
        refresh_date = api_settings.REFRESH_TOKEN_LIFETIME + timezone.now()
        return int(time.mktime(time.localtime(refresh_date.timestamp())))  # 刷新taoken的过期时间戳
    
    
class TokenObtainPairView(BaseTokenObtainPairView):
    
    serializer_class = TokenObtainPairSerializer
    

class LogoutView(APIView):
    """ 退出登录接口 """
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'code': 'ok'})
    

class BaykeVerifyCodeObtainAPIView(CreateAPIView):
    """ 获取验证码接口 """
    from .serializers import ObtainEmailCodeSerializer
    serializer_class = ObtainEmailCodeSerializer
    
    def get_queryset(self):
        return BaykeVerifyCode.objects.all()
    

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
    

class BaykeUserRegisterAPIView(CreateModelMixin, GenericAPIView):
    """ 用户注册接口 
    这个用到了邮箱验证码验证
    """
    from .serializers import RegisterSerializer
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)