# Generated by Django 4.2.3 on 2023-08-06 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_baykeshopbrand_sort_baykeshopbrand_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baykeshopbrand',
            options={'ordering': ['-sort'], 'verbose_name': 'BaykeshopBrand', 'verbose_name_plural': 'BaykeshopBrands'},
        ),
    ]