import rest_framework.serializers as ser
from baykeshop.common import serializers
from baykeshop.apps.shop.models import BaykeShopCategory


class BaykeShopCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BaykeShopCategory
        fields = "__all__"

