# Generated by Django 2.2 on 2021-09-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210906_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (2, '拒绝'), (1, '通过')], default=0, verbose_name='审核状态'),
        ),
    ]