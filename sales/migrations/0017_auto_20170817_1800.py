# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-18 01:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0016_auto_20170520_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 1, 0, 36, 248409, tzinfo=utc), verbose_name='clients_first_purchase'),
        ),
        migrations.AlterField(
            model_name='paypaldb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 1, 0, 36, 249240, tzinfo=utc), verbose_name='date_of_purchase'),
        ),
        migrations.AlterField(
            model_name='paypaltestdb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 1, 0, 36, 249946, tzinfo=utc), verbose_name='date_of_purchase'),
        ),
    ]
