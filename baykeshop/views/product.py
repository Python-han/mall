#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :product.py
@说明    :商品相关视图
@时间    :2023/04/28 14:00:05
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''


from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages

from rest_framework import renderers

from baykeshop.forms import SearchForm
from baykeshop.models import BaykeProductCategory, BaykeProductSPU
from baykeshop.api.product import BaykeProductSPUViewSet


class BaykeProductSPUListView(ListView):
    """ 全部商品 """
    model = BaykeProductSPU
    template_name = "baykeshop/product/list.html"
    paginate_by = 15


class BaykeProductCategoryListView(SingleObjectMixin, BaykeProductSPUListView):
    """ 点击分类显示商品视图 """
    
    model = BaykeProductCategory
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=BaykeProductCategory.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cate"] = self.object
        return context

    def get_queryset(self):
        queryset = self.object.baykeproductspu_set.all()
        if self.object.parent is None:
            queryset = BaykeProductSPU.objects.filter(cates__in=self.object.baykeproductcategory_set.all()).distinct()
        return queryset
    

class BaykeSearchView(BaykeProductSPUListView):
    """ 搜索视图 """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word'] = self.request.GET.get('search')
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            word = form.cleaned_data['search']
            queryset = queryset.filter(
                Q(title__icontains=word)|Q(desc__icontains=word)|Q(keywords__icontains=word)
            )
            messages.add_message(self.request, messages.SUCCESS, f'共搜索到{queryset.count()}条数据')
        return queryset


class BaykeProductSPUDetailView(BaykeProductSPUViewSet):
    """ 商品详情页，继承api接口视图 """
    
    renderer_classes = (renderers.TemplateHTMLRenderer, )
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/product/detail.html"
        return response

    
    
