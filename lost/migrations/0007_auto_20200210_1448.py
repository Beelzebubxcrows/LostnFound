# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2020-02-10 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0006_found'),
    ]

    operations = [
        migrations.RenameField(
            model_name='found',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='found',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='found',
            old_name='place',
            new_name='Place',
        ),
        migrations.RenameField(
            model_name='found',
            old_name='thing',
            new_name='Thing',
        ),
    ]
