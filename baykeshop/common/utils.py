#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :utils.py
@说明    :小工具快捷方法
@时间    :2023/06/30 09:14:17
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

import random
import string

from django.urls import get_urlconf, get_resolver
from django.urls import URLPattern, URLResolver
from baykeshop.conf import bayke_settings


def code_random(code_length=bayke_settings.CODE_LENGTH):
    """ 生成指定位数随机字符串方法 """
    # chars = string.ascii_letters + string.digits   # 生成a-zA-Z0-9字符串
    chars = string.digits
    strcode = ''.join(random.sample(chars, code_length))  # 生成随机指定位数字符串
    return strcode


def generate_tree(source, parent):
    """ 树形结构迭代 """
    tree = []
    for item in source:
        if item["parent"] == parent:
            item["children"] = generate_tree(source, item["id"])
            tree.append(item)
    return tree


def get_all_url(resolver=None, pre='/'):
    """获取项目全部 url
    # 获取某个 app 下的全部 url
    # 假设有一个 app 叫 dashboard
    # 通过 pre 参数传入相应前缀
    >> for url, name in get_all_url(get_resolver('dashboard.urls')):
    >>      print("url='{}'  name='{}'".format(url, name))
    """
    if resolver is None:
        resolver = get_resolver()
    for r in resolver.url_patterns:
        if isinstance(r, URLPattern):
            if '<pk>' in str(r.pattern):
                continue
            yield pre + str(r.pattern).replace('^', '').replace('$', ''), r.name
        if isinstance(r, URLResolver):
            yield from get_all_url(r, pre + str(r.pattern))