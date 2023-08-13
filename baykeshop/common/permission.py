from django.urls import resolve
from rest_framework import permissions
from baykeshop.apps.badmin.models import BaykeFrontedMenus


class BaykePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # print(request.user)
        # 超管不受权限约束
        if request.user.is_superuser:
            return True
        
        # 反向解析当前访问的接口
        resolver_match = resolve(request.path)
        # 获取当前访问的接口url_name
        current_url_name = resolver_match.url_name
        # 权限放行标识
        has_perm = False
        # 循环执行菜单权限比对
        menu_perms = self.get_menu_perms(request)
        for menu in menu_perms:
            if not menu.permission:
                # 跳出循环执行下一个循环
                continue
            # 获取该菜单的菜单的权限标识
            app_label = menu.permission.content_type.app_label
            codename = menu.permission.codename
            info = f"{app_label}.{codename}"
            # 校验url 和 请求方式
            if menu.apiname == current_url_name and menu.request_method == request.method:
                has_perm = True
                
        print(request.user.has_perm(info))
        return has_perm and request.user.has_perm(info)
    
    def has_object_permission(self, request, view, obj):
        # print(obj)
        # print(view.args)
        # print(view.kwargs)
        # print(view.http_method_not_allowed(request))
        return super().has_object_permission(request, view, obj)
    
    def get_user_menus(self, request):
        """ 当前用户的权限菜单 """
        roles = request.user.groups.values_list("baykeroles__id", flat=True)
        menus_queryset = BaykeFrontedMenus.objects.filter(baykeroles__id__in=list(roles))
        if request.user.is_superuser:
            menus_queryset = BaykeFrontedMenus.objects.all()
        return menus_queryset
    
    def get_menu_perms(self, request):
        perms = []
        menus = self.get_user_menus(request)
        for menu in menus:
            perms.extend(list(menu.baykepermissionaction_set.all()))
        return perms
            
       
    