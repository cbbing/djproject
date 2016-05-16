# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_count', models.IntegerField(verbose_name='\u641c\u7d22\u9875\u6570')),
                ('key_from', models.IntegerField(verbose_name='\u5173\u952e\u8bcd\u6765\u6e90')),
                ('operation_date', models.DateTimeField(default=datetime.datetime(2016, 5, 14, 8, 53, 3, 520142, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_date', models.DateTimeField(default=datetime.datetime(2016, 5, 14, 8, 53, 3, 520624, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('lentype_all', models.BooleanField(default=True, verbose_name='\u5168\u90e8')),
                ('lentype_0_10', models.BooleanField(default=False, verbose_name='0-10\u5206\u949f')),
                ('lentype_10_30', models.BooleanField(default=False, verbose_name='10-30\u5206\u949f')),
                ('lentype_30_60', models.BooleanField(default=False, verbose_name='30-60\u5206\u949f')),
                ('lentype_60_More', models.BooleanField(default=False, verbose_name='60\u5206\u949f\u4ee5\u4e0a')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videosearch.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_include', models.CharField(max_length=100, verbose_name='\u5305\u542b\u5173\u952e\u8bcd')),
                ('key_exclude', models.CharField(max_length=100, verbose_name='\u6392\u9664\u5173\u952e\u8bcd')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videosearch.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('status', models.CharField(max_length=30, verbose_name='\u72b6\u6001')),
                ('progress', models.CharField(max_length=50, verbose_name='\u8fdb\u5ea6')),
                ('actions', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c')),
                ('create_at', models.DateTimeField(default=datetime.datetime(2016, 5, 14, 8, 53, 3, 521898, tzinfo=utc), verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('configs', models.ManyToManyField(to='videosearch.PlatformConfig')),
                ('video_platforms', models.ManyToManyField(to='videosearch.Platform')),
            ],
        ),
    ]
