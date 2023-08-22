#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :settings.py
@说明    :在默认配置文件上扩展的配置
@时间    :2023/08/22 14:41:50
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.conf import settings
from datetime import timedelta

INSTALLED_APPS =[
    # 导入第一项必选先注释掉默认配置的后台管理
    # 'baykeshop.admin.apps.BaykeAdminConfig',
    'baykeshop.apps.shop',
    'baykeshop.apps.badmin',
    'baykeshop.apps.comment',
    'rest_framework',
    'django_filters',
]

# 将该中间件插入到默认中间件列表的第三位
# 跨域问题处理相关配置
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
]

# 配置允许跨域访问的站点列表
CORS_ALLOWED_ORIGINS = [
    "http://localhost:2800",
    "http://127.0.0.1:2800",
]

# csrf可信来源
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:2800",
]

# 允许静态文件跨域
SECURE_CROSS_ORIGIN_OPENER_POLICY = None


# Mysql数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': settings.BASE_DIR / 'mysql.cnf',
            'charset': 'utf8mb4',
        },
    }
}

# 静态文件配置
# STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    settings.BASE_DIR / "static",
]

# 本地上传文件配置
MEDIA_URL = 'media/'
MEDIA_ROOT = settings.BASE_DIR / "media"


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


# redis缓存后端配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}


# 发送邮件后端
if settings.DEBUG:
    # 邮件本地测试后端，开发环境启用
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # 邮件控制台后端
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'