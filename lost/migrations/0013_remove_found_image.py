# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2020-02-15 18:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0012_found_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found',
            name='image',
        ),
    ]
