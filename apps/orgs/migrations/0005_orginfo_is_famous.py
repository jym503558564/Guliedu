# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-28 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0004_auto_20180826_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='orginfo',
            name='is_famous',
            field=models.BooleanField(default=0, verbose_name='是否经典'),
        ),
    ]
