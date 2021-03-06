# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170703_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='animation',
            field=models.CharField(choices=[('bounceInRight', 'bounceInRight'), ('bounceInLeft', 'bounceInLeft'), ('bounceInUp', 'bounceInUp'), ('bounceInDown', 'bounceInDown')], default='bounceInLeft', max_length=50),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('App', 'App'), ('Others', 'Others'), ('Design', 'Design'), ('Web', 'Web')], default='App', max_length=200),
        ),
    ]
