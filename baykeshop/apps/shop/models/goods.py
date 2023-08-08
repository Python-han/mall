from django.db import models
from django.utils.translation import gettext_lazy as _
from baykeshop.common.models import BaseModelMixin
from baykeshop.common.validators import validate_count

class BaykeShopCategory(BaseModelMixin):
    """Model definition for BaykeShopCategory."""
    name = models.CharField(_("名称"), max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(_("分类图标"), upload_to="shop/category", max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField(_("排序"), default=1)
    status = models.BooleanField(_("状态"), default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopCategory."""
        ordering = ['-sort']
        verbose_name = 'BaykeShopCategory'
        verbose_name_plural = 'BaykeShopCategorys'

    def __str__(self):
        """Unicode representation of BaykeShopCategory."""
        return self.name


class BaykeshopBrand(BaseModelMixin):
    """Model definition for BaykeshopBrand."""
    name = models.CharField(_("品牌名称"), max_length=50)
    logo = models.ImageField(
        _("品牌logo"), upload_to="shop/brand/", max_length=200, blank=True, null=True)
    sort = models.PositiveSmallIntegerField(_("排序"), default=1)
    status = models.BooleanField(_("状态"), default=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeshopBrand."""
        ordering = ['-sort']
        verbose_name = 'BaykeshopBrand'
        verbose_name_plural = 'BaykeshopBrands'

    def __str__(self):
        """Unicode representation of BaykeshopBrand."""
        return self.name


class BaykeShopSPU(BaseModelMixin):
    """Model definition for BaykeShopSPU."""
    title = models.CharField(_("标题"), max_length=80)
    subtitle = models.CharField(_("副标题"), max_length=150, blank=True, default="")
    keywords = models.CharField(_("商品关键字"), max_length=150, blank=True, default="")
    desc = models.CharField(_("商品简介"), max_length=150, blank=True, default="")
    content = models.TextField(_("详情"))
    unit = models.CharField(_("单位"), max_length=50)
    images = models.JSONField(_("轮播图"), default=list, validators=[validate_count], blank=True)
    category = models.ManyToManyField(BaykeShopCategory, blank=True, verbose_name=_("分类"))
    brand = models.ForeignKey(BaykeshopBrand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("品牌"))
    skutype = models.PositiveSmallIntegerField(choices=((0, "单规格"), (1, "多规格")), default=0, blank=True, verbose_name="规格类型")
    freighttype = models.PositiveSmallIntegerField(choices=((0, "固定运费"), (1, "运费模板")), default=0, blank=True, verbose_name="运费类型")
    expresstype = models.PositiveSmallIntegerField(choices=((0, "快递"), (1, "上门自提")), default=0, blank=True, verbose_name="运费类型")
    freight = models.DecimalField(_("运费"), max_digits=8, decimal_places=2, blank=True, default=0)
    sort = models.IntegerField(default=1, verbose_name=_("排序"))
    status = models.BooleanField(default=True, verbose_name=_("商品状态(上下架)"))

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSPU."""
        ordering = ['-sort', '-add_date']
        verbose_name = 'BaykeShopSPU'
        verbose_name_plural = 'BaykeShopSPUs'

    def __str__(self):
        """Unicode representation of BaykeShopSPU."""
        return self.title

class BaykeShopSpec(BaseModelMixin):
    """Model definition for BaykeShopSpec."""
    name = models.CharField(_("名称"), max_length=50)
    sort = models.IntegerField(default=1, verbose_name=_("排序"))
    status = models.BooleanField(default=True, verbose_name=_("状态"))
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSpec."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopSpec'
        verbose_name_plural = 'BaykeShopSpecs'

    def __str__(self):
        """Unicode representation of BaykeShopSpec."""
        return self.name


class BaykeShopSpecValue(BaseModelMixin):
    """Model definition for BaykeShopSpecValue."""
    value = models.CharField(_("规格值"), max_length=50)
    spec = models.ForeignKey(BaykeShopSpec, on_delete=models.CASCADE, verbose_name=_("规格"))
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSpecValue."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopSpecValue'
        verbose_name_plural = 'BaykeShopSpecValues'

    def __str__(self):
        """Unicode representation of BaykeShopSpecValue."""
        return self.value


class BaykeShopSKU(BaseModelMixin):
    """Model definition for BaykeShopSKU."""

    stock = models.PositiveSmallIntegerField(_("库存"), default=0)
    sales = models.PositiveIntegerField(_("销量"), default=0)
    img = models.ImageField(_("主图"), upload_to="shop/sku/",
                            max_length=200, blank=True, null=True)
    spu = models.ForeignKey(
        BaykeShopSPU, on_delete=models.CASCADE, verbose_name=_("商品"))
    spec_values = models.ManyToManyField(
        BaykeShopSpecValue, blank=True, verbose_name=_("规格"))
    price = models.DecimalField(_("售价"), max_digits=8, decimal_places=2, blank=True, default=0.00)
    cost_price = models.DecimalField(_("成本价"), max_digits=8, decimal_places=2, blank=True, default=0.00)
    retail_price = models.DecimalField(
        _("零售价"), max_digits=10, decimal_places=2, blank=True, default=0.00)
    item = models.CharField(_("商品编号"), max_length=50, blank=True)
    weight = models.FloatField(_("重量"), blank=True, default=0)
    vol = models.FloatField(_("体积"), blank=True, default=0)
    status = models.BooleanField(default=True, verbose_name=_("商品状态(上下架)"))

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSKU."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopSKU'
        verbose_name_plural = 'BaykeShopSKUs'

    def __str__(self):
        """Unicode representation of BaykeShopSKU."""
        return self.spu.title
