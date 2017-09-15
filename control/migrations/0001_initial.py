# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 14:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mailbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2017, 7, 3, 14, 42, 56, 788209))),
                ('classifications', models.CharField(choices=[('Unread', 'Unread'), ('Read', 'Read')], default='Unread', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=15)),
                ('date', models.DateField(default=datetime.datetime(2017, 7, 3, 14, 42, 56, 790595))),
                ('address', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('supporting_doc', models.FileField(upload_to='media/control')),
            ],
        ),
    ]
