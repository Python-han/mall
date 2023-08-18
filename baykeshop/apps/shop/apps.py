from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baykeshop.apps.shop'

    def ready(self) -> None:
        from . import signals