from baykeshop.views.public import HomeTemplateView
from baykeshop.views.product import (
    BaykeProductCategoryListView, BaykeProductSPUListView, 
    BaykeSearchView, BaykeProductSPUDetailView
)
from baykeshop.views.cart import BaykeCartListView
from baykeshop.views.order import (
    BaykeOrderConfirmView, BaykeOrderPayMethodView, BaykeAlipayNotifyView,
    BaykeOrderView
)
from baykeshop.views.user import (
    LoginView, LogoutView, BaykeRegisterView, BaykeUserMenmberView,
    BaykeAddressView
)
from baykeshop.views.article import(
    BaykeArticleView, BaykeArticleCategoryView, BaykeArticleTagView
)