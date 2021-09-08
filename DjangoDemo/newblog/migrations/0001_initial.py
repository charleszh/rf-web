# Generated by Django 2.2 on 2021-09-08 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否为导航')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('author', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否为导航')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('author', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('desc', models.CharField(blank=True, max_length=1024, verbose_name='摘要')),
                ('content', models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文')),
                ('content_html', models.TextField(blank=True, editable=False, verbose_name='正文html代码')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=1, verbose_name='状态')),
                ('is_nav', models.BooleanField(default=False, verbose_name='是否为导航')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('pv', models.PositiveIntegerField(default=1)),
                ('uv', models.PositiveIntegerField(default=1)),
                ('is_md', models.BooleanField(default=False, verbose_name='markdown语法')),
                ('author', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=None, to='newblog.Category', verbose_name='分类')),
                ('tag', models.ManyToManyField(to='newblog.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-id'],
            },
        ),
    ]
