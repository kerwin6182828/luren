# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 03:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_test_t_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='t_title',
            field=models.CharField(default='kerwin', max_length=30),
        ),
        migrations.AlterField(
            model_name='test',
            name='t_text',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='test',
            name='t_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 11, 5, 26, 683801)),
        ),
    ]
