from django.urls import path
from . import views

urlpatterns = [
    # 获取token post
    path("token/", views.TokenObtainPairView.as_view(), name="token"),
    # 刷新token post
    path("refresh/", views.TokenRefreshView.as_view(), name="refresh"),
    # 验证token post 
    path("verify/", views.TokenVerifyView.as_view(), name="verify"),
    # 退出 post
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # 获取邮箱验证码
    path('obtain/code/', views.BaykeVerifyCodeObtainAPIView.as_view(), name='obtain-code'),
    # 效验邮箱验证码 post
    path('check/code/', views.BaykeVerifyCodeCheckAPIView.as_view(), name='check-code'),
    # 注册接口 post
    path("register/", views.BaykeUserRegisterAPIView.as_view(), name="register-api"),
    # 修改自己的密码 post
    path("user/changepassword/", views.UpdateUserPasswordView.as_view(), name="user-changepassword"),
    # 修改指定用户的密码 post
    path("owner/changepassword/", views.UpdateOwnerPasswordView.as_view(), name="owner-changepassword"),
]