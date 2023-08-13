from django.urls import path
from . import views

urlpatterns = [
    # 获取token post
    path("token/", views.TokenObtainPairView.as_view(), name="token"),
    # 刷新token post
    path("refresh/", views.TokenRefreshView.as_view(), name="refresh"),
    # 验证token post 
    path("verify/", views.TokenVerifyView.as_view(), name="verify"),
    # 退出
    path("logout/", views.LogoutView.as_view(), name="logout")
]