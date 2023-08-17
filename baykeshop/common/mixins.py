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