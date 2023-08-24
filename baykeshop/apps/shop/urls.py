from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name="home"),
    path('goods/<int:pk>/', views.BaykeShopSPUView.as_view({'get': 'retrieve'}), name="spu-detail"),
    path('goods/', views.BaykeShopSPUView.as_view({'get': 'list'}), name="spu-list"),
    path('cart/', views.BaykeShopCartView.as_view({'get': 'list'}), name="cart-list"),
    
    path('order/', views.BaykeShopOrderView.as_view({'get':'list'}), name='order-list'),
    path('order/create/', views.BaykeShopOrderView.as_view({'post': 'create'}), name="order-create"),
    path('order/<int:pk>/confirm/', views.BaykeShopOrderView.as_view({'get': 'orderconfirm'}), name="order-confirm"),
    # 发起支付请求
    path('order/<int:pk>/pay/', views.BaykeShopOrderView.as_view({'patch': 'partial_update'}), name="order-pay"),
    path('order/<int:pk>/confirmok/', views.BaykeShopOrderView.as_view({'post': 'confirmok', 'get': 'confirmok'}), name="order-confirmok"),
    path('order/<int:pk>/comment/', views.BaykeShopOrderView.as_view({'get': 'ordercomment', 'post': 'ordercomment'}), name="order-comment"),
    # 余额支付
    path('order/<int:pk>/paybanlance', views.BaykeShopOrderView.as_view({'get': 'paybanlance'}), name="order-banlancepay"),


    path('menmber/', views.BaykeUserView.as_view(), name='menmber'),
    path('user/<int:pk>/patch/', views.BaykeUserUpdateView.as_view({'patch': 'partial_update'}), name='user-update'),
    path('balance/', views.BaykeUserUpdateView.as_view({'get': 'balance'}), name='balance'),
    
    path('address/', views.BaykeAddressView.as_view({'get': 'list'}), name='address'),
    # 支付宝支付后回调
    path('alipay/', views.AliPayCallBackView.as_view(), name='alipay'),
    # 余额充值后回调
    path('balance_recharge/', views.BalanceRechargeAliPayCallBackView.as_view(), name='balance_recharge'),
    
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.BaykeRegisterView.as_view(), name='register'),
]