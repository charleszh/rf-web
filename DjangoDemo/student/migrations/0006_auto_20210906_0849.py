# Generated by Django 2.2 on 2021-09-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210906_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], default=0, verbose_name='审核状态'),
        ),
    ]
