# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170515_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='limmit_date',
            new_name='limit_date',
        ),
        migrations.RenameField(
            model_name='todoitem',
            old_name='limmit_time',
            new_name='limit_time',
        ),
    ]
