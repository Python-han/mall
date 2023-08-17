from collections import OrderedDict
from django.template import Library
from baykeshop.apps.shop.models import BaykeShopCart, BaykeShopCategory
from baykeshop.common import utils

register = Library()


def get_cates():
    data = BaykeShopCategory.objects.values("id", "name", "icon", "parent", "status")
    return data

@register.simple_tag
def catetags():
    return get_cates().filter(parent__isnull=True)


@register.inclusion_tag("baykeshop/comp/navbar.html")
def navbar():
    data = get_cates()
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
    
    if isinstance(spu, OrderedDict):
        sku =  spu['baykeshopsku_set'][0] if spu['baykeshopsku_set'] else {}
        spu['price'] = sku.get('price', 0)
        spu['sales'] = sku.get('sales', 0)
        spu['img'] = sku.get('img', "")
    else:     
        sku = spu.baykeshopsku_set.order_by("price").first()
        if sku:
            spu.price = sku.price
            spu.sales = sku.sales
            spu.img = sku.img
    return {'spu': spu}


@register.simple_tag
def breadcrumbcate(category):
    return BaykeShopCategory.objects.filter(id__in=category)


@register.simple_tag
def filtercates(request):
    """ 全部商品及按分类筛选页通用数据 """
    cate = None
    if request.query_params.get('category'):
        cate = BaykeShopCategory.objects.get(id=int(request.query_params.get('category')))
    
    cates = BaykeShopCategory.objects.filter(parent__isnull=True)
    sub_cates = cates.first().baykeshopcategory_set.all()

    if cate and cate.parent:
        sub_cates = cate.parent.baykeshopcategory_set.all()
    elif cate and cate.parent is None:
        sub_cates = cate.baykeshopcategory_set.all()
    return {
        'cates': cates,
        'sub_cates': sub_cates,
        'cate': cate
    }