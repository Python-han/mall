from baykeshop.common import viewsets
from baykeshop.apps.shop.models import BaykeShopCategory
from baykeshop.api.shop.serializers import BaykeShopCategorySerializer


class BaykeShopCategoryViewSet(viewsets.ModelViewSet):
    queryset = BaykeShopCategory.objects.all()
    serializer_class = BaykeShopCategorySerializer
    permission_classes = []