# Generated by Django 2.1.1 on 2018-09-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20180915_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='u_id',
            field=models.ForeignKey(on_delete=None, to='index.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='a_id',
            field=models.ForeignKey(on_delete=None, to='index.Article'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_uid',
            field=models.ForeignKey(on_delete=None, to='index.User'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='c_id',
            field=models.ForeignKey(on_delete=None, to='index.Comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='from_uid',
            field=models.ForeignKey(on_delete=None, to='index.User'),
        ),
    ]