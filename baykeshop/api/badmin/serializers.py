from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from baykeshop.apps.badmin.models import (
    BaykeDepartment, BaykeFrontedMenus, BaykeRoles,
    BaykeUser, BaykePermissionAction, BaykeDictKey, BaykeDictValue,
    BaykeImage, BaykeSystemExtend, BaykeEmailConf, BaykeSystem
)

from baykeshop.common.serializers import ModelSerializer


class BaykeDepartmentSerializer(ModelSerializer):
    """ 部门 """
    class Meta:
        model = BaykeDepartment
        fields = "__all__"


class BaykeFrontedMenusSerializer(ModelSerializer):
    """ 前端菜单 """
    
    apiList = serializers.SerializerMethodField()
    
    class Meta:
        model = BaykeFrontedMenus
        fields = "__all__"
    
    def get_apiList(self, obj):
        actions = obj.baykepermissionaction_set.values('id', 'permission__id', 'apiname')
        return [{'id':perm['id'], 'code': perm['permission__id'], 'url': perm['apiname']} for perm in actions]
        
    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        apiList = self.context['request'].data.get('apiList', [])
        if apiList:
            for perm in apiList:
                if perm.get('code'):
                    obj, created = instance.baykepermissionaction_set.update_or_create(
                        permission__id=perm.get('code'),
                        defaults = {
                            "permission": Permission.objects.get(id=perm.get('code')),
                            "apiname": perm.get('url', '')
                        }
                    )
                    instance = obj.menus
        return instance
        

class UserSerializer(ModelSerializer):
    """ 用户 """
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
        
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "is_active", "is_staff", "is_superuser", "date_joined")


class BaykeUserSerializer(ModelSerializer):
    """ 获取当前登录用户信息序列化 """
    menus = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    perms = serializers.SerializerMethodField()
    owner = UserSerializer(many=False)
    
    class Meta:
        model = BaykeUser
        fields = "__all__"
    
    def get_roles(self, obj):
        roles = obj.owner.groups.values_list('baykeroles__codename', flat=True)
        return list(roles)
    
    def get_menus(self, obj):
        """ 返回当前用户的权限菜单 """
        roles = obj.owner.groups.values_list("baykeroles__id", flat=True)
        menus_queryset = BaykeFrontedMenus.objects.filter(baykeroles__id__in=list(roles))
        try:
            if self.context['request'].user.is_superuser:
                menus_queryset = BaykeFrontedMenus.objects.all()
        except KeyError:
            pass
        return BaykeFrontedMenusSerializer(menus_queryset, many=True).data
    
    def get_perms(self, obj):
        return obj.owner.get_all_permissions()
        

class UserCreateSerializer(ModelSerializer):
    """ 创建用户 """
    password1 = serializers.CharField(write_only=True)
    group_ids = serializers.ListField(required=True, write_only=True)
    dept = serializers.IntegerField(required=True, write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "password1", "dept", "group_ids")
    
    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password1'])
        super().validate(attrs)
        del attrs['password1']
        return attrs

    def validate_password(self, password):
        if password != self.context['request'].data['password1']:
            raise serializers.ValidationError("两次密码输入不一致")
        return password
    
    def create(self, validated_data):
        group_ids = validated_data.pop('group_ids')
        dept = validated_data.pop('dept')
        insatnce = super().create(validated_data)
        insatnce.groups.set(group_ids)
        baykeuser = insatnce.baykeuser
        baykeuser.dept = BaykeDepartment.objects.get(id=dept)
        baykeuser.save()
        return insatnce
        

class BaykeUserModelSerializer(ModelSerializer):
    """ 用户增删改查 """
    owner = UserSerializer(many=False, read_only=True)
    groupName = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    group_ids = serializers.ListField(required=False, write_only=True)
    
    class Meta:
        model = BaykeUser
        fields = "__all__"
    
    def get_groupName(self, obj):
        roles = obj.owner.groups.values_list('name', flat=True)
        return ' / '.join(list(roles))
    
    def get_group(self, obj):
        roles = obj.owner.groups.values_list('id', flat=True)
        return list(roles)
    
    def update(self, instance, validated_data):
        # 修改的时候传递角色id进行角色关系绑定
        instance.owner.groups.set(validated_data.get('group_ids', []))
        return super().update(instance, validated_data)
    

class GroupModelSerializer(ModelSerializer):
    """ 关联角色的权限组 """
    class Meta:
        model = Group
        fields = "__all__"


class BaykeRolesSerializer(ModelSerializer):
    """ 角色增删改查 """
    name = serializers.CharField(write_only=True, label="角色名")
    group = GroupModelSerializer(many=False, read_only=True)
    
    class Meta:
        model = BaykeRoles
        fields = "__all__"

    def update(self, instance, validated_data):
        try:
            name = validated_data.pop('name')
            group = instance.group
            group.name = name
            group.save()
        except KeyError:
            pass
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        name = validated_data.pop('name')
        group = Group.objects.create(name=name)
        validated_data['group'] = group
        return super().create(validated_data)
    

class BaykePermissionActionSerializer(ModelSerializer):
    """ 菜单权限操作表 """
    class Meta:
        model = BaykePermissionAction
        fields = "__all__"
        

class PermissionSerializer(ModelSerializer):
    """ django自带权限序列化 """
    class Meta:
        model = Permission
        fields = ("id", "name", "codename", "content_type")
        

class BaykeDictKeySerializer(ModelSerializer):
    """ 字典键 """
    class Meta:
        model = BaykeDictKey
        fields = "__all__"


class BaykeDictValueSerializer(ModelSerializer):
    """ 字典值 """
    class Meta:
        model = BaykeDictValue
        fields = "__all__"
        

class BaykeImageSerializer(ModelSerializer):
    """ 图片管理 """
    class Meta:
        model = BaykeImage
        fields = "__all__"


class BaykeSystemSerializer(ModelSerializer):
    """ 站点配置 """
    class Meta:
        model = BaykeSystem
        fields = "__all__"
        
        
class BaykeEmailConfSerializer(ModelSerializer):
    """ 邮箱配置 """
    class Meta:
        model = BaykeEmailConf
        fields = "__all__"
        

class BaykeSystemExtendSerializer(ModelSerializer):
    """ 系统扩展配置 """
    class Meta:
        model = BaykeSystemExtend
        fields = "__all__"