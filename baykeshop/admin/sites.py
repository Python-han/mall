from django.contrib import admin

from baykeshop.conf import bayke_settings


class AdminSite(admin.AdminSite):
    
    site_header = "baykeshop"
    site_title = "baykeshop"
    
    def get_app_list(self, request, app_label=None):
        if bayke_settings.CUSTOM_MENU:
            from baykeshop.admin.menus import MenusMixins
            menu = MenusMixins()
            return menu.get_menus(request)
        return super().get_app_list(request)