from django.urls import resolve
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from baykeshop.apps.badmin.models import BaykePermissionAction


class BaykePermission(permissions.BasePermission):
    
    authenticated_users_only = False
    is_authenticated = False
    
    def has_permission(self, request, view):
        is_auth = self.is_authenticated if self.is_authenticated else bool(request.user and request.user.is_authenticated)
        # 反向解析当前访问的接口
        resolver_match = resolve(request.path)
        # 获取当前访问的接口url_name
        current_url_name = resolver_match.url_name
        # 权限放行标识
        has_perm = False
        # 循环执行菜单权限比对
        perms = request.user.get_all_permissions()
        print(current_url_name)
        # 是否开放get权限不受控制    
        if self.authenticated_users_only and is_auth and (request.method in SAFE_METHODS):
            return True
    
        # 超管不受权限约束
        if request.user.is_superuser:
            return True
        
        for perm in perms:
            perm_split = perm.split('.')
            actions = BaykePermissionAction.objects.filter(
                permission__content_type__app_label=perm_split[0],
                permission__codename=perm_split[1]
            )
            for action in actions:
                if action.apiname == current_url_name and action.request_method.lower() == request.method.lower():
                    has_perm = True
        return has_perm and is_auth
            
    
    def has_object_permission(self, request, view, obj):
        # print(obj)
        # print(view.args)
        # print(view.kwargs)
        # print(view.http_method_not_allowed(request))
        return super().has_object_permission(request, view, obj) 
       

class BaykePermissionOrReadOnly(BaykePermission):
    """ get请求不受任何限制,且无需登录 """
    authenticated_users_only = True
    is_authenticated = True
    
    
class BaykePermissionAuthReadOnly(BaykePermission):
    """ get请求仅接受登录访问，不受权限系统控制 """
    authenticated_users_only = True
    is_authenticated = False


class IsOwnerAuthenticated(permissions.IsAuthenticated):
    """ 仅拥有获取自己个人相关信息的权限 """
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.owner)