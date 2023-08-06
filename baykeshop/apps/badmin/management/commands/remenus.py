import json
from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from baykeshop.apps.badmin.models import BaykeFrontedMenus


class Command(BaseCommand):
    help = "初始化菜单"
    
    def handle(self, *args, **options):
        menusJson_path = settings.BASE_DIR / 'baykeshop/conf/menus.json'
        with open(menusJson_path, encoding="utf-8") as f:
            menus = json.load(f)
        self.create_menu(menus)
        
    def create_menu(self, menus, parent=None): 
        name = ""
        iscreated = False
        for menu in menus:
            parent_menu, iscreated = BaykeFrontedMenus.objects.update_or_create(
                name=menu['name'],
                path=menu['path'],
                defaults={
                    'path':menu['path'],
                    'name':menu['name'],
                    'component':menu.get('component', ''),
                    'redirect': menu.get('redirect', ''),
                    'meta': menu['meta'],
                    'parent': parent
                }
            )
            name = parent_menu.name
            iscreated = iscreated
            if menu.get('children'):
                for submenu in menu.get('children'):
                    child_menu, iscreated = BaykeFrontedMenus.objects.update_or_create(
                        name=submenu['name'],
                        path=submenu['path'],
                        defaults={
                            'path':submenu['path'],
                            'name':submenu['name'],
                            'component':submenu.get('component', ''),
                            'redirect': submenu.get('redirect', ''),
                            'meta': submenu['meta'],
                            'parent': parent_menu
                        }
                    )
                    if submenu.get('children'):
                        self.create_menu(menu['children'], child_menu)
            success = f"{name}添加成功" if iscreated else f"{name}修改成功"
            self.stdout.write(self.style.SUCCESS(success))