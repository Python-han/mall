#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :home.py
@说明    :首页
@时间    :2023/04/28 13:59:42
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''


from django.views.generic import TemplateView, View
from django.http.response import JsonResponse
# Create your views here.
from baykeshop.conf import bayke_settings
from baykeshop.models import BaykeProductCategory, BaykeProductSPU


class HomeTemplateView(TemplateView):
    """ 商城首页 """
    template_name = "baykeshop/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = self.get_queryset()
        return context
    
    def get_queryset(self):
        queryset = BaykeProductCategory.get_cates()
        for cate in queryset:
            cate.spus = BaykeProductSPU.objects.filter(
                cates__in=cate.sub_cates
            ).distinct()[:bayke_settings.HOME_NAV_COUNT]
        return queryset


def has_upload_perm(request, perm_codename=None):
    # 权限判断方法
    perms = [
        request.user.is_authenticated,
        request.user.is_active,
        request.user.is_staff,
        request.user.has_perm(f'baykeshop.{perm_codename}') if perm_codename else True
    ]
    return False if not all(perms) else True
    

class TinymceUploadImg(View):
    """ tinymce 编辑器上传图片 """
    from django.views.decorators.csrf import csrf_exempt
    from django.utils.decorators import method_decorator
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        from baykeshop.models import BaykeUpload
        if not has_upload_perm(request, 'add_baykeupload'):
            return JsonResponse({"message": "无权限！"}, status=400)
        if request.FILES:
            from baykeshop.utils import add_upload_file 
            file_name = add_upload_file(request.FILES['file'])
            if file_name:
                baykeupload = BaykeUpload(img=f"{bayke_settings.FILE_PATH}{file_name}")
                baykeupload.save()
                return JsonResponse({'code': 'ok', 'location':f'{baykeupload.img.url}'})
            else:
                return JsonResponse({'code': 'err', 'message': 'error' })
        else:
            return JsonResponse({'code': 'err', 'message': 'qingxuanze' })