# Generated by Django 2.2.3 on 2021-08-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
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
            field=models.IntegerField(choices=[(2, '拒绝'), (0, '申请'), (1, '通过')], default=0, verbose_name='审核状态'),
        ),
    ]