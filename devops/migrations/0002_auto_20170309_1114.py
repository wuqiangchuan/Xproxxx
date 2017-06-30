# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-09 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcname', models.CharField(max_length=100)),
                ('bandwidth', models.CharField(max_length=5, verbose_name='\u5e26\u5bbd')),
                ('operator', models.CharField(max_length=30, verbose_name='\u8fd0\u8425\u5546')),
                ('tel_name', models.CharField(max_length=30, verbose_name='\u8054\u7cfb\u4eba')),
                ('tel_phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd')),
                ('comm', models.CharField(max_length=300, verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=6)),
                ('comm', models.CharField(max_length=300, verbose_name='\u7528\u6237\u63cf\u8ff0\u4fe1\u606f')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devops.CmdbHost')),
            ],
        ),
        migrations.AddField(
            model_name='cmdbgroup',
            name='host',
            field=models.ManyToManyField(to='devops.CmdbHost'),
        ),
    ]