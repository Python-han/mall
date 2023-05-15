#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :article.py
@说明    :文章相关
@时间    :2023/05/15 18:50:40
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from rest_framework.renderers import TemplateHTMLRenderer

from baykeshop.api.article import (
    BaykeArticleViewset, BaykeArticleCategoryViewset, BaykeArticleTagViewset
)


class BaykeArticleView(BaykeArticleViewset):
    """ 文章相关 """
    
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/article/list.html"
        return response
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/article/detail.html"
        return response
    

class BaykeArticleCategoryView(BaykeArticleCategoryViewset):
    """ 文章分类详情 """
    
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/article/cate.html"
        return response
    

class BaykeArticleTagView(BaykeArticleTagViewset):
    """ 文章分类详情 """
    
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/article/tag.html"
        return response