from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from baykeshop.conf import bayke_settings


class HomeTemplateView(TemplateView):
    """ 商城首页 """
    template_name = "baykeshop/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = self.get_queryset()
        return context
    
    def get_queryset(self):
        from baykeshop.models import BaykeProductCategory, BaykeProductSPU
        queryset = BaykeProductCategory.get_cates()
        for cate in queryset:
            cate.spus = BaykeProductSPU.objects.filter(category__in=cate.sub_cates).distinct()[:bayke_settings.HOME_NAV_COUNT]
        return queryset  
