from collections import OrderedDict
from decimal import Decimal
from django.template import Library
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
from baykeshop.apps.shop.models import BaykeShopCart, BaykeShopCategory, BaykeShopSKU
from baykeshop.apps.comment.models import BaykeShopComment
from baykeshop.common import utils

register = Library()


def get_cates():
    data = BaykeShopCategory.objects.values("id", "name", "icon", "parent", "status")
    return data

def skurate(baykeshopsku_set):
    # 计算商品评分及评价内容
    if isinstance(baykeshopsku_set, list):
        sku_ids = [sku['id'] for sku in baykeshopsku_set]
        content_type = ContentType.objects.get_for_model(BaykeShopSKU)
        comments = BaykeShopComment.objects.filter(object_id__in=sku_ids, content_type=content_type)
        gte_3 = comments.filter(comment_choices__gte=3).count()
        rate = gte_3 / comments.count() if comments.count() else 0.98
        comment_choices__avg = comments.aggregate(Avg('comment_choices')).get('comment_choices__avg', 4.8)
        return {
            'comments': comments,
            'rate': rate * 100,
            'comment_choices__avg': round(comment_choices__avg, 1) if comment_choices__avg else 4.8
        }
    

@register.inclusion_tag("baykeshop/comp/navbar.html", takes_context=True)
def navbar(context):
    data = get_cates()
    return {
        'navs' : utils.generate_tree(data, None) if data else [],
        'words': context['request'].GET.get('search', '')
    } 
    
    
@register.simple_tag
def cartscount(request):
    # 购物车商品数量
    return BaykeShopCart.get_cart_count(request.user) if request.user.is_authenticated else 0


@register.inclusion_tag("baykeshop/comp/spubox.html", takes_context=False)
def spubox(spu):
    if isinstance(spu, OrderedDict):
        rate = skurate(spu['baykeshopsku_set'])
        sku =  spu['baykeshopsku_set'][0] if spu['baykeshopsku_set'] else {}
        spu['price'] = sku.get('price', 0)
        spu['sales'] = sku.get('sales', 0)
        spu['img'] = sku.get('img', "")
        spu['rate'] = rate['rate']
        spu['comment_choices__avg'] = rate['comment_choices__avg']
    else:
        sku_ids = spu.baykeshopsku_set.values_list("id", flat=True)
        content_type = ContentType.objects.get_for_model(BaykeShopSKU)
        comments = BaykeShopComment.objects.filter(object_id__in=sku_ids, content_type=content_type)
        gte_3 = comments.filter(comment_choices__gte=3).count()
        rate = gte_3 / comments.count() if comments.count() else 0.98
        comment_choices__avg = comments.aggregate(Avg('comment_choices')).get('comment_choices__avg', 4.8)
        sku = spu.baykeshopsku_set.order_by("price").first()
        if sku:
            spu.price = sku.price
            spu.sales = sku.sales
            spu.img = sku.img
            spu.comment_choices__avg = round(comment_choices__avg, 1) if comment_choices__avg else 4.8
    return {'spu': spu}


@register.simple_tag
def breadcrumbcate(category):
    return BaykeShopCategory.objects.filter(id__in=category)


@register.simple_tag
def filtercates(request):
    """ 全部商品及按分类筛选页通用数据 """
    cate = None
    sub_cates = []
    if request.query_params.get('category'):
        cate = BaykeShopCategory.objects.get(id=int(request.query_params.get('category')))
        
    cates = BaykeShopCategory.objects.filter(parent__isnull=True)
    
    if cates.exists():
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
    
@register.simple_tag
def totalPrice(ordersku):
    return ordersku['sku_json']['price'] * int(ordersku['count'])

@register.simple_tag
def ordersku(baykeordersku_set):
    spus = {BaykeShopSKU.objects.get(id=sku['sku']).spu  for sku in baykeordersku_set}
    total = sum([sku['count'] * Decimal(sku['sku_json']['price']) for sku in baykeordersku_set])
    freight = sum([spu.freight for spu in spus])
    is_commented = all([sku['is_commented'] for sku in baykeordersku_set])
    return {
        'count': sum([sku['count'] for sku in baykeordersku_set]),
        'total': total,
        'freight': freight,
        'total_amount': total + freight,
        'is_commented': is_commented
    }
    

@register.filter
def paystatus(val):
    status = "待付款"
    if val == 1:
        pass
    elif val == 2:
        status = "待发货"
    elif val == 3:
        status = "待收货"
    elif val == 4:
        status = "待评价"
    elif val == 5:
        status = "已完成"
    elif val == 6:
        status = "已关闭"
    elif val == 7:
        status = "退款中"
    return status


@register.filter
def paymethod(val):
    method = ""
    if val == 1:
        method = "支付宝支付"
    elif val == 2:
        method = "微信支付"
    elif val == 3:
        method = "余额支付"
    return method


@register.simple_tag
def comments(baykeshopsku_set):
    """ 商品详情页评价 """
    return skurate(baykeshopsku_set)


@register.filter
def change_status_format(val):
    status = ""
    if val == 1:
        status = "增加"
    elif val == 2:
        status = "支出"
    return status


@register.filter
def change_way_format(val):
    status = ""
    if val == 1:
        status = "线上充值"
    elif val == 2:
        status = "管理员手动修改"
    elif val == 3:
        status = "余额抵扣商品"
    return status