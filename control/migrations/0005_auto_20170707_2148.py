# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_auto_20170707_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='supporting_doc',
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 7, 21, 48, 15, 893713)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 7, 21, 48, 15, 897438)),
        ),
    ]
