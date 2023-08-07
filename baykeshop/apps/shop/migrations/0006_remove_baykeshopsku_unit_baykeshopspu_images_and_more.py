# Generated by Django 4.2.3 on 2023-08-07 02:52

import baykeshop.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_baykeshopbrand_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baykeshopsku',
            name='unit',
        ),
        migrations.AddField(
            model_name='baykeshopspu',
            name='images',
            field=models.JSONField(default=list, validators=[baykeshop.common.validators.validate_count], verbose_name='轮播图'),
        ),
        migrations.AddField(
            model_name='baykeshopspu',
            name='unit',
            field=models.CharField(default=1, max_length=50, verbose_name='单位'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='baykeshopspu',
            name='category',
        ),
        migrations.DeleteModel(
            name='BaykeShopBanner',
        ),
        migrations.DeleteModel(
            name='BaykeShopUnit',
        ),
        migrations.AddField(
            model_name='baykeshopspu',
            name='category',
            field=models.ManyToManyField(blank=True, to='shop.baykeshopcategory', verbose_name='分类'),
        ),
    ]
