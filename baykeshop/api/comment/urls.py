from django.urls import path
from rest_framework.routers import DefaultRouter
from .import viewsets

router = DefaultRouter()

router.register('comment', viewsets.BaykeShopCommentViewSet, basename='comment')

urlpatterns = router.urls