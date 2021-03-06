# Generated by Django 2.2 on 2021-09-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210906_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (2, '拒绝'), (1, '通过')], default=0, verbose_name='审核状态'),
        ),
    ]
