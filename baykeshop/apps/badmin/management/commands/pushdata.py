from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "导入初始数据"
    
    def handle(self, *args, **options):
        baykefrontedmenus = settings.BASE_DIR / 'baykeshop/conf/baykefrontedmenus.json'
        permission = settings.BASE_DIR / 'baykeshop/conf/permission.json'
        baykepermissionaction = settings.BASE_DIR / 'baykeshop/conf/baykepermissionaction.json'
        baykesystem = settings.BASE_DIR / 'baykeshop/conf/baykesystem.json'
        baykeemailconf = settings.BASE_DIR / 'baykeshop/conf/baykeemailconf.json'
        management.call_command('loaddata', baykefrontedmenus, verbosity=0)
        management.call_command('loaddata', permission, verbosity=0)
        management.call_command('loaddata', baykepermissionaction, verbosity=0)
        management.call_command('loaddata', baykesystem, verbosity=0)
        management.call_command('loaddata', baykeemailconf, verbosity=0)
        self.stdout.write(self.style.SUCCESS("数据导入成功！"))