from django.core import management
from django.core.management.base import BaseCommand, CommandError

from django.conf import settings


class Command(BaseCommand):
    help = "导出初始数据"
    
    def handle(self, *args, **options):
        baykefrontedmenus = settings.BASE_DIR / 'baykeshop/conf/baykefrontedmenus.json'
        permission = settings.BASE_DIR / 'baykeshop/conf/permission.json'
        baykepermissionaction = settings.BASE_DIR / 'baykeshop/conf/baykepermissionaction.json'
        # baykesystem = settings.BASE_DIR / 'baykeshop/conf/baykesystem.json'
        # baykeemailconf = settings.BASE_DIR / 'baykeshop/conf/baykeemailconf.json'
        management.call_command('dumpdata', 'badmin.baykefrontedmenus', output=baykefrontedmenus)
        management.call_command('dumpdata', 'auth.permission', output=permission)
        management.call_command('dumpdata', 'badmin.baykepermissionaction', output=baykepermissionaction)
        # management.call_command('dumpdata', 'badmin.baykesystem', output=baykesystem)
        # management.call_command('dumpdata', 'badmin.baykeemailconf', output=baykeemailconf)
        self.stdout.write(self.style.SUCCESS(f"数据导出成功，导出数据路径在{settings.BASE_DIR / 'baykeshop/conf'}文件夹下"))