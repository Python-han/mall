# Generated by Django 4.1.5 on 2023-02-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0028_alter_baykeuserinfo_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykeuserinfo',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8, verbose_name='余额'),
        ),
    ]