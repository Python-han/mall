from django.contrib import admin

# Register your models here.
from . models import (
    BaykeShopSPU, BaykeShopOrderSKU, BaykeShopSKU, BaykeshopBrand, BaykeShopCart, BaykeShopCategory,
    BaykeShopOrder, BaykeShopSpec, BaykeShopSpecValue 
)

admin.site.register([
    BaykeShopSPU, BaykeShopOrderSKU, BaykeShopSKU, BaykeshopBrand, BaykeShopCart, BaykeShopCategory,
    BaykeShopOrder, BaykeShopSpec, BaykeShopSpecValue 
])