# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-02 01:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='iamge',
            new_name='image',
        ),
    ]