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


def generate_order_sn(user):
    # 当前时间 + userid + 随机数
    from random import Random
    from django.utils import timezone
    random_ins = Random()
    order_sn = "{time_str}{user_id}{ranstr}".format(
        time_str=timezone.now().strftime("%Y%m%d%H%M%S"),
        user_id=user.id,
        ranstr=random_ins.randint(10, 99))
    return order_sn