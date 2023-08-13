from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from . import mixins, permission


class GenericViewSet(viewsets.GenericViewSet):
    """
    The GenericViewSet class does not provide any actions by default,
    but does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """
    permission_classes = [permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter) # DRF自带的过滤器
    search_fields = ()
    ordering_fields = "__all__"


class ModelViewSet(mixins.BatchDestroyModelMixin, viewsets.ModelViewSet):
    """ 全局继承类 """
    permission_classes = [permission.BaykePermission]
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter) # DRF自带的过滤器
    search_fields = ()
    ordering_fields = "__all__"

    @action(methods=['delete'], detail=False)
    def batch_destroy(self, request, *args, **kwargs):
        return super().batch_destroy(request, *args, **kwargs)