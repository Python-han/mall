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


from django.db.models import Sum
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from baykeshop.conf import bayke_settings
from baykeshop.permissions import IsOwnerAuthenticated
from baykeshop.models import BaykeAddress, BaykeUser, BaykeUserBalanceLog


class BaykeAddressSerializer(serializers.ModelSerializer):
    """ 地址序列化 """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = BaykeAddress
        fields = "__all__"
        

class BaykeAddressViewSet(viewsets.ModelViewSet):
    """ 地址增删改查 """
    
    serializer_class = BaykeAddressSerializer
    permission_classes = [IsOwnerAuthenticated, ]
    authentication_classes = [SessionAuthentication, JWTAuthentication]

    def get_queryset(self):
        return BaykeAddress.objects.filter(owner=self.request.user)
    
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



class BaykeUserBalanceLogSerializer(serializers.ModelSerializer):
    """ 余额记录序列化 """
    change_status = serializers.SerializerMethodField()
    change_way = serializers.SerializerMethodField()
    
    class Meta:
        model = BaykeUserBalanceLog
        fields = "__all__"
        
    def get_change_status(self, obj):
        return obj.get_change_status_display()
    
    def get_change_way(self, obj):
        return obj.get_change_way_display()


class BaykeUserSerializer(serializers.ModelSerializer):
    """ 扩展用户信息序列化 """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    balance = serializers.ReadOnlyField()
    
    class Meta:
        model = BaykeUser
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """ 用户序列化 """
    baykeuser = BaykeUserSerializer(many=False)
    username = serializers.ReadOnlyField()
    baykeuserbalancelog_set = BaykeUserBalanceLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'baykeuser', 'baykeuserbalancelog_set')
        
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        print(validated_data)
        try:
            BaykeUser.objects.filter(owner=instance).update(**validated_data['baykeuser'])
        except KeyError:
            pass
        instance.save()
        return instance
    
    def validate_baykeuser(self, data):
        try:
            import re
            phone = data['phone']
            reg = re.compile(bayke_settings.REGEX_PHONE)
            if not reg.search(phone):
                raise serializers.ValidationError("手机号格式有误！")
        except KeyError:
            pass
        return data
    

class BaykeUserMenmberViewset(mixins.RetrieveModelMixin, 
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    
    """ 用户中心 """
    
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return get_user_model().objects.filter(id=self.request.user.id)
    
    @action(detail=True, methods=['get'])
    def balance(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/user/balance.html"
        response.data['addplus'] = (
            self.get_object().baykeuserbalancelog_set.filter(change_status=1).aggregate(Sum('amount'))['amount__sum'] or 0
        )
        response.data['minusplus'] = (
            self.get_object().baykeuserbalancelog_set.filter(change_status=2).aggregate(Sum('amount'))['amount__sum'] or 0
        )
        return response