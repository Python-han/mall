# Generated by Django 4.1.5 on 2023-02-11 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0017_alter_baykeuserinfo_avatar'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='baykeshopaddress',
            name='unique_happy_addr',
        ),
    ]