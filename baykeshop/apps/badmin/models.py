#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :models.py
@说明    :后台菜单管理
@时间    :2023/07/16 10:14:45
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _

from baykeshop.conf import bayke_settings
from baykeshop.common.models import BaseModelMixin
from baykeshop.common.validators import validate_phone


class BaykeSiteMenus(BaseModelMixin):
    """ 后台管理菜单自定义 """
    name = models.CharField(_("名称"), max_length=50, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    icon = models.CharField(_("图标"), max_length=50, blank=True, default="")
    permission = models.OneToOneField(
        Permission, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        verbose_name=_("权限")
    )

    # TODO: Define fields here

    class Meta:
        ordering = ['-add_date']
        verbose_name = 'SiteMenus'
        verbose_name_plural = 'SiteMenus'

    def __str__(self):
        return self.name


class BaykeFrontedMenus(BaseModelMixin):
    """ 前后端分离管理菜单 """
    name = models.CharField(_("名称"), max_length=50, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    path = models.CharField("path", max_length=100, blank=True, default="")
    component = models.CharField("组件", max_length=50, blank=True, null=True)
    meta = models.JSONField(blank=True, null=True, verbose_name="meta")
    redirect = models.CharField(
        "跳转地址", 
        max_length=50, 
        blank=True, 
        default="", 
        help_text="格式应为`/home`"
    )
    sort = models.PositiveSmallIntegerField("排序", default=1)

    # TODO: Define fields here

    class Meta:
        ordering = ['sort']
        verbose_name = 'BaykeFrontedMenus'
        verbose_name_plural = 'BaykeFrontedMenus'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.meta:
            self.meta = {
                "title": self.name,
                "hidden": False,
                "affix": False,
                "icon": "menu",
                "type": "menu", # menu，button，iframe, link
                "hiddenBreadcrumb": False,
                "active": False,
                "color": "black",
                "fullpage": False
            }
        super().save(*args, **kwargs)


class BaykePermissionAction(BaseModelMixin):
    """Model definition for BaykePermissionAction."""
    class RequestMethod(models.TextChoices):
        GET = "GET", _("查看")
        POST = "POST", _("新增")
        PUT = "PUT", _("修改")
        PATCH = "PATCH", _("局部修改")
        DELETE = "DELETE", _("删除")
    
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE, verbose_name=_("权限"))
    menus = models.ForeignKey(BaykeFrontedMenus, on_delete=models.CASCADE, verbose_name=_("菜单"), blank=True, null=True)
    apiname = models.CharField(_("api接口name"), max_length=50, blank=True, default="", help_text="url的name别名，用来反解url")
    request_method = models.CharField(choices=RequestMethod.choices, max_length=10, blank=True, default="GET")
    mark = models.CharField(_("备注"), max_length=150, blank=True, default="")
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykePermissionAction."""
        ordering = ['-add_date']
        verbose_name = 'BaykePermissionAction'
        verbose_name_plural = 'BaykePermissionActions'

    def __str__(self):
        """Unicode representation of BaykePermissionAction."""
        return self.permission.codename


class BaykeDepartment(BaseModelMixin):
    """Model definition for department."""
    name = models.CharField("名称", max_length=50)
    parent = models.ForeignKey(
        "self", 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        verbose_name="上级部门"
    )
    mark = models.CharField("备注", max_length=150, blank=True, default="")
    sort = models.PositiveSmallIntegerField("排序", default=1)
    is_enable = models.BooleanField("启用状态", default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for department."""
        ordering = ["-sort", "-add_date"]
        verbose_name = 'department'
        verbose_name_plural = 'departments'
        constraints = [
            # 一个总公司下不能有相同的部门
            models.UniqueConstraint("name", "parent", name="dept_name_parent_unique")
        ]

    def __str__(self):
        """Unicode representation of department."""
        return self.name


class BaykeUser(BaseModelMixin):
    """Model definition for BaykeUser."""
    
    class UserType(models.TextChoices):
        FRONTED = "FRONTED", _("前台用户")
        SYSTEM = "SYSTEM", _("后台用户")
    
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name=_("用户"))
    name = models.CharField(_("姓名"), max_length=50)
    dept = models.ForeignKey(BaykeDepartment, on_delete=models.SET_NULL, verbose_name="归属部门", blank=True, null=True)
    phone = models.CharField("手机号", blank=True, null=True, max_length=11, validators=[validate_phone])
    user_type = models.CharField(choices=UserType.choices, default=UserType.SYSTEM, max_length=50, verbose_name=_("用户类型"))
    sex = models.PositiveSmallIntegerField(choices=((0, "未知"), (1, "男"), (2, "女")), default=0, verbose_name=_("性别"))
    about = models.CharField(_("简介"), max_length=150, default="我喜欢baykeshop这个程序！", blank=True)
    avatar = models.CharField(_("头像地址"), max_length=150, blank=True, default="/media/avatar.png")
    balance = models.DecimalField(_("余额"), max_digits=8, decimal_places=2, blank=True, default=0)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeUser."""
        ordering = ["-add_date"]
        verbose_name = 'BaykeUser'
        verbose_name_plural = 'BaykeUsers'

    def __str__(self):
        """Unicode representation of BaykeUser."""
        return self.name


class BaykeRoles(BaseModelMixin):
    """Model definition for BaykeRoles."""
    
    class PermRange(models.IntegerChoices):
        ALL = 1, _("全部可见")
        OWNER = 2, _("本人可见")
        DEPTS = 3, _("所在部门可见")
        DEPT = 4, _("所在部门及子级可见")
        SELECT = 5, _("选择的部门可见")
        CUSTOM = 6, _("自定义数据权限")
        
    group = models.OneToOneField(Group, on_delete=models.CASCADE, verbose_name=_("权限组"))
    codename = models.CharField(_("角色标识"), max_length=50, unique=True)
    depts = models.ManyToManyField(BaykeDepartment, blank=True, verbose_name="数据权限-关联部门")
    menus = models.ManyToManyField(BaykeFrontedMenus, blank=True, verbose_name=_("菜单"))
    perm_range = models.IntegerField(choices=PermRange.choices, default=PermRange.ALL, verbose_name=_("权限范围"))
    dashboard_grid = models.JSONField(blank=True, default=list, verbose_name=_("控制台模块权限"), help_text="当dashboard值为0时才有用！")
    dashboard = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name=_("控制台视图"))
    sort = models.IntegerField(default=0, verbose_name=_("排序"))
    status = models.BooleanField(default=True, verbose_name=_("状态"))
    remark = models.CharField(_("备注"), max_length=150, blank=True, default="")

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeRoles."""
        ordering = ["-sort"]
        verbose_name = 'BaykeRoles'
        verbose_name_plural = 'BaykeRoless'

    def __str__(self):
        """Unicode representation of BaykeRoles."""
        return self.codename


