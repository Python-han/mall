# Generated by Django 4.1.5 on 2023-02-16 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baykeShop', '0030_alter_baykeuserinfo_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeUserBalanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_del', models.BooleanField(default=False, editable=False, verbose_name='删除')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='金额')),
                ('change_status', models.PositiveSmallIntegerField(choices=[(1, 'Pay'), (2, 'Admin'), (3, 'Shop')], default=2)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '余额明细',
                'verbose_name_plural': '余额明细',
            },
        ),
    ]