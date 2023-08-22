from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.validators import UniqueValidator


from baykeshop.common.serializers import ModelSerializer, Serializer
from baykeshop.apps.badmin.models import BaykeVerifyCode
from baykeshop.conf import bayke_settings


class ObtainEmailCodeSerializer(ModelSerializer):
    """ 邮箱发送验证码 """
    email = serializers.EmailField(
        label="邮箱", 
        max_length=150, 
        min_length=3
    )
    code = serializers.ReadOnlyField()

    class Meta:
        model = BaykeVerifyCode
        fields = ('email', 'code')

    def create(self, validated_data):
        data = validated_data
        from django.utils import timezone
        from baykeshop.common.utils import code_random

        code = BaykeVerifyCode.objects.filter(email=data['email']).first()

        if code:
            nd = timezone.now() - bayke_settings.EMAIL_CODE_EXP
            # 判断是否过期，刷新验证码
            if nd > code.pub_date:
                code.code = code_random()
                code.save()
            else:
                # 这里只发送邮件
                code.save_send_main(code.code)
        else:
            code = BaykeVerifyCode.objects.create(email=data['email'])     
        return code
    

class CheckEmailCodeSerializer(Serializer):
    """ 验证码效验 """
    code = serializers.CharField(
        label="验证码", 
        max_length=bayke_settings.CODE_LENGTH, 
        min_length=bayke_settings.CODE_LENGTH
    )
    email = serializers.EmailField(label="邮箱", max_length=150)
    
    def validate(self, attrs):
        email_codes = BaykeVerifyCode.objects.filter(email=attrs['email'], code=attrs['code'])
        if not email_codes.exists():
            raise serializers.ValidationError("该验证码不存在！")
        else:
            code = email_codes.first()
            from django.utils import timezone
            nd = timezone.now() - bayke_settings.EMAIL_CODE_EXP
            # 判断是否过期，刷新验证码
            if nd > code.pub_date:
                raise serializers.ValidationError("该验证码已过期，请重新获取！")
        return attrs
    

class RegisterSerializer(CheckEmailCodeSerializer):
    """ 用户注册 """
    username = serializers.CharField(label="用户名", max_length=32, min_length=2, validators=[
        UniqueValidator(queryset=get_user_model().objects.all(), message="该用户名已存在，请更换！")
    ])
    password = serializers.CharField(label="密码", max_length=36, min_length=8, write_only=True)
    email = serializers.EmailField(label="邮箱", max_length=100, validators=[
        UniqueValidator(queryset=get_user_model().objects.all(), message="该邮箱已存在，请更换！")
    ])
    code = serializers.CharField(
        label="验证码", 
        max_length=bayke_settings.CODE_LENGTH, 
        min_length=bayke_settings.CODE_LENGTH,
        write_only=True
    )
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def validate(self, attrs):
        # 如果不需要邮箱验证只需要注释掉下边这句
        super().validate(attrs)  # 邮箱验证 
        del attrs["code"]
        return attrs
    
    
class UpdateUserSerializer(Serializer):
    """ 修改密码序列化 """
    
    def __init__(self, instance=None, data=empty, user=None, **kwargs):
        self.user = user
        super().__init__(instance, data, **kwargs)
    
    owner = serializers.IntegerField(min_value=1, required=False)
    user_password = serializers.CharField(min_length=3, max_length=64)
    new_password = serializers.CharField(min_length=3, max_length=64)
    confirm_new_password = serializers.CharField(min_length=3, max_length=64)
    
    def validate_user_password(self, user_password):
        if not self.user.check_password(user_password):
            raise serializers.ValidationError("当前密码不正确！")
        return user_password
    
    def validate_new_password(self, new_password):
        if new_password != self.initial_data.get('confirm_new_password'):
            raise serializers.ValidationError("两次密码输入不一致！")
        return new_password