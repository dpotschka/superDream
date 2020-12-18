# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 05:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myDream', '0011_auto_20161215_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendinguser',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 5, 3, 33, 854155, tzinfo=utc), verbose_name='date_pendingUser_joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 5, 3, 33, 844839, tzinfo=utc), verbose_name='date_user_joined'),
        ),
    ]
