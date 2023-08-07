from django.urls import path
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('category', viewsets.BaykeShopCategoryViewSet, basename='category')

router.register('brand', viewsets.BaykeshopBrandViewSet, basename='brand')

router.register('spu', viewsets.BaykeShopSPUViewSet, basename='spu')

urlpatterns = router.urls