# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-03 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180902_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('girl', '女'), ('boy', '男')], default='girl', max_length=10, verbose_name='用户性别'),
        ),
    ]
