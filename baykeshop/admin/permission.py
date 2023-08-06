from django.urls import resolve
from baykeshop.admin.menus import DynamicMenu


class PermissionMenus(DynamicMenu):
    """ 权限菜单 """
    def _get_queryset(self):
        return super()._get_queryset()


class PermissionHandler:
    """ 权限控制类 """
    
    def __init__(self, request) -> None:
        self.request = request
    
    @property
    def dynamic_menu_obj(self):
        # 获取当前用户的权限标识
        return PermissionMenus(self.request)
    
    def get_perm(self):
        resolver_match = resolve(self.request.path)
        # 当前url_name
        current_url_name = resolver_match.url_name
        # 视图
        view_func = resolver_match.func
        args = resolver_match.args      # 路由里的args
        kwargs = resolver_match.kwargs  # 路由里的关键字参数
        route = resolver_match.route
        captured_kwargs = resolver_match.captured_kwargs
        
        perm_menus = self.dynamic_menu_obj.get_permmenus()
        isperm = False
        
        match_results = []
        for menu in perm_menus:
            if not menu.permission:
                continue
            
            # 获取该菜单的菜单的权限标识
            app_label = menu.permission.content_type.app_label
            codename = menu.permission.codename
            info = f"{app_label}.{codename}"
            for p in menu.permissionaction_set.body():
                if p.url_name == current_url_name:
                    if p.action_type == self.request.method:
                        # 校验权限参数类型
                        if p.args and (not isinstance(p.args, (list or tuple))):
                            raise ValueError("校验参数填写类型不正确，应为list")
                        
                        # 反解出请求方式
                        request_method_func = (
                            self.request.query_params 
                            if self.request.method == 'GET'
                            else self.request.data
                        )
                        args_matched = False
                        # 校验必须要有的参数
                        for item in p.args:
                            # args参数校验通过
                            print(request_method_func)
                            if request_method_func.get(item, None):
                                args_matched = True
                            else:
                                # 有一个参数不匹配，失效该条整条权限
                                args_matched = False
                                break
                        else:
                            args_matched = True
                              
                        # 校验权限关键字参数类型
                        if p.kwargs and (not isinstance(p.kwargs, dict)):
                            raise ValueError("校验参数填写类型不正确，应为dict")
                        
                        kwargs_matched = True
                        for k, v in p.kwargs.items():
                            # kwargs参数校验通过
                            arg_val = request_method_func.get(k, None)
                            if arg_val == str(v):
                                kwargs_matched = True
                            else:
                                # 有一个参数不匹配，失效该条整条权限
                                kwargs_matched = False
                                break
                        else:
                            kwargs_matched = True

                        # 自定义权限
                        from django.utils.module_loading import import_string
                        has_custom_perm = True
                        try:
                            perm_func = import_string\
                                (p.custom_perm_func if p.custom_perm_func else "")\
                                (self.request, view_args=args, view_kwargs=kwargs)
                            has_custom_perm = True if perm_func else False
                        except ImportError:
                            pass
                        match_results = [args_matched, kwargs_matched, has_custom_perm]
                        
                        # 判断两个参数的校验结果，如果通过则修改权限表示跳出循环
                        if all(match_results):
                            isperm = True
                            break
        
        return isperm and self.request.user.has_perm(info)
