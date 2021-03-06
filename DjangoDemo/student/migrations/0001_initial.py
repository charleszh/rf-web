# Generated by Django 2.2.3 on 2021-08-16 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('sex', models.IntegerField(choices=[(2, '女'), (1, '男'), (0, '未知')], verbose_name='性别')),
                ('profession', models.CharField(max_length=128, verbose_name='职业')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('qq', models.CharField(max_length=128, verbose_name='QQ')),
                ('phone', models.CharField(max_length=128, verbose_name='电话')),
                ('homephone', models.CharField(max_length=128, null=True, verbose_name='家庭电话')),
                ('status', models.IntegerField(choices=[(2, '拒绝'), (1, '通过'), (0, '申请')], default=0, verbose_name='审核状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '学员信息',
                'verbose_name_plural': '学员信息',
            },
        ),
    ]
