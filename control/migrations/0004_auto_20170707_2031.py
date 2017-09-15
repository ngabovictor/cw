# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 20:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20170704_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mailed',
            field=models.CharField(default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='classifications',
            field=models.CharField(choices=[('Unread', 'Unread'), ('Read', 'Read')], default='Unread', max_length=200),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 7, 20, 31, 34, 935576)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 7, 20, 31, 34, 938236)),
        ),
    ]
