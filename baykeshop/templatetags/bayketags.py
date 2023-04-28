from django.template import Library
from baykeshop.models import BaykeProductCategory

register = Library()


@register.inclusion_tag("baykeshop/comp/spubox.html")
def spubox(spu):
    sku = spu.baykeproductsku_set.order_by("price").first()
    if sku:
        spu.price = sku.price
        spu.sales = sku.sales
    return {
        'spu': spu
    }

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