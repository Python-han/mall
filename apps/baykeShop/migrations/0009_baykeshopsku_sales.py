# Generated by Django 4.1.5 on 2023-02-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0008_alter_baykeshopsku_cover_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='baykeshopsku',
            name='sales',
            field=models.PositiveIntegerField(default=0, verbose_name='销量'),
        ),
    ]