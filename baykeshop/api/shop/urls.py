from django.urls import path
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('category', viewsets.BaykeShopCategoryViewSet, basename='category')

urlpatterns = router.urls