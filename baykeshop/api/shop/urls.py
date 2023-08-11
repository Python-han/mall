from django.urls import path
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('category', viewsets.BaykeShopCategoryViewSet, basename='category')

router.register('brand', viewsets.BaykeshopBrandViewSet, basename='brand')

router.register('spu', viewsets.BaykeShopSPUViewSet, basename='spu')

router.register('sku', viewsets.BaykeShopSKUViewSet, basename='sku')

router.register('spec', viewsets.BaykeShopSpecViewSet, basename='spec')

router.register('specvalue', viewsets.BaykeShopSpecValueViewSet, basename='specvalue')

urlpatterns = [
    path('spu/create/', viewsets.BaykeShopSPUCreateAPIView.as_view(), name='spu_create'),
    
    *router.urls
]
