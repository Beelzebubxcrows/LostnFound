# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2020-02-10 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0009_remove_found_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='Description',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='found',
            name='Name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='found',
            name='Place',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='found',
            name='Thing',
            field=models.CharField(max_length=15),
        ),
    ]