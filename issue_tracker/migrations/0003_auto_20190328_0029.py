# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-28 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0002_auto_20190325_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('a', 'Backlog'), ('b', 'In Progress'), ('c', 'Completed')], default='Backlog', max_length=20),
        ),
    ]
