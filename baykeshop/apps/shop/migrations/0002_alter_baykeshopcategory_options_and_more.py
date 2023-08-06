# Generated by Django 4.2.3 on 2023-08-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baykeshopcategory',
            options={'ordering': ['-sort'], 'verbose_name': 'BaykeShopCategory', 'verbose_name_plural': 'BaykeShopCategorys'},
        ),
        migrations.AddField(
            model_name='baykeshopcategory',
            name='icon',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='shop/category', verbose_name='分类图标'),
        ),
        migrations.AddField(
            model_name='baykeshopcategory',
            name='sort',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='排序'),
        ),
        migrations.AddField(
            model_name='baykeshopcategory',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]