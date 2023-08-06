from django.contrib import admin

# Register your models here.
from baykeshop.apps.badmin.models import (
    BaykeDepartment, BaykeFrontedMenus, BaykeRoles,
    BaykeUser, BaykePermissionAction,
    BaykeDictKey, BaykeDictValue
)


admin.site.register([
    BaykeDepartment, BaykeFrontedMenus, BaykeRoles,
    BaykeUser, BaykePermissionAction, BaykeDictKey, BaykeDictValue
])