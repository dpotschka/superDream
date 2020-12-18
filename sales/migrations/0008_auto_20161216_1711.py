# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 01:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import sales.jsonfield.fields
import sales.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20161216_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypaldb',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 1, 11, 32, 135351, tzinfo=utc), verbose_name='date_user_joined'),
        ),
        migrations.AlterField(
            model_name='paypaldb',
            name='txn_info',
            field=sales.jsonfield.fields.JSONField(default=sales.models.txn_default, verbose_name='transaction_info'),
        ),
    ]
