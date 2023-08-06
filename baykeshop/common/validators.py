'''
@file            :validators.py
@Description     :验证器
@Date            :2023/07/17 17:11:50
@Author          :幸福关中 && 轻编程
@version         :v1.0
@EMAIL           :1158920674@qq.com
@WX              :baywanyun
'''
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from baykeshop.conf import bayke_settings

def validate_phone(value):
    # 中国区手机号验证
    reg = re.compile(bayke_settings.REGEX_PHONE)
    if not reg.search(value):
        raise ValidationError(
            _("%(value)s is not phone"),
            params={"value": value},
        )