class BaykeDictKey(BaseModelMixin):
    """ 字典分类 """
    name = models.CharField(_("名称"), max_length=50)
    code = models.SlugField(_("字典名称"), max_length=50, unique=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("父级")
    )
    status = models.BooleanField(default=True, verbose_name=_("状态"))
    sort = models.PositiveIntegerField(default=1, verbose_name=_("排序"))
    
    # TODO: Define fields here

    class Meta:
        ordering = ['-sort']
        verbose_name = 'ByakeDictKey'
        verbose_name_plural = 'ByakeDictKeys'

    def __str__(self):
        return self.name
    
    
class BaykeDictValue(models.Model):
    """Model definition for BaykeDictValue."""
    name = models.CharField(_("名称"), max_length=50)
    key = models.CharField(_("值"), max_length=150)
    dic = models.ForeignKey(BaykeDictKey, on_delete=models.CASCADE, verbose_name=_("字典key"))
    status = models.BooleanField(default=True, verbose_name=_("状态"))
    sort = models.PositiveIntegerField(default=1, verbose_name=_("排序"))
    
    # TODO: Define fields here

    class Meta:
        ordering = ['-sort']
        verbose_name = 'BaykeDictValue'
        verbose_name_plural = 'BaykeDictValue'

    def __str__(self):
        return self.name


