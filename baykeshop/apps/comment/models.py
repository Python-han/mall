from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.
from baykeshop.common.models import ContentTypeAbstract


class BaykeShopComment(ContentTypeAbstract):
    """ 模型的通用关系 """
    
    class CommentChoices(models.IntegerChoices):
        GOOD = 5, _('好评')
        SO = 3, _('中评')
        BAD = 1, _('差评')
        
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="用户")
    content = models.CharField("留言内容", max_length=200)
    reply = models.CharField("回复内容", max_length=200, blank=True, default="")
    comment_choices = models.PositiveSmallIntegerField(
        default=5,
        choices=CommentChoices.choices,
        verbose_name="评分"
    )

    class Meta:
        ordering = ['-add_date']
        verbose_name = 'BaykeShopComment'
        verbose_name_plural = 'BaykeShopComment'
        
    def __str__(self):
        return self.content