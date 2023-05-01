#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :forms.py
@说明    :表单
@时间    :2023/05/01 21:20:28
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django import forms

from baykeshop.conf import bayke_settings


class SearchForm(forms.Form):
    
    template_name = "baykeshop/comp/search_form.html"
    
    search = forms.CharField(
        max_length=32, 
        label="搜索", 
        widget=forms.TextInput(
            {
                'type': 'search', 
                'class': 'input',
                'placeholder': f'{bayke_settings.SEARCH_VALUE}'
            }
        ))
    
    