from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from baykeshop.common.models import BaseModelMixin
from .goods import BaykeShopSKU


class BaykeShopOrder(BaseModelMixin):
    """Model definition for BaykeShopOrder."""

    class PayMethod(models.TextChoices):
        ALIPAY = "ALIPAY", _("支付宝支付")
        WXPAY = "WXPAY", _("微信支付")
        BALANCE = "BALANCE", _("余额支付")

        __empty__ = _("(Unknown)")

    class OrderStatus(models.TextChoices):
        UNPAID = "UNPAID", _("待付款")
        UNSHIP = "UNSHIP", _("待发货")
        UNGOODS = "UNGOODS", _("待收货")
        UNCOMMENT = "UNCOMMENT", _("待评价")
        DONE = "DONE", _("已完成")
        CLOSED = "CLOSED", _("已关闭")
        REFUND = "REFUND", _("退款中")

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("用户"))
    status = models.CharField(choices=OrderStatus.choices,
                              default=OrderStatus.UNPAID, max_length=50, verbose_name=_("订单状态"))
    paymethod = models.CharField(
        choices=PayMethod.choices, default=PayMethod.__empty__, max_length=50, verbose_name=_("支付方式"))
    order_sn = models.CharField(_("订单号"), max_length=100)
    total_price = models.DecimalField(_("总价"), max_digits=10, decimal_places=2)
    mark = models.CharField(_("订单备注"), max_length=150, blank=True, default="")
    name = models.CharField("签收人", max_length=50)
    phone = models.CharField("手机号", max_length=11)
    email = models.EmailField("邮箱", blank=True, default="", max_length=50)
    address = models.CharField("收货地址", max_length=200)
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间", help_text="支付时间", editable=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopOrder."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopOrder'
        verbose_name_plural = 'BaykeShopOrders'
        constraints = [
            models.UniqueConstraint('owner', 'order_sn', name='unique_owner_order'),
        ]

    def __str__(self):
        """Unicode representation of BaykeShopOrder."""
        return self.order_sn

    def save(self, *args, **kwargs):
        if not self.order_sn:
            self.order_sn = self.generate_order_sn()
        super().save(*args, **kwargs)

    def generate_order_sn(self):
        # 当前时间 + userid + 随机数
        from random import Random
        from django.utils import timezone
        random_ins = Random()
        order_sn = "{time_str}{user_id}{ranstr}".format(
            time_str=timezone.now().strftime("%Y%m%d%H%M%S"),
            user_id=self.owner.id,
            ranstr=random_ins.randint(10, 99))
        return order_sn


class BaykeShopOrderSKU(BaseModelMixin):
    """Model definition for BaykeShopOrderSKU."""
    order = models.ForeignKey(
        BaykeShopOrder, on_delete=models.CASCADE, verbose_name=_("订单"))
    sku = models.ForeignKey(
        BaykeShopSKU, on_delete=models.PROTECT, verbose_name=_("商品规格"))
    count = models.PositiveSmallIntegerField(default=1, verbose_name=_("数量"))
    sku_json = models.JSONField(verbose_name=_("商品快照"), blank=True, default=dict)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopOrderSKU."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopOrderSKU'
        verbose_name_plural = 'BaykeShopOrderSKUs'

    def __str__(self):
        """Unicode representation of BaykeShopOrderSKU."""
        return self.order.order_sn

    def save(self, *args, **kwargs):
        self.sku_json = {
            "title": self.sku.spu.title,
            "content": self.sku.spu.content,
            "price": self.sku.price.to_eng_string(),
            "retail_price": self.sku.retail_price.to_eng_string(),
            "unit": self.sku.unit.name
        }
        super().save(*args, **kwargs)
