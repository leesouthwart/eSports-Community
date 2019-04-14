# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-03 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0004_auto_20190402_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
            preserve_default=False,
        ),
    ]