# Generated by Django 4.2.3 on 2023-08-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_baykeshopcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baykeshopbrand',
            name='sort',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='排序'),
        ),
        migrations.AddField(
            model_name='baykeshopbrand',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]