#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :article.py
@说明    :文章接口
@时间    :2023/05/15 18:30:44
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import serializers

from baykeshop.models import BaykeArticle, BaykeArticleCategory, BaykeArticleTag
from baykeshop.pagination import PageNumberPagination


class BaykeArticleTagSerializer(serializers.ModelSerializer):
    """ 文章标签 """
    
    class Meta:
        model = BaykeArticleTag
        fields = "__all__"


class BaykeArticleCategorySerializer(serializers.ModelSerializer):
    """ 文章分类序列化 """
    
    class Meta:
        model = BaykeArticleCategory
        fields = "__all__"


class BaykeArticleSerializer(serializers.ModelSerializer):
    """ 文章序列化 """
    
    tags = BaykeArticleTagSerializer(many=True)
    category = BaykeArticleCategorySerializer(many=False, read_only=True)
    
    class Meta:
        model = BaykeArticle
        fields = "__all__"


class BaykeArticleCategoryDetailSerializer(BaykeArticleCategorySerializer):
    """ 文章分类序列化 """
    baykearticle_set = BaykeArticleSerializer(many=True)
        

class BaykeArticleTagDetailSerializer(BaykeArticleTagSerializer):
    """ 标签详情序列化 """
    baykearticle_set = BaykeArticleSerializer(many=True)


class BaykeArticleViewset(mixins.ListModelMixin, 
                          mixins.RetrieveModelMixin, 
                          viewsets.GenericViewSet):
    
    """
    list:
        文章列表
    retrieve:
        文章详情 
    """
    serializer_class = BaykeArticleSerializer
    pagination_class = PageNumberPagination
    queryset = BaykeArticle.objects.all()


class BaykeArticleCategoryViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
        分类详情 
    """
    serializer_class = BaykeArticleCategoryDetailSerializer
    queryset = BaykeArticleCategory.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        page = PageNumberPagination()
        ret = page.paginate_queryset(response.data['baykearticle_set'], request, self)
        response.data['baykearticle_set'] = ret
        response.data['count'] = page.page.paginator.count
        response.data['next'] = page.get_next_link()
        response.data['previous'] = page.get_previous_link()
        response.data['current'] = int(request.query_params.get(page.page_query_param, 1))
        response.data['page_range'] = page.get_page_range()
        response.data['params'] = page.get_query_params()
        return response


class BaykeArticleTagViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
        标签详情 
    """
    serializer_class = BaykeArticleTagDetailSerializer
    pagination_class = PageNumberPagination
    queryset = BaykeArticleTag.objects.all()