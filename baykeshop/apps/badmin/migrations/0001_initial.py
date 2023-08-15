# Generated by Django 4.2.4 on 2023-08-14 10:46

import baykeshop.common.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('mark', models.CharField(blank=True, default='', max_length=150, verbose_name='备注')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='启用状态')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='badmin.baykedepartment', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ['-sort', '-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeDictKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('code', models.SlugField(unique=True, verbose_name='字典名称')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('sort', models.PositiveIntegerField(default=1, verbose_name='排序')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='badmin.baykedictkey', verbose_name='父级')),
            ],
            options={
                'verbose_name': 'ByakeDictKey',
                'verbose_name_plural': 'ByakeDictKeys',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykeEmailConf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('email_host', models.CharField(default='smtp.qq.com', max_length=50, verbose_name='邮箱发送后端')),
                ('email_host_user', models.EmailField(help_text='用于发送邮件的邮箱地址', max_length=150, verbose_name='发送邮箱号')),
                ('email_host_password', models.CharField(help_text='自己的邮箱密码，或授权码，一般现在的邮箱都需要授权码', max_length=80, verbose_name='邮箱登录密码或授权码')),
                ('email_port', models.PositiveSmallIntegerField(default=465, help_text='QQ邮箱一般为465', verbose_name='邮箱服务器端口号')),
                ('email_use_ssl', models.BooleanField(default=True, verbose_name='是否为隐式安全连接')),
                ('default_from_email', models.EmailField(blank=True, default='', max_length=150, verbose_name='发送邮件默认邮箱')),
                ('status', models.BooleanField(default=True, verbose_name='开启状态')),
            ],
            options={
                'verbose_name': 'BaykeEmailConf',
                'verbose_name_plural': 'BaykeEmailConfs',
            },
        ),
        migrations.CreateModel(
            name='BaykeFrontedMenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='名称')),
                ('path', models.CharField(blank=True, default='', max_length=100, verbose_name='path')),
                ('component', models.CharField(blank=True, max_length=50, null=True, verbose_name='组件')),
                ('meta', models.JSONField(blank=True, null=True, verbose_name='meta')),
                ('redirect', models.CharField(blank=True, default='', help_text='格式应为`/home`', max_length=50, verbose_name='跳转地址')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='badmin.baykefrontedmenus')),
            ],
            options={
                'verbose_name': 'BaykeFrontedMenus',
                'verbose_name_plural': 'BaykeFrontedMenus',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('img', models.ImageField(max_length=200, upload_to='upload/', verbose_name='图片')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
            ],
            options={
                'verbose_name': 'BaykeImage',
                'verbose_name_plural': 'BaykeImages',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykeSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('site_title', models.CharField(default='baykeshop商城系统', max_length=50, verbose_name='站点名称')),
                ('logo_url', models.URLField(blank=True, default='', verbose_name='logo地址')),
                ('extend_json', models.JSONField(blank=True, default=dict, null=True, verbose_name='扩展配置')),
                ('copyright', models.CharField(blank=True, default='baykeshop版权所有', max_length=150, verbose_name='版权信息')),
            ],
            options={
                'verbose_name': 'BaykeSystem',
                'verbose_name_plural': 'BaykeSystems',
            },
        ),
        migrations.CreateModel(
            name='BaykeSystemExtend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('key', models.SlugField(max_length=150, verbose_name='key')),
                ('value', models.CharField(blank=True, default='', max_length=200, verbose_name='字符串值')),
                ('title', models.CharField(max_length=80, verbose_name='配置标题')),
            ],
            options={
                'verbose_name': 'BaykeSystemExtend',
                'verbose_name_plural': 'BaykeSystemExtends',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, validators=[baykeshop.common.validators.validate_phone], verbose_name='手机号')),
                ('user_type', models.CharField(choices=[('FRONTED', '前台用户'), ('SYSTEM', '后台用户')], default='SYSTEM', max_length=50, verbose_name='用户类型')),
                ('sex', models.PositiveSmallIntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='性别')),
                ('about', models.CharField(blank=True, default='我喜欢baykeshop这个程序！', max_length=150, verbose_name='简介')),
                ('avatar', models.CharField(blank=True, default='/media/avatar.png', max_length=150, verbose_name='头像地址')),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='badmin.baykedepartment', verbose_name='归属部门')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'BaykeUser',
                'verbose_name_plural': 'BaykeUsers',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeSiteMenus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='图标')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='badmin.baykesitemenus')),
                ('permission', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': 'SiteMenus',
                'verbose_name_plural': 'SiteMenus',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('codename', models.CharField(max_length=50, unique=True, verbose_name='角色标识')),
                ('perm_range', models.IntegerField(choices=[(1, '全部可见'), (2, '本人可见'), (3, '所在部门可见'), (4, '所在部门及子级可见'), (5, '选择的部门可见'), (6, '自定义数据权限')], default=1, verbose_name='权限范围')),
                ('dashboard_grid', models.JSONField(blank=True, default=list, help_text='当dashboard值为0时才有用！', verbose_name='控制台模块权限')),
                ('dashboard', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='控制台视图')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('remark', models.CharField(blank=True, default='', max_length=150, verbose_name='备注')),
                ('depts', models.ManyToManyField(blank=True, to='badmin.baykedepartment', verbose_name='数据权限-关联部门')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group', verbose_name='权限组')),
                ('menus', models.ManyToManyField(blank=True, to='badmin.baykefrontedmenus', verbose_name='菜单')),
            ],
            options={
                'verbose_name': 'BaykeRoles',
                'verbose_name_plural': 'BaykeRoless',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykePermissionAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('apiname', models.CharField(blank=True, default='', help_text='url的name别名，用来反解url', max_length=50, verbose_name='api接口name')),
                ('request_method', models.CharField(blank=True, choices=[('GET', '查看'), ('POST', '新增'), ('PUT', '修改'), ('PATCH', '局部修改'), ('DELETE', '删除')], default='GET', max_length=10)),
                ('mark', models.CharField(blank=True, default='', max_length=150, verbose_name='备注')),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badmin.baykefrontedmenus', verbose_name='菜单')),
                ('permission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.permission', verbose_name='权限')),
            ],
            options={
                'verbose_name': 'BaykePermissionAction',
                'verbose_name_plural': 'BaykePermissionActions',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeDictValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('key', models.CharField(max_length=150, verbose_name='值')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('sort', models.PositiveIntegerField(default=1, verbose_name='排序')),
                ('dic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badmin.baykedictkey', verbose_name='字典key')),
            ],
            options={
                'verbose_name': 'BaykeDictValue',
                'verbose_name_plural': 'BaykeDictValue',
                'ordering': ['-sort'],
            },
        ),
        migrations.AddConstraint(
            model_name='baykedepartment',
            constraint=models.UniqueConstraint(models.F('name'), models.F('parent'), name='dept_name_parent_unique'),
        ),
    ]
