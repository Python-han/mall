# Generated by Django 4.2.3 on 2023-08-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badmin', '0003_baykesystem_extend_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykesystem',
            name='logo_url',
            field=models.URLField(blank=True, default='', verbose_name='logo地址'),
        ),
    ]