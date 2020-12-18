# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myDream', '0020_auto_20170107_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendinguser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 22, 55, 11, 860889, tzinfo=utc), verbose_name='date_pendingUser_joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 22, 55, 11, 555829, tzinfo=utc), verbose_name='date_user_joined'),
        ),
    ]
