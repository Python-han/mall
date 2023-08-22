#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :production.py
@说明    :生产环境配置
@时间    :2023/08/22 15:21:55
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.conf import settings
from datetime import timedelta


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x8wk&q%a26xd6jal@%**(mp-z@00zkldt!wn0_0akvxo573hj3'

ALLOWED_HOSTS = ['*']

# Mysql数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': f"{settings.BASE_DIR}/mysql.cnf",
            'charset': 'utf8mb4',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
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

# 邮件控制台后端
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 允许静态文件跨域
SECURE_CROSS_ORIGIN_OPENER_POLICY = None