from django.db import models
from django.utils.translation import gettext_lazy as _
from baykeshop.common.models import BaseModelMixin


class BaykeShopCategory(BaseModelMixin):
    """Model definition for BaykeShopCategory."""
    name = models.CharField(_("名称"), max_length=50)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopCategory."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopCategory'
        verbose_name_plural = 'BaykeShopCategorys'

    def __str__(self):
        """Unicode representation of BaykeShopCategory."""
        return self.name


class BaykeshopBrand(BaseModelMixin):
    """Model definition for BaykeshopBrand."""
    name = models.CharField(_("品牌名称"), max_length=50)
    logo = models.ImageField(
        _("品牌logo"), upload_to="shop/brand/", max_length=200)
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeshopBrand."""
        ordering = ['-add_date']
        verbose_name = 'BaykeshopBrand'
        verbose_name_plural = 'BaykeshopBrands'

    def __str__(self):
        """Unicode representation of BaykeshopBrand."""
        return self.name


class BaykeShopSPU(BaseModelMixin):
    """Model definition for BaykeShopSPU."""
    title = models.CharField(_("标题"), max_length=80)
    subtitle = models.CharField(
        _("副标题"), max_length=150, blank=True, default="")
    content = models.TextField(_("详情"))
    category = models.ForeignKey(
        BaykeShopCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("分类"))
    brand = models.ForeignKey(
        BaykeshopBrand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("品牌"))

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSPU."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopSPU'
        verbose_name_plural = 'BaykeShopSPUs'

    def __str__(self):
        """Unicode representation of BaykeShopSPU."""
        return self.title


class BaykeShopBanner(BaseModelMixin):
    """Model definition for BaykeShopBanner."""
    spu = models.ForeignKey(
        BaykeShopSPU, on_delete=models.CASCADE, verbose_name=_("商品"))
    img = models.ImageField(_("图片"), upload_to="shop/banner/", max_length=200)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopBanner."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopBanner'
        verbose_name_plural = 'BaykeShopBanners'

    def __str__(self):
        """Unicode representation of BaykeShopBanner."""
        return self.spu.title


class BaykeShopUnit(BaseModelMixin):
    """Model definition for BaykeShopUnit."""
    name = models.CharField(_("名称"), max_length=50)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopUnit."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopUnit'
        verbose_name_plural = 'BaykeShopUnits'

    def __str__(self):
        """Unicode representation of BaykeShopUnit."""
        return self.name


class BaykeShopSpec(BaseModelMixin):
    """Model definition for BaykeShopSpec."""
    name = models.CharField(_("名称"), max_length=50)

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
    spec = models.ForeignKey(
        BaykeShopSpec, on_delete=models.CASCADE, verbose_name=_("规格"))
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
    unit = models.ForeignKey(BaykeShopUnit, on_delete=models.SET_DEFAULT,
                             default="", blank=True, verbose_name=_("单位"))
    img = models.ImageField(_("主图"), upload_to="shop/sku/",
                            max_length=200, blank=True, null=True)
    spu = models.ForeignKey(
        BaykeShopSPU, on_delete=models.CASCADE, verbose_name=_("商品"))
    spec_values = models.ManyToManyField(
        BaykeShopSpecValue, blank=True, verbose_name=_("规格"))
    price = models.DecimalField(_("售价"), max_digits=8, decimal_places=2)
    retail_price = models.DecimalField(
        _("零售价"), max_digits=10, decimal_places=2)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeShopSKU."""
        ordering = ['-add_date']
        verbose_name = 'BaykeShopSKU'
        verbose_name_plural = 'BaykeShopSKUs'

    def __str__(self):
        """Unicode representation of BaykeShopSKU."""
        return self.spu.title
