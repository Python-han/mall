#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :development.py
@说明    :开发配置
@时间    :2023/08/22 15:21:25
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.conf import settings
from datetime import timedelta

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x8wk&q%a26xd6jal@%**(mp-z@00zkldt!wn0_0akvxo573hj3'

ALLOWED_HOSTS = ['*']

# sqlite3数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings.BASE_DIR / 'db.sqlite3',
    }
}

# 项目语言
LANGUAGE_CODE = 'zh-hans'
# 当前时区
TIME_ZONE = 'Asia/Shanghai'
# 多语言
USE_I18N = True
# 多时区
USE_TZ = True

# 静态文件配置
STATIC_URL = 'static/'
STATIC_ROOT = settings.BASE_DIR / "static"
# STATICFILES_DIRS = [
#     settings.BASE_DIR / "static",
# ]

# 本地上传文件配置
MEDIA_URL = 'media/'
MEDIA_ROOT = settings.BASE_DIR / "media"


# 配置允许跨域访问的站点列表
CORS_ALLOWED_ORIGINS = [
    'http://192.168.31.174',
    'http://127.0.0.1:2800'
]

# csrf可信来源
CSRF_TRUSTED_ORIGINS = [
    'http://192.168.31.174',
    'http://127.0.0.1:2800'
]

# drf默认全局配置
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

# 配置token的过期时间
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# 控制台邮件后端
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 允许静态文件跨域
SECURE_CROSS_ORIGIN_OPENER_POLICY = None