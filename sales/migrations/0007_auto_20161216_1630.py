# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 00:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import jsonfield.fields
import sales.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20161215_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypaldb',
            name='txn_info',
            field=jsonfield.fields.JSONField(default=sales.models.txn_default, verbose_name='transaction_info'),
        ),
        migrations.AlterField(
            model_name='paypaldb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 0, 30, 48, 492629, tzinfo=utc), verbose_name='date_user_joined'),
        ),
    ]
