# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0005_auto_20170111_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('1waiting', 'Waiting Payment'), ('2paid', 'Paid'), ('3preparing', 'Preparing'), ('4done', 'Done')], default='1waiting', max_length=50),
        ),
    ]