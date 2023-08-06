from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from baykeshop.common.models import BaseModelMixin
from .goods import BaykeShopSKU


class BaykeShopCart(BaseModelMixin):
    """Model definition for BaykeShopCart."""
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("用户"))
    sku = models.ForeignKey(BaykeShopSKU, on_delete=models.CASCADE, verbose_name=_("规格"))
    num = models.PositiveSmallIntegerField(default=1, verbose_name=_("数量"))
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopCart."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopCart'
        verbose_name_plural = 'BaykeShopCarts'
        constraints = [
            models.UniqueConstraint('owner', 'sku', name='unique_owner_sku'),
        ]

    def __str__(self):
        """Unicode representation of BaykeShopCart."""
        return self.sku.spu.title
