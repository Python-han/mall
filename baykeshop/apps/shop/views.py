#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :views.py
@说明    :pc端商城页面视图
@时间    :2023/08/20 00:04:02
@作者    :幸福关中&轻编程
@版本    :1.0
@微信    :baywanyun
'''

from django.shortcuts import redirect
from django.db.models import F
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from baykeshop.common import mixins
from baykeshop.common.renderers import TemplateHTMLRenderer, JSONRenderer
from baykeshop.common.permission import BaykePermissionOrReadOnly, IsOwnerAuthenticated
from baykeshop.api.auth.views import BaykeUserRegisterAPIView
from baykeshop.api.badmin.viewsets import BaykeUserRetrieveAPIView, BaykeUserViewset
from baykeshop.api.badmin.serializers import UserSerializer
from baykeshop.api.shop.serializers import (
    BaykeShopSKUSerializer, BaykeShopSPUSerializer, BaykeShopOrderSerializer
)
from baykeshop.api.shop.viewsets import (
    BaykeShopCategoryViewSet, BaykeShopSPUViewSet, BaykeShopCartViewSet, 
    BaykeShopOrderViewSet, BaykeAddressViewSet
)
from baykeshop.apps.shop.models import (
    BaykeShopSPU, BaykeShopSKU, BaykeShopSpecValue, BaykeShopOrderSKU, BaykeUserBalanceLog,
    BaykeShopOrder
)
from baykeshop.apps.comment.models import BaykeShopComment
from baykeshop.apps.badmin.models import BaykeUser
from baykeshop.common import utils
from baykeshop.apps.shop.form import LoginForm


class BaykeShopCategoryView(BaykeShopCategoryViewSet):
    """ 实例化一个分类接口
    重写权限属性 取消分页
    permission_classes, get请求不受权限控制
    """
    permission_classes = [BaykePermissionOrReadOnly]
    pagination_class = None


class HomeTemplateView(TemplateView):
    """ 商城首页 """
    template_name = "baykeshop/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cates'] = self.get_spus(self.request)
        return context
    
    def get_spus(self, request):
        cates = utils.generate_tree(BaykeShopCategoryView.as_view({"get": "list"})(request).data, None) 
        for cate in cates:
            subcate_ids = [subcate['id'] for subcate in cate['children']]
            cate['spus'] = BaykeShopSPU.objects.filter(category__id__in=subcate_ids).distinct()
        return cates


class BaykeShopSPUOrderingFilter(OrderingFilter):
    """ 商品排序过滤器 """
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            qs = []
            for q in queryset.order_by(*ordering):
                if q not in qs:
                    qs.append(q)
            return qs
        return queryset


class BaykeShopSPUView(BaykeShopSPUViewSet):
    """ 商品 """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [BaykePermissionOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter, BaykeShopSPUOrderingFilter)
    ordering_fields = ("baykeshopsku__price", "baykeshopsku__sales", "add_date")
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/list.html"
        return response
    
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.template_name = "baykeshop/goods/detail.html"
        return response


class LoginView(SuccessMessageMixin, BaseLoginView):
    """ 登录 """
    next_page = "/"
    form_class = LoginForm
    redirect_field_name = 'redirect_to'
    template_name = "baykeshop/login.html"
    success_message = "%(username)s 登录成功！"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=cleaned_data['username'],
        )
        

class LogoutView(BaseLogoutView):
    """ 登出 """
    template_name = 'baykeshop/logout.html'
    

class BaykeRegisterView(BaykeUserRegisterAPIView):
    """ 用户注册 """
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response({}, template_name="baykeshop/register.html")
    

class BaykeShopCartView(BaykeShopCartViewSet):
    """ 购物车 """
    renderer_classes = [TemplateHTMLRenderer]
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, '未登录，请登录后访问！')
            return redirect('shop:login')
        return super().dispatch(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/cart.html"
        if response.data:
            for res in response.data:
                res['skuData'] = BaykeShopSKUSerializer(
                    BaykeShopSKU.objects.get(id=int(res['sku'])), many=False
                ).data
                
                res['skuData']['spu'] = BaykeShopSPUSerializer(
                    BaykeShopSPU.objects.get(id=res['skuData']['spu']), many=False
                ).data
                
                res['skuData']['options'] = list(BaykeShopSpecValue.objects.filter(
                    id__in=res['skuData']['spec_values']).values("id", "spec__name", "value"))
        return response


class BaykeShopOrderViewSerializer(BaykeShopOrderSerializer):
    """ 订单相关操作序列化 """
    class BaykeShopOrderSKUSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaykeShopOrderSKU
            exclude = ('order',)
    
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    baykeshopordersku_set = BaykeShopOrderSKUSerializer(many=True)
    payurl = serializers.SerializerMethodField()
    
    def create(self, validated_data):
        """ 创建订单 """
        baykeshopordersku_set = validated_data.pop('baykeshopordersku_set')
        # 创建订单时计算总价，这里只是粗略计算，未计算运费
        total_price = sum([ 
            order_sku.get('sku').price * int(order_sku.get('count', 1))  
            for order_sku in baykeshopordersku_set
        ])
        validated_data['total_price'] = total_price
        instance = super().create(validated_data)
        for order_sku in baykeshopordersku_set:
            BaykeShopOrderSKU.objects.create(order=instance, **order_sku)
        messages.add_message(self.context['request'], messages.SUCCESS, "订单创建成功，请尽快支付！")
        return instance
    
    def update(self, instance, validated_data):
        """ 立即支付，订单确认，返回支付地址走patch请求 """
        if instance.status != 1:
            raise serializers.ValidationError("该订单已支付或已失效，请重新下单支付！")
        if (not validated_data.get('name')) or (not validated_data.get('phone')) or (not validated_data.get('address')):
            raise serializers.ValidationError("收货信息不完整，请检查！")
        if validated_data.get('paymethod') == 2:
            raise serializers.ValidationError("暂不支持该支付方式！")
        return super().update(instance, validated_data)
    
    def get_payurl(self, obj):
        payurl = ""
        paymethod = obj.paymethod
        # 支付宝支付
        if paymethod == 1:
            request = self.context['request']
            from django.urls import reverse
            from baykeshop.pay.alipay.trade_page_pay import trade_page_pay
            return_url = f"{request.scheme}://{request.get_host()}{reverse('shop:alipay')}"
            notify_url = f"{request.scheme}://{request.get_host()}{reverse('shop:alipay')}"
            response = trade_page_pay(
                out_trade_no=obj.order_sn, total_amount=obj.total_price.to_eng_string(),
                subject=obj.order_sn, body=f"alipay{obj.order_sn}", 
                return_url=return_url, notify_url=notify_url
            )
            payurl = response
        return payurl


class BaykeShopOrderView(mixins.CreateModelMixin, BaykeShopOrderViewSet):
    """ 订单 """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    permission_classes = [IsOwnerAuthenticated]
    serializer_class = BaykeShopOrderViewSerializer
    
    def get_queryset(self):
        # 仅允许操作自己的订单
        return super().get_queryset().filter(owner=self.request.user)
    
    @action(methods=['GET'], detail=True)
    def orderconfirm(self, request, *args, **kwargs):
        # 订单确认发起支付
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = Response(serializer.data)
        response.template_name = "baykeshop/order_confirm.html"
        return response
    
    def list(self, request, *args, **kwargs):
        # 个人中心订单列表
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/orders.html"
        return response
    
    @action(methods=['GET', 'POST'], detail=True)
    def confirmok(self, request, *args, **kwargs):
        # 订单详情get及确认收货接口post
        instance = self.get_object()
        # 确认收货
        if request.method == 'POST':
            instance.status = 4
            instance.save()
            messages.add_message(request, messages.SUCCESS, "确认成功！")
        serializer = self.get_serializer(instance)
        return Response(serializer.data, template_name="baykeshop/order-detail.html")
    
    @action(methods=['GET', 'POST'], detail=True)
    def ordercomment(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if request.method == 'POST':
            from django.contrib.contenttypes.models import ContentType
            from baykeshop.api.comment.serializers import BaykeShopCommentSerializer
            content_type = ContentType.objects.get_for_model(BaykeShopSKU)
            data = request.data
            data['content_type'] = content_type.id
            data['owner'] = request.user.id
            comment_serializer = BaykeShopCommentSerializer(data=data)
            comment_serializer.is_valid(raise_exception=True)
            BaykeShopComment.objects.create(**comment_serializer.validated_data)
            order_skus = BaykeShopOrderSKU.objects.filter(
                sku__id=comment_serializer.validated_data['object_id']
            )
            order_skus.update(is_commented=True)
            # 判断订单商品是否均已评价
            is_commented = all(
                [ordersku.is_commented for ordersku in instance.baykeshopordersku_set.all()]
            )
            # 修改订单状态为已完成
            if is_commented:
                instance.status = 5
                instance.save()
            messages.add_message(request, messages.SUCCESS, "评价成功！")   
        return Response(serializer.data, template_name="baykeshop/comment.html")
    

class BaykeUserSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    email = serializers.EmailField(write_only=True, required=False)
    
    class Meta:
        model = BaykeUser
        fields = "__all__"
        
    def update(self, instance, validated_data):
        # 处理修改邮箱
        if validated_data.get('email'):
            user = instance.owner
            user.email = validated_data.get('email')
            user.save()
        return super().update(instance, validated_data)

class BaykeUserView(BaykeUserRetrieveAPIView):
    """ 用户中心 """
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsOwnerAuthenticated]
    serializer_class = BaykeUserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = Response(serializer.data)
        response.template_name = "baykeshop/menmber.html"
        return response


class BaykeUserUpdateView(BaykeUserViewset):
    """ 修改用户信息 """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    permission_classes = [IsOwnerAuthenticated]
    serializer_class = BaykeUserSerializer
    
    @action(methods=['GET'], detail=False)
    def balance(self, request, *args, **kwargs):
        add_sum_amount = BaykeUserBalanceLog.add_sum_amount(request.user)
        minus_sum_amount = BaykeUserBalanceLog.minus_sum_amount(request.user)
        balance_queryset = BaykeUserBalanceLog.balance_queryset(request.user)
        context = {
            'add_sum_amount': add_sum_amount,
            'minus_sum_amount': minus_sum_amount,
            'balance_queryset': list(balance_queryset.values())
        }
        return Response(context, template_name="baykeshop/balance.html")
    

class BaykeAddressView(BaykeAddressViewSet):
    """ 用户地址 """
    renderer_classes = [TemplateHTMLRenderer, ]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = "baykeshop/address.html"
        return response
    

class AliPayCallBackView(APIView, mixins.AlipayCallBackVerifySignMixin):
    """ 支付宝支付成功回调 """
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    
    def get(self, request, *args, **kwargs):
        # 验签通过处理逻辑
        data = request.query_params.dict()
        if self.has_verify_sign(data):
            from django.utils import timezone
            order_queryset = BaykeShopOrder.objects.filter(order_sn=data['out_trade_no'])
            instance = order_queryset.first()
            order_queryset.update(pay_time=timezone.now(), total_price=data['total_amount'], paymethod=1, status=2)
            serializer = BaykeShopOrderSerializer(instance, many=False)
            return Response(serializer.data, template_name="baykeshop/payok.html")
    
    def post(self, request, *args, **kwargs):
        data = request.data.dict()
        if self.has_verify_sign(data):
            from django.utils import timezone
            order_queryset = BaykeShopOrder.objects.filter(order_sn=data['out_trade_no'])
            order_queryset.update(pay_time=timezone.now(), total_price=data['total_amount'],paymethod=1,status=2)
            return Response("success")
    

class BalanceRechargeAliPayCallBackView(AliPayCallBackView):
    """ 余额充值回调 """
    
    def get(self, request, *args, **kwargs):
        data = request.query_params.dict()
        from django.http.response import HttpResponseRedirect
        if self.has_verify_sign(data):
            baykeusers = BaykeUser.objects.filter(owner=request.user)
            baykeusers.update(balance=F('balance') + float(data['total_amount']))
            serializer = BaykeUserSerializer(baykeusers.first(), many=False)
            messages.add_message(request, messages.SUCCESS, "充值成功！")
            return HttpResponseRedirect('/menmber/')
            # return Response(serializer.data, template_name="baykeshop/menmber.html")
    
    def post(self, request, *args, **kwargs):
        data = request.data.dict()
        if self.has_verify_sign(data):
            BaykeUser.objects.filter(owner=self.get_user(request)).update(
                balance=F('balance') + float(data['total_amount'])
            )
        return Response('success')