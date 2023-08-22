# Generated by Django 4.2.4 on 2023-08-22 13:32

import baykeshop.common.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeShopBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('img', models.ImageField(upload_to='banner')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='描述')),
                ('target', models.URLField(blank=True, null=True, verbose_name='跳转链接')),
                ('sort', models.PositiveSmallIntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'BaykeShopBanner',
                'verbose_name_plural': 'BaykeShopBanners',
                'ordering': ['sort', '-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeshopBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='品牌名称')),
                ('logo', models.ImageField(blank=True, max_length=200, null=True, upload_to='shop/brand/', verbose_name='品牌logo')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': 'BaykeshopBrand',
                'verbose_name_plural': 'BaykeshopBrands',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('icon', models.ImageField(blank=True, max_length=200, null=True, upload_to='shop/category', verbose_name='分类图标')),
                ('sort', models.PositiveSmallIntegerField(default=1, verbose_name='排序')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.baykeshopcategory')),
            ],
            options={
                'verbose_name': 'BaykeShopCategory',
                'verbose_name_plural': 'BaykeShopCategorys',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '待付款'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成'), (6, '已关闭'), (7, '退款中')], default=1, verbose_name='订单状态')),
                ('paymethod', models.PositiveSmallIntegerField(blank=True, choices=[(None, '(Unknown)'), (1, '支付宝支付'), (2, '微信支付'), (3, '余额支付')], null=True, verbose_name='支付方式')),
                ('order_sn', models.CharField(blank=True, max_length=100, verbose_name='订单号')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价')),
                ('mark', models.CharField(blank=True, default='', max_length=150, verbose_name='订单备注')),
                ('name', models.CharField(blank=True, default='', max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(blank=True, default='', max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('address', models.CharField(blank=True, default='', max_length=200, verbose_name='收货地址')),
                ('pay_time', models.DateTimeField(blank=True, editable=False, help_text='支付时间', null=True, verbose_name='支付时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'BaykeShopOrder',
                'verbose_name_plural': 'BaykeShopOrders',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('sort', models.IntegerField(default=1, verbose_name='排序')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': 'BaykeShopSpec',
                'verbose_name_plural': 'BaykeShopSpecs',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeUserBalanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='金额')),
                ('change_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, '增加'), (2, '支出')], null=True)),
                ('change_way', models.PositiveSmallIntegerField(choices=[(1, '线上充值'), (2, '管理员手动更改'), (3, '余额抵扣商品')], default=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '余额明细',
                'verbose_name_plural': '余额明细',
            },
        ),
        migrations.CreateModel(
            name='BaykeShopSPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=80, verbose_name='标题')),
                ('subtitle', models.CharField(blank=True, default='', max_length=150, verbose_name='副标题')),
                ('keywords', models.CharField(blank=True, default='', max_length=150, verbose_name='商品关键字')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='商品简介')),
                ('content', models.TextField(verbose_name='详情')),
                ('unit', models.CharField(max_length=50, verbose_name='单位')),
                ('images', models.JSONField(blank=True, default=list, validators=[baykeshop.common.validators.validate_count], verbose_name='轮播图')),
                ('skutype', models.PositiveSmallIntegerField(blank=True, choices=[(0, '单规格'), (1, '多规格')], default=0, verbose_name='规格类型')),
                ('freighttype', models.PositiveSmallIntegerField(blank=True, choices=[(0, '固定运费'), (1, '运费模板')], default=0, verbose_name='运费类型')),
                ('expresstype', models.PositiveSmallIntegerField(blank=True, choices=[(0, '快递'), (1, '上门自提')], default=0, verbose_name='运费类型')),
                ('freight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='运费')),
                ('sort', models.IntegerField(default=1, verbose_name='排序')),
                ('status', models.BooleanField(default=True, verbose_name='商品状态(上下架)')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.baykeshopbrand', verbose_name='品牌')),
                ('category', models.ManyToManyField(blank=True, to='shop.baykeshopcategory', verbose_name='分类')),
            ],
            options={
                'verbose_name': 'BaykeShopSPU',
                'verbose_name_plural': 'BaykeShopSPUs',
                'ordering': ['-sort', '-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopSpecValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('value', models.CharField(max_length=50, verbose_name='规格值')),
                ('spec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.baykeshopspec', verbose_name='规格')),
            ],
            options={
                'verbose_name': 'BaykeShopSpecValue',
                'verbose_name_plural': 'BaykeShopSpecValues',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('stock', models.PositiveSmallIntegerField(default=0, verbose_name='库存')),
                ('sales', models.PositiveIntegerField(default=0, verbose_name='销量')),
                ('img', models.CharField(blank=True, default='', max_length=200, verbose_name='主图')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='售价')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='成本价')),
                ('retail_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, verbose_name='零售价')),
                ('item', models.CharField(blank=True, max_length=50, verbose_name='商品编号')),
                ('weight', models.FloatField(blank=True, default=0, verbose_name='重量')),
                ('vol', models.FloatField(blank=True, default=0, verbose_name='体积')),
                ('status', models.BooleanField(default=True, verbose_name='商品状态(上下架)')),
                ('spec_values', models.ManyToManyField(blank=True, to='shop.baykeshopspecvalue', verbose_name='规格')),
                ('spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.baykeshopspu', verbose_name='商品')),
            ],
            options={
                'verbose_name': 'BaykeShopSKU',
                'verbose_name_plural': 'BaykeShopSKUs',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopOrderSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('count', models.PositiveSmallIntegerField(default=1, verbose_name='数量')),
                ('sku_json', models.JSONField(blank=True, default=dict, verbose_name='商品快照')),
                ('is_commented', models.BooleanField(default=False, verbose_name='是否已评价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.baykeshoporder', verbose_name='订单')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.baykeshopsku', verbose_name='商品规格')),
            ],
            options={
                'verbose_name': 'BaykeShopOrderSKU',
                'verbose_name_plural': 'BaykeShopOrderSKUs',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('num', models.PositiveSmallIntegerField(default=1, verbose_name='数量')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.baykeshopsku', verbose_name='规格')),
            ],
            options={
                'verbose_name': 'BaykeShopCart',
                'verbose_name_plural': 'BaykeShopCarts',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, editable=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=50, verbose_name='签收人')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='邮箱')),
                ('province', models.CharField(max_length=150, verbose_name='省')),
                ('city', models.CharField(max_length=150, verbose_name='市')),
                ('county', models.CharField(max_length=150, verbose_name='区/县')),
                ('address', models.CharField(max_length=150, verbose_name='详细地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='设为默认')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
        migrations.AddConstraint(
            model_name='baykeshoporder',
            constraint=models.UniqueConstraint(models.F('owner'), models.F('order_sn'), name='unique_owner_order'),
        ),
        migrations.AddConstraint(
            model_name='baykeshopcart',
            constraint=models.UniqueConstraint(models.F('owner'), models.F('sku'), name='unique_owner_sku'),
        ),
    ]
