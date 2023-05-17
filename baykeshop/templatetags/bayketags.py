from django.template import Library

from baykeshop.conf import bayke_settings
from baykeshop.models import (
    BaykeProductCategory, BaykePermission, BaykeCart,
    BaykeArticleCategory, BaykeProductSPU
)
from baykeshop.forms import SearchForm


register = Library()


@register.inclusion_tag("baykeshop/comp/spubox.html", takes_context=True)
def spubox(context, spu):
    request = context['request']
    sort = request.GET.get('price', '').startswith('-')
    sku = spu.baykeproductsku_set.order_by("-price" if sort else "price").first()
    if sku:
        spu.price = sku.price
        spu.sales = sku.sales
    return {'spu': spu}


# @register.simple_tag
# def navbar():
#     # 导航菜单
#     return BaykeProductCategory.get_cates()

@register.inclusion_tag("baykeshop/comp/navbar.html", takes_context=True)
def navbar(context):
    request = context['request']
    return {
        "pc_logo": bayke_settings.PC_LOGO,
        "navs": BaykeProductCategory.get_cates(),
        "word": request.GET.get("search", ''),
        "placeholder": bayke_settings.SEARCH_VALUE
    }

 
@register.simple_tag
def filtercates(cate=None):
    """ 全部商品及按分类筛选页通用数据 """
    cates = BaykeProductCategory.objects.filter(parent__isnull=True)
    sub_cates = cates.first().baykeproductcategory_set.all()

    if cate and cate.parent:
        sub_cates = cate.parent.baykeproductcategory_set.all()
    elif cate and cate.parent is None:
        sub_cates = cate.baykeproductcategory_set.all()
    return {
        'cates': cates,
        'sub_cates': sub_cates
    }
    

@register.simple_tag
def cartscount(request):
    # 购物车商品数量
    return BaykeCart.get_cart_count(request.user) if request.user.is_authenticated else 0


@register.filter
def paymethod(value):
    v = ""
    if value == 1:
        v = "货到付款"
    elif value == 2:
        v = "支付宝"
    elif value == 3:
        v = "微信支付"
    elif value == 4:
        v = "余额支付"
    else:
        v = "待支付"
    return v


@register.filter
def paystatus(value):
    s = ''
    if value == 1:
        s = "待支付"
    elif value == 2:
        s = "待发货"
    elif value == 3:
        s = "待收货"
    elif value == 4:
        s = "待评价"
    elif value == 5:
        s = "已完成"
    elif value == 6:
        s = "已取消"
    return s


@register.filter
def ordercount(baykeordersku_set):
    # 订单商品数据量
    return sum([sku.get('count', 0) for sku in baykeordersku_set])


@register.simple_tag
def breadcrumbs(request, opts=None):
    if bayke_settings.ADMIN_MENUS:
        if opts:
            p = BaykePermission.objects.filter(
                permission__content_type__app_label=opts.app_label,
                permission__content_type__model=opts.model_name
            )
            request.breadcrumbs = {
                p.first().menus.name: {
                    'name': str(opts.verbose_name_plural), 
                    'url': request.path
                }
            }
            return request.breadcrumbs
        return request.breadcrumbs
    else:
        return None


@register.inclusion_tag("baykeshop/comp/pages.html", takes_context=True)
def pages(context, page_obj):
    # 分页，适配django,不兼容drf接口
    return {
        "page_obj": page_obj,
        "page_range": page_obj.paginator.get_elided_page_range(int(context['request'].GET.get('page', 1))),
        "current": int(context['request'].GET.get('page', 1))
    }


@register.simple_tag
def article_cates():
    # 文章分类
    return BaykeArticleCategory.objects.all()


@register.simple_tag
def spuhots():
    # 热销排行
    spus = []
    for spu in BaykeProductSPU.objects.order_by('-baykeproductsku__sales')[:6]:
        if spu not in spus:
            spus.append(spu)
    return spus