# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-09 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0002_auto_20170309_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idc',
            name='bandwidth',
            field=models.CharField(max_length=5, null=True, verbose_name='\u5e26\u5bbd'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='comm',
            field=models.CharField(max_length=300, null=True, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='operator',
            field=models.CharField(max_length=30, null=True, verbose_name='\u8fd0\u8425\u5546'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='tel_name',
            field=models.CharField(max_length=30, null=True, verbose_name='\u8054\u7cfb\u4eba'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='tel_phone',
            field=models.CharField(max_length=20, null=True, verbose_name='\u7535\u8bdd'),
        ),
    ]
