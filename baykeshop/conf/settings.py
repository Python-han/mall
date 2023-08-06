from django.conf import settings

INSTALLED_APPS = [
    'baykeshop.admin.apps.BaykeAdminConfig',
    'baykeshop.apps.shop',
    'baykeshop.apps.badmin',
    'rest_framework',
    'django_filters',
]


STATIC_ROOT = settings.BASE_DIR / "static"
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     "/var/www/static/",
# ]

MEDIA_URL = 'media/'
MEDIA_ROOT = settings.BASE_DIR / "media"

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

# 配置允许跨域访问的站点列表
CORS_ALLOWED_ORIGINS = [
    "http://localhost:2800",
    "http://127.0.0.1:2800",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:2800",
]

# 配置token的过期时间
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
