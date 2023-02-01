# Generated by Django 4.1.5 on 2023-02-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0004_remove_baykeshopspec_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baykeshopspec',
            options={'verbose_name': '商品规格', 'verbose_name_plural': '商品规格'},
        ),
        migrations.AlterModelOptions(
            name='baykeshopspecoption',
            options={'verbose_name': '规格值', 'verbose_name_plural': '规格值'},
        ),
        migrations.AlterField(
            model_name='baykeshopspec',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='baykeshopspecoption',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='规格值'),
        ),
    ]
