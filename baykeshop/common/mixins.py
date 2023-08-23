from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings

from . import serializers


class CreateModelMixin(mixins.CreateModelMixin):
    pass


class ListModelMixin(mixins.ListModelMixin):
    pass


class RetrieveModelMixin(mixins.RetrieveModelMixin):
    pass


class DestroyModelMixin(mixins.DestroyModelMixin):
    pass


class UpdateModelMixin(mixins.UpdateModelMixin):
    pass


class BatchDestroyModelMixin:
    """ 批量删除 """
    def batch_destroy(self, request, *args, **kwargs):
        serializer = serializers.BatchDestroySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_batch_destroy(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

    def perform_batch_destroy(self, serializer):
        ids = serializer.data.get('ids', [])
        self.get_queryset().filter(id__in=ids).delete()
        
    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class CheckVerifyCodeMixin:
    """ 验证码单独效验 """
    
    def verify(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        self.check_code(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    
    def check_code(self, serializer):
        # 验证
        serializer.is_valid(raise_exception=True)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        

class AlipayCallBackVerifySignMixin:
    """ 支付宝支付回调，验签 """
    
    def has_verify_sign(self, data):
        """ 验签
        data是从请求中获得的字典数据，携带 sign和sign_type
        """
        from baykeshop.pay.alipay.client import _alipay_public_key
        from alipay.aop.api.util.SignatureUtils import verify_with_rsa
        sign = data.pop('sign')
        sign_type = data.pop('sign_type')
        alipay_public_key = _alipay_public_key
        # 去除sign和sign_type参数之后进行升序排列，拼装请求参数用支付宝公钥进行验签
        message='&'.join([f"{k}={v}" for k, v in dict(sorted(data.items(), key=lambda d: d[0], reverse=False)).items()])
        flag = verify_with_rsa(alipay_public_key, message.encode('UTF-8','strict'), sign)
        return flag