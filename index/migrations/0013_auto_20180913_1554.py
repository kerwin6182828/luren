# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_remove_test_t_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='r_type_id',
            field=models.IntegerField(null=True),
        ),
    ]
