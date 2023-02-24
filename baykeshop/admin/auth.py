from django.contrib import admin
from django.contrib.auth.models import Permission, User, Group
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin,
    GroupAdmin as BaseGroupAdmin
)
from django.core.cache import cache

from baykeshop.models import (
    BaykeUserInfo, BaykeUserBalanceLog, 
    BaykePermission, BaykeMenu
)
from baykeshop.admin.base import BaseModelAdmin
from baykeshop.admin.sites import bayke_site
from baykeshop.admin import inline

# 禁用全局删除
# admin.site.disable_action('delete_selected')

admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(User, site=bayke_site)
class UserAdmin(BaseUserAdmin, BaseModelAdmin):
    inlines = (inline.BaykeUserInfoInline, )

    # 编辑打开之前先缓存旧值，之后保存时读取缓存并比较
    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        if obj is not None:
            user, created = BaykeUserInfo.objects.get_or_create(
                owner=obj,
                defaults={'owner': obj},
            )
            cache.set(f'{obj.username}_balance', obj.baykeuserinfo.balance)
            cache_balance = cache.get(f"{obj.username}_balance")
        return super().get_inline_formsets(request, formsets, inline_instances, obj)

    def save_formset(self, request, form, formset, change):
        cache_balance = cache.get(f"{form.cleaned_data['username']}_balance")
        data = formset.cleaned_data[0]
        balance = data['balance']
        if float(balance) > 0 and float(balance) > float(cache_balance):
            item_balance = float(balance) - float(cache_balance)
            BaykeUserBalanceLog.objects.create(
                owner=data['owner'],
                amount=item_balance,
                change_status=1,
                change_way=2
            )
        if float(balance) < float(cache_balance) and float(balance) != 0:
            item_balance = float(cache_balance) - float(balance)
            BaykeUserBalanceLog.objects.create(
                owner=data['owner'],
                amount=item_balance,
                change_status=2,
                change_way=2
            )
        if float(balance) == 0 and float(balance) < float(cache_balance):
            BaykeUserBalanceLog.objects.create(
                owner=data['owner'],
                amount=float(cache_balance),
                change_status=2,
                change_way=2
            )
        return super().save_formset(request, form, formset, change)


@admin.register(Group, site=bayke_site)
class GroupAdmin(BaseGroupAdmin, BaseModelAdmin):
    pass


@admin.register(Permission, site=bayke_site)
class PermissionAdmin(BaseModelAdmin):
    '''Admin View for BaykePermission'''

    list_display = ('id', 'name',)
    search_fields = ('name', )
    readonly_fields = ('codename', 'content_type')
    # inlines = (BaykePermissionInline, )


@admin.register(BaykePermission, site=bayke_site)
class BaykePermissionAdmin(BaseModelAdmin):
    '''Admin View for BaykePermission'''

    list_display = ('id', 'permission_name')

    @admin.display(description='Name')
    def permission_name(self, obj):
        return f"{obj.permission.name}"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "menus":
            kwargs["queryset"] = BaykeMenu.objects.filter(
                parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(LogEntry, site=bayke_site)
class LogEntryAdmin(BaseModelAdmin):
    '''Admin View for '''

    list_display = (
        'id', 'action_time', 'user', 'content_type',
        'object_id', 'object_repr', 'action_flag', 'change_message'
    )

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

