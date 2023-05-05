from django.template import Library

from baykeshop.conf import bayke_settings
from baykeshop.models import BaykeProductCategory, BaykePermission, BaykeCart

register = Library()


@register.inclusion_tag("baykeshop/comp/spubox.html")
def spubox(spu):
    sku = spu.baykeproductsku_set.order_by("price").first()
    if sku:
        spu.price = sku.price
        spu.sales = sku.sales
    return {'spu': spu}


@register.simple_tag
def navbar():
    return BaykeProductCategory.get_cates()

 
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
    