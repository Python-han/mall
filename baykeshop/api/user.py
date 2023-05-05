#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :user.py
@说明    :与用户相关的视图及序列化
@时间    :2023/05/04 17:04:07
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''




from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


from baykeshop.permissions import IsOwnerAuthenticated
from baykeshop.models import BaykeAddress




class BaykeAddressSerializer(serializers.ModelSerializer):
    
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = BaykeAddress
        fields = "__all__"
        

class BaykeAddressViewSet(viewsets.ModelViewSet):
    """ 地址增删改查 """
    queryset = BaykeAddress.objects.all() 
    serializer_class = BaykeAddressSerializer
    permission_classes = [IsOwnerAuthenticated, ]
    authentication_classes = [SessionAuthentication, JWTAuthentication]

    def perform_create(self, serializer):
        self.save_only_default(serializer)
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        self.save_only_default(serializer)
        return super().perform_update(serializer)
    
    def save_only_default(self, serializer):
        # 处理默认收货地址只能有一个
        if serializer.validated_data['is_default']:
            self.get_queryset().filter(is_default=True).update(is_default=False)


