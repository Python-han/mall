from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('goods/<int:pk>/', views.BaykeShopSPUView.as_view({'get': 'retrieve'}), name="spu-detail"),
    path('goods/', views.BaykeShopSPUView.as_view({'get': 'list'}), name="spu-list"),
]