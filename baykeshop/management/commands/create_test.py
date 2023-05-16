from django.core.management.base import BaseCommand
from django.core import management
from django.conf import settings


class Command(BaseCommand):
    
    help = '创建测试数据'
    
    def add_arguments(self, parser) -> None:
        pass
    
    def handle(self, *args, **options):
        baykebanner = f"{settings.BASE_DIR}/baykeshop/conf/data/baykebanner.json"
        baykecategory = f"{settings.BASE_DIR}/baykeshop/conf/data/baykeproductcategory.json"
        baykespec = f"{settings.BASE_DIR}/baykeshop/conf/data/baykeproductspec.json"
        baykespecoptions = f"{settings.BASE_DIR}/baykeshop/conf/data/baykespecoption.json"
        baykegoods = f"{settings.BASE_DIR}/baykeshop/conf/data/baykeproductspu.json"
        baykegoodsbanners = f"{settings.BASE_DIR}/baykeshop/conf/data/baykeproductbanner.json"
        baykeproduct = f"{settings.BASE_DIR}/baykeshop/conf/data/baykeproductsku.json"
        baykearticlecategory = f"{settings.BASE_DIR}/baykeshop/conf/data/baykearticlecategory.json"
        baykearticle = f"{settings.BASE_DIR}/baykeshop/conf/data/baykearticle.json"
        baykearticletag = f"{settings.BASE_DIR}/baykeshop/conf/data/baykearticletag.json"
        flatpages = f"{settings.BASE_DIR}/baykeshop/conf/data/flatpages.json"
        management.call_command('loaddata', baykebanner, verbosity=0)
        management.call_command('loaddata', baykecategory, verbosity=0)
        management.call_command('loaddata', baykespec, verbosity=0)
        management.call_command('loaddata', baykespecoptions, verbosity=0)
        management.call_command('loaddata', baykegoods, verbosity=0)
        management.call_command('loaddata', baykegoodsbanners, verbosity=0)
        management.call_command('loaddata', baykeproduct, verbosity=0)
        management.call_command('loaddata', baykearticlecategory, verbosity=0)
        management.call_command('loaddata', baykearticle, verbosity=0)
        management.call_command('loaddata', baykearticletag, verbosity=0)
        management.call_command('loaddata', flatpages, verbosity=0)
        self.stdout.write(self.style.SUCCESS("演示数据创建成功！"))