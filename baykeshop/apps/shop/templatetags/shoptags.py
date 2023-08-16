from django.template import Library
from rest_framework.utils.serializer_helpers import ReturnList

from baykeshop.apps.shop.views import BaykeShopCategoryView
from baykeshop.apps.shop.models import BaykeShopCart, BaykeShopCategory
from baykeshop.common import utils

register = Library()


@register.inclusion_tag("baykeshop/comp/navbar.html")
def navbar():
    data = BaykeShopCategory.objects.values("id", "name", "icon", "parent", "status")
    return {
        'navs' : utils.generate_tree(data, None) if data else []
    } 
    
    
@register.simple_tag
def cartscount(request):
    # 购物车商品数量
    return BaykeShopCart.get_cart_count(request.user) if request.user.is_authenticated else 0


@register.inclusion_tag("baykeshop/comp/spubox.html", takes_context=True)
def spubox(context, spu):
    request = context['request']
    sku = spu.baykeshopsku_set.order_by("price").first()
    if sku:
        spu.price = sku.price
        spu.sales = sku.sales
        spu.img = sku.img
    return {'spu': spu}


@register.simple_tag
def breadcrumbcate(category):
    return BaykeShopCategory.objects.filter(id__in=category)