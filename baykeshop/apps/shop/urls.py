from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('goods/<int:pk>/', views.BaykeShopSPUView.as_view({'get': 'retrieve'}), name="spu-detail"),
    path('goods/', views.BaykeShopSPUView.as_view({'get': 'list'}), name="spu-list"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.BaykeRegisterView.as_view(), name='register'),
]