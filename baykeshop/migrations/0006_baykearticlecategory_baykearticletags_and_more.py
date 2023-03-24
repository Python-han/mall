# Generated by Django 4.1.7 on 2023-03-24 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baykeshop', '0005_alter_baykeipaddress_browser'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaykeArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='分类名称')),
                ('icon', models.CharField(blank=True, default='', max_length=50, verbose_name='分类icon')),
                ('img_map', models.ImageField(blank=True, help_text='图片尺寸为600 X 480', max_length=200, null=True, upload_to='category/imgMap/%Y', verbose_name='推荐图')),
                ('desc', models.CharField(blank=True, default='', max_length=150, verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='BaykeArticleTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
                'ordering': ['-add_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='baykeshopcategory',
            options={'ordering': ['-add_date'], 'verbose_name': '商品分类', 'verbose_name_plural': '商品分类'},
        ),
        migrations.AlterModelOptions(
            name='baykeshopspu',
            options={'ordering': ['-add_date'], 'verbose_name': '商品管理', 'verbose_name_plural': '商品管理'},
        ),
        migrations.CreateModel(
            name='BaykeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_del', models.BooleanField(default=False, editable=False)),
                ('title', models.CharField(max_length=150, verbose_name='标题')),
                ('desc', models.CharField(blank=True, default='', max_length=200, verbose_name='描述')),
                ('keywords', models.CharField(blank=True, default='', max_length=200, verbose_name='关键字')),
                ('content', models.TextField(verbose_name='内容')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baykeshop.baykearticlecategory', verbose_name='文章分类')),
                ('owner', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='baykeshop.baykearticletags', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-add_date'],
            },
        ),
    ]
