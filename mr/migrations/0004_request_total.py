# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0003_auto_20170110_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
