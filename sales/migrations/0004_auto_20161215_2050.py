# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 04:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20161215_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypaldb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 50, 1, 247594, tzinfo=utc), verbose_name='date_user_joined'),
        ),
    ]
