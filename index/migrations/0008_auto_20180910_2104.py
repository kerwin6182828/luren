# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='a_page_views',
            field=models.IntegerField(null='True'),
        ),
        migrations.AlterField(
            model_name='article',
            name='a_time',
            field=models.DateTimeField(null='True'),
        ),
    ]
