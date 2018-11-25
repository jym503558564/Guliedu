# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-25 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherinfo',
            name='category',
        ),
        migrations.AddField(
            model_name='orginfo',
            name='category',
            field=models.ImageField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=10, upload_to='', verbose_name='机构类型'),
        ),
    ]