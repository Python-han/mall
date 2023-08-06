from django.urls import path, include

urlpatterns = [
    path('shop/', include(('baykeshop.api.shop.urls', 'baykeshop'), namespace="shop")),
    path('auth/', include(('baykeshop.api.auth.urls', 'baykeshop'), namespace='auth')),
    path('badmin/', include(('baykeshop.api.badmin.urls', 'baykeshop'), namespace='badmin')),
]