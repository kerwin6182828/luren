# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180910_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='a_page_views',
            field=models.IntegerField(default=0),
        ),
    ]
