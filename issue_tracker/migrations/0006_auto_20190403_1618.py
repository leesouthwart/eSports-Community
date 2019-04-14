# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-03 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_content_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]