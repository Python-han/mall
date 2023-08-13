# Generated by Django 4.2.3 on 2023-08-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badmin', '0002_alter_baykefrontedmenus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='baykepermissionaction',
            name='request_method',
            field=models.CharField(blank=True, choices=[('GET', '查看'), ('POST', '新增'), ('PUT', '修改'), ('PATCH', '局部修改'), ('DELETE', '删除')], default='GET', max_length=10),
        ),
    ]