class BaykeImage(BaseModelMixin):
    """Model definition for BaykeImage."""
    img = models.ImageField(_("图片"), upload_to="upload/", max_length=200)
    sort = models.PositiveSmallIntegerField(default=1, verbose_name=_("排序"))
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeImage."""
        ordering = ['-sort']
        verbose_name = 'BaykeImage'
        verbose_name_plural = 'BaykeImages'

    def __str__(self):
        """Unicode representation of BaykeImage."""
        return self.img.name


class BaykeSystem(BaseModelMixin):
    """Model definition for BaykeSystem."""
    site_title = models.CharField(_("站点名称"), max_length=50, default="baykeshop商城系统")
    logo_url = models.URLField(_("logo地址"), max_length=200, blank=True, default="")
    extend_json = models.JSONField(_("扩展配置"), default=dict, blank=True, null=True)
    copyright = models.CharField(_("版权信息"), max_length=150, blank=True, default="baykeshop版权所有")

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeSystem."""

        verbose_name = 'BaykeSystem'
        verbose_name_plural = 'BaykeSystems'

    def __str__(self):
        """Unicode representation of BaykeSystem."""
        return self.site_title
    
    def save(self, *args, **kwargs):
        if BaykeSystem.objects.count() > 1:
            raise ValidationError("最多只能添加一条！")
        super().save(*args, **kwargs)


class BaykeEmailConf(BaseModelMixin):
    """Model definition for BaykeEmailConf."""
    email_host = models.CharField(_("邮箱发送后端"), max_length=50, default="smtp.qq.com")
    email_host_user = models.EmailField(_("发送邮箱号"), max_length=150, help_text=_("用于发送邮件的邮箱地址"))
    email_host_password = models.CharField(_("邮箱登录密码或授权码"), max_length=80, help_text=_("自己的邮箱密码，或授权码，一般现在的邮箱都需要授权码"))
    email_port = models.PositiveSmallIntegerField(_("邮箱服务器端口号"), default=465, help_text=_("QQ邮箱一般为465"))
    email_use_ssl = models.BooleanField(_("是否为隐式安全连接"), default=True)
    default_from_email = models.EmailField(_("发送邮件默认邮箱"), max_length=150, default="", blank=True)
    status = models.BooleanField(_("开启状态"), default=True)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeEmailConf."""

        verbose_name = 'BaykeEmailConf'
        verbose_name_plural = 'BaykeEmailConfs'

    def __str__(self):
        """Unicode representation of BaykeEmailConf."""
        return self.email_host_user

    def save(self, *args, **kwargs):
        if BaykeEmailConf.objects.count() > 1:
            raise ValidationError("最多只能添加一条！")
        if not self.default_from_email:
            self.default_from_email = self.email_host_user
        super().save(*args, **kwargs)
        

class BaykeSystemExtend(BaseModelMixin):
    """Model definition for BaykeSystemExtend."""
    key = models.SlugField(_("key"), max_length=150)
    value = models.CharField(_("字符串值"), max_length=200, blank=True, default="")
    title = models.CharField(_("配置标题"), max_length=80)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeSystemExtend."""
        ordering = ['-add_date']
        verbose_name = 'BaykeSystemExtend'
        verbose_name_plural = 'BaykeSystemExtends'

    def __str__(self):
        """Unicode representation of BaykeSystemExtend."""
        return self.key


class BaykeVerifyCode(BaseModelMixin):
    """Model definition for VerifyCode."""
    
    email = models.EmailField(_("邮箱"), max_length=254)
    code = models.CharField(_("验证码"), max_length=bayke_settings.CODE_LENGTH, blank=True, default="")
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for VerifyCode."""
        ordering = ['-add_date']
        verbose_name = 'VerifyCode'
        verbose_name_plural = 'VerifyCodes'

    def __str__(self):
        """Unicode representation of VerifyCode."""
        return f"{self.email}-{self.code}"
    
    def save(self, *args, **kwargs) -> None:
        from baykeshop.common.utils import code_random
        if not self.code:
            self.code = code_random()
        try:
            self.save_send_main(self.code)
            super().save(*args, **kwargs)
        except Exception as e:
            raise ValueError("邮箱账号密码可能有误，请检查！")
    
    def save_send_main(self, code):
        from django.core.mail import send_mail
        email_conf = BaykeEmailConf.objects.first()
        send_mail(
            subject="BaykeShop验证码, 请查收！", 
            message=f"您的验证码为：{code}, 请尽快验证，5分钟内有效！",
            from_email=email_conf.email_host_user,
            recipient_list=[self.email],
            fail_silently=False,
            auth_user=email_conf.email_host_user,
            auth_password=email_conf.email_host_password
        )
        
