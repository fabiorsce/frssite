# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
