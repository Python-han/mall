# Generated by Django 4.2.3 on 2023-08-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badmin', '0002_baykeemailconf_baykesystem_baykesystemextend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baykesystem',
            name='extend_json',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='扩展配置'),
        ),
    ]
