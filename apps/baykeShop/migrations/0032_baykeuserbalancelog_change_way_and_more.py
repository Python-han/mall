# Generated by Django 4.1.5 on 2023-02-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0031_baykeuserbalancelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='baykeuserbalancelog',
            name='change_way',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pay'), (2, 'Admin'), (3, 'Shop')], default=2),
        ),
        migrations.AlterField(
            model_name='baykeuserbalancelog',
            name='change_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Add'), (2, 'Minus')], null=True),
        ),
    ]