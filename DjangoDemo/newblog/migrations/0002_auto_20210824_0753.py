# Generated by Django 2.2.3 on 2021-08-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]