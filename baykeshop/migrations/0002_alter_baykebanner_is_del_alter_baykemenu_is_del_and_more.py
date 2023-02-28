# Generated by Django 4.1.7 on 2023-02-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baykeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baykebanner',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykemenu',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykepermission',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopaddress',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopcategory',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopingcart',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshoporderinfo',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopordersku',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshoporderskucomment',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopsku',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopspec',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopspecoption',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeshopspu',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykespucarousel',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeuserbalancelog',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='baykeuserinfo',
            name='is_del',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]