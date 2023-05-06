import random
import string

from rest_framework import renderers
from baykeshop.conf import bayke_settings


def code_random(code_length=bayke_settings.CODE_LENGTH):
    """ 生成指定位数随机字符串方法 """
    # chars = string.ascii_letters + string.digits   # 生成a-zA-Z0-9字符串
    chars = string.digits
    strcode = ''.join(random.sample(chars, code_length))  # 生成随机的8位数字符串
    return strcode


class TemplateHTMLRenderer(renderers.TemplateHTMLRenderer):
    """ 修复为list时渲染html错误 """
    def get_template_context(self, data, renderer_context):
        context = super().get_template_context(data, renderer_context)
        if isinstance(context, list):
            context = {'datas': context}
        return context