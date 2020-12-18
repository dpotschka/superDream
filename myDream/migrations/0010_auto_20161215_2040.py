# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 04:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myDream', '0009_auto_20161215_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendinguser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 40, 42, 131198, tzinfo=utc), verbose_name='date_pendingUser_joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 40, 42, 118784, tzinfo=utc), verbose_name='date_user_joined'),
        ),
    ]
