from django.urls import path, include

urlpatterns = [
    path('', include("baykeshop.apps.shop.urls")),
]