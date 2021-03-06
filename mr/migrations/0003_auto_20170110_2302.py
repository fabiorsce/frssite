# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0002_auto_20161206_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting Payment'), ('queue', 'Queue'), ('preparing', 'Preparing'), ('done', 'Done')], default='waiting', max_length=50),
        ),
    ]
