from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/', include('baykeshop.api.urls')),
    path('apps/', include('baykeshop.apps.urls')),
    path('docs/', include_docs_urls(title='My API title'))
]