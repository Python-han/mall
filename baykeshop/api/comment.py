#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :comment.py
@说明    :评论相关接口
@时间    :2023/05/06 13:41:55
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from baykeshop.models import BaykeOrderComments



class BaykeOrderCommentsSerializer(serializers.ModelSerializer):
    
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = BaykeOrderComments
        fields = ("id", "content", "comment_choices", "object_id", "tag")
        
    def create(self, validated_data):
        return super().create(validated_data)


class BaykeOrderCommentsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BaykeOrderCommentsSerializer
    queryset = BaykeOrderComments.objects.all()
    
    
