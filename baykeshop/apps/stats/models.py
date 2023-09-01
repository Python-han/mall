from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from django.utils import timezone
# Create your models here.
from baykeshop.common.models import BaseModelMixin, ContentTypeAbstract


class BaykeClientUser(BaseModelMixin):
    """Model definition for BaykeClientUser."""
    username = models.CharField(_("终端名称"), max_length=150)
    user_agent = models.CharField(_("浏览器"), max_length=250)
    ip = models.GenericIPAddressField(_("ip地址"), protocol='both', unpack_ipv4=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeClientUser."""
        ordering = ['-add_date']
        verbose_name = 'BaykeClientUser'
        verbose_name_plural = 'BaykeClientUsers'

    def __str__(self):
        """Unicode representation of BaykeClientUser."""
        return self.username
    
    @staticmethod
    def get_client_ip(request) -> str:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')


class BaykeDataStats(ContentTypeAbstract):
    """Model definition for BaykeDataStats."""
    pv = models.PositiveIntegerField(default=0, verbose_name=_("访问量"))
    uv = models.PositiveIntegerField(default=0, verbose_name=_("访客量"))

    # TODO: Define fields here

    class Meta:
        """Meta definition for BaykeDataStats."""
        ordering = ['-add_date']
        verbose_name = 'BaykeDataStats'
        verbose_name_plural = 'BaykeDataStatss'

    def __str__(self):
        """Unicode representation of BaykeDataStats."""
        return f"uv:{self.uv}-pv:{self.pv}"
    
    @classmethod
    def save_count(cls, request, content_type, object_id, tag=""):
        _meta = request.META
        username = _meta['USERNAME']
        user_agent = request.headers["User-Agent"]
        now = timezone.now()
        client_user = BaykeClientUser.objects.filter(
            username=username, 
            ip=BaykeClientUser.get_client_ip(request),
            add_date__date=now.date(),
        )
        stats, is_created = BaykeDataStats.objects.get_or_create(
            defaults={
                "content_type": content_type,
                "object_id": object_id
            },
            content_type=content_type,
            object_id=object_id,
            tag=tag
        )

        if not client_user.exists():
            BaykeClientUser.objects.create(
                username=username, 
                user_agent=user_agent,
                ip=BaykeClientUser.get_client_ip(request),
                add_date=timezone.now()
            )
            stats.uv = models.F('uv')+1
        stats.pv = models.F('pv')+1
        stats.save()
        return stats



