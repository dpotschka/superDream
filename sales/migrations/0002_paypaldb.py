# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 02:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 12, 16, 2, 15, 48, 141906, tzinfo=utc), verbose_name='date_user_joined')),
            ],
        ),
    ]
