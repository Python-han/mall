from django.urls import path
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('menus', viewsets.BaykeFrontedMenusViewSet, basename='menus')

router.register('dept', viewsets.BaykeDepartmentViewSet, basename='dept')

router.register('users', viewsets.BaykeUserViewset, basename='users')

router.register('roles', viewsets.BaykeRolesViewSet, basename='roles')

router.register('user/add', viewsets.UserCreateViewset, basename='user_add')

router.register('action', viewsets.BaykePermissionActionViewSet, basename='action')

router.register('dictkey', viewsets.BaykeDictKeyViewSet, basename='dict_key')

router.register('dictvalue', viewsets.BaykeDictValueViewSet, basename='dict_value')

router.register('imgs', viewsets.BaykeImageViewset, basename='imgs')

router.register('system', viewsets.BaykeSystemViewset, basename='system')

router.register('emailconf', viewsets.BaykeEmailConfViewset, basename='emailconf')

router.register('system_extend', viewsets.BaykeSystemExtendViewset, basename='system_extend')

router.register('content_type', viewsets.ContentTypeViewset, basename='content_type')

urlpatterns = [
    
    path('user/', viewsets.BaykeUserRetrieveAPIView.as_view(), name='user'),
    
    # django的权限列表
    path('perms/', viewsets.PermissionListAPIView.as_view(), name='perms'),
        
    path('readsystem/<str:field_name>/', viewsets.BaykeSystemViewset.as_view({'get': 'readsystem'}), name='readsystem'),
    
    *router.urls
]