from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from baykeshop.common.models import BaseModelMixin


class BaykeUserBalanceLog(BaseModelMixin):
    """ 用户余额变动表 """
    
    class BalanceChangeStatus(models.IntegerChoices):
        # 收支状态
        ADD = 1, _('增加')
        MINUS = 2, _('支出')
    
    class BalanceChangeWay(models.IntegerChoices):
        # 收支渠道或方式
        PAY = 1, _('线上充值')        
        ADMIN = 2, _('管理员手动更改') 
        SHOP = 3, _('余额抵扣商品')
    
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="用户")
    amount = models.DecimalField("金额", max_digits=15, decimal_places=2)
    change_status = models.PositiveSmallIntegerField(
        choices=BalanceChangeStatus.choices, 
        blank=True,
        null=True
    )
    change_way = models.PositiveSmallIntegerField(
        choices=BalanceChangeWay.choices, 
        default=BalanceChangeWay.ADMIN        # 默认为后台
    )

    class Meta:
        verbose_name = '余额明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.owner.username}-{self.amount}"
    

class BaykeAddress(BaseModelMixin):
    """ 收货地址 """
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="用户")
    name = models.CharField("签收人", max_length=50)
    phone = models.CharField("手机号", max_length=11)
    email = models.EmailField("邮箱", blank=True, default="", max_length=50)
    province = models.CharField(max_length=150, verbose_name="省")
    city = models.CharField(max_length=150, verbose_name="市")
    county = models.CharField(max_length=150, verbose_name="区/县")
    address = models.CharField(max_length=150, verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="设为默认")
    
    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name
       
    def __str__(self):
        return f'{self.name} {self.address}'