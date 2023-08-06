#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :default.py
@说明    :项目的默认配置
@时间    :2023/07/09 13:20:51
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''
import datetime


DEFAULTS_CONF = {
    # 站点title
    "SITE_TITLE": "baykeShop开源商城系统",
    # 站点头Logo
    "SITE_HEADER": "baykeShop Header",
    # 数据表前缀
    "DB_PREFIX": "bayke",
    # 默认管理后台开启自定义菜单
    "CUSTOM_MENU": False,
    # 手机号验证正则
    "REGEX_PHONE": "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$",
    # 邮箱验证正则
    "REGEX_EMAIL": "^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
    # 邮箱验证码过期时间
    "EMAIL_CODE_EXP": datetime.timedelta(seconds=300),
    # 验证码随机范围
    "CODE_CHAR": "1234567890",
    # 验证码长度
    "CODE_LENGTH": 4,
}