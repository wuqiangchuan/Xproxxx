# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-24 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosts',
            name='ip_addr',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]