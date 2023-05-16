#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :pay.py
@说明    :
@时间    :2023/05/05 16:19:40
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.conf import settings
from baykeshop.conf import bayke_settings
from baykeshop.payment import AliPay


# 私钥
private_key_string = """
-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
"""
# 支付宝公钥
public_key_string = """
-----BEGIN RSA PUBLIC KEY-----
-----END RSA PUBLIC KEY-----
"""
    
try:
    with open(settings.BASE_DIR / bayke_settings.ALIPAY_PRIVATE_KEY, 'r') as f:
        private_key_string = f.read()
        
    with open(settings.BASE_DIR / bayke_settings.ALIPAY_PUBLIC_KEY, 'r') as f:
        public_key_string = f.read()
except FileNotFoundError:
    pass


alipay = AliPay(
    appid=bayke_settings.ALIPAY_APPID,
    app_private_key_string=private_key_string,
    alipay_public_key_string=public_key_string,
    sign_type=bayke_settings.ALIPAY_SIGN_TYPE,
    # app_notify_url=f"{bayke_settings.SITE_URL}{reverse(bayke_settings.ALIPAY_RETURN_URL)}",
    debug=settings.DEBUG,
    verbose=settings.DEBUG,
)