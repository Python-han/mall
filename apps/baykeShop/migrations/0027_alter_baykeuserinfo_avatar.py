# Generated by Django 4.1.5 on 2023-02-15 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeShop', '0026_alter_baykeuserinfo_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykeuserinfo',
            name='avatar',
            field=models.ImageField(blank=True, max_length=200, upload_to='avatar/', verbose_name='头像'),
        ),
    ]
