from django_filters import rest_framework
from baykeshop.apps.shop.models import BaykeShopSPU, BaykeShopOrder


class BaykeShopSPUFilterSet(rest_framework.FilterSet):
    """ spu筛选 """
    groupId = rest_framework.ChoiceFilter(method='group_filter', choices=(
            (1, "出售中"), 
            (2, "仓库中"), 
            (3, "已售罄"),
            (4, "警戒库存"),
            (5, "回收站")
        )
    )
    brand = rest_framework.CharFilter(method='brand_filter')
    category = rest_framework.CharFilter(method='category_filter')
    
    class Meta:
        model = BaykeShopSPU
        fields = ('brand', 'category', 'groupId')
    
    def group_filter(self, queryset, name, value):
        queryset = queryset
        if int(value) == 1:
            queryset = queryset.filter(status=True)
        elif int(value) == 2:
            queryset = queryset.filter(status=False)
        elif int(value) == 3:
            queryset = queryset.filter(status=True, baykeshopsku__stock__lte=0).distinct()
        elif int(value) == 4:
            queryset = queryset.filter(status=True, baykeshopsku__stock__gte=5).distinct()
        elif int(value) == 5:
            queryset = queryset.nobody()
        return queryset
    
    def brand_filter(self, queryset, name, value):
        # 按品牌筛选
        if int(value) != 0:
            queryset = queryset.filter(brand__id=int(value))
        return queryset
    
    def category_filter(self, queryset, name, value):
        # 按分类多选筛选
        ids = value.split(',')
        if len(ids) >= 1 and ids[0] != '0':
            ids = [int(i) for i in value.split(',')]
            queryset = queryset.filter(category__id__in=ids).distinct()
        return queryset
    

class BaykeShopOrderFilterSet(rest_framework.FilterSet):
    """ 订单筛选器 """
    class Meta:
        model = BaykeShopOrder
        fields = ('status', 'paymethod',)