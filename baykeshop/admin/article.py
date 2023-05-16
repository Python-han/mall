from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.sites.admin import SiteAdmin as BaseSiteAdmin
from django.contrib.sites.models import Site

from baykeshop.admin.base import BaseModelAdmin
from baykeshop.models import BaykeArticleCategory, BaykeArticle, BaykeArticleTag

admin.site.unregister(FlatPage)
admin.site.unregister(Site)


@admin.register(BaykeArticleCategory)
class BaykeArticleCategoryAdmin(BaseModelAdmin):
    '''Admin View for BaykeArticleCategory'''

    list_display = ('name', 'icon', 'desc', 'add_date')
    search_fields = ('name', 'desc')


@admin.register(BaykeArticle)
class BaykeArticleAdmin(BaseModelAdmin):
    '''Admin View for BaykeArticleCategory'''

    list_display = ('title', 'category', 'add_date')
    search_fields = ('title', 'desc')
    
    def save_model(self, request, obj, form, change) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(BaykeArticleTag)


@admin.register(FlatPage)
class FlatPageAdmin(BaseFlatPageAdmin):
    from baykeshop.forms import FlatpageForm
    form = FlatpageForm
    

@admin.register(Site)
class SiteAdmin(BaseSiteAdmin):
    pass