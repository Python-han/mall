from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include('baykeshop.apps.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('baykeshop.api.urls')),
    path('docs/', include_docs_urls(title='baykeShop API'))
]