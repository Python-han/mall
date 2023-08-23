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

router.register('order', viewsets.BaykeShopOrderViewSet, basename='order')

router.register('cart', viewsets.BaykeShopCartViewSet, basename='cart')

router.register('address', viewsets.BaykeAddressViewSet, basename='address')

router.register('banner', viewsets.BaykeShopBannerViewSet, basename='banner')

urlpatterns = [
    # 创建商品
    path('spu/create/', viewsets.BaykeShopSPUCreateOrUpdateAPIView.as_view(), name='spu_create'),
    # 余额充值
    path('balance/create/', viewsets.BalanceRechargeAPIView.as_view(), name='user_balance_create'),
    
    *router.urls
]
