# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_count', models.IntegerField(verbose_name='\u641c\u7d22\u9875\u6570')),
                ('key_from', models.IntegerField(verbose_name='\u5173\u952e\u8bcd\u6765\u6e90')),
                ('operation_date', models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 35, 40, 286870, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operation_date', models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 35, 40, 287384, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('lentype_all', models.BooleanField(default=True, verbose_name='\u5168\u90e8')),
                ('lentype_0_10', models.BooleanField(default=False, verbose_name='0-10\u5206\u949f')),
                ('lentype_10_30', models.BooleanField(default=False, verbose_name='10-30\u5206\u949f')),
                ('lentype_30_60', models.BooleanField(default=False, verbose_name='30-60\u5206\u949f')),
                ('lentype_60_More', models.BooleanField(default=False, verbose_name='60\u5206\u949f\u4ee5\u4e0a')),
                ('platform', models.ForeignKey(to='videosearch.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key_include', models.CharField(max_length=100, verbose_name='\u5305\u542b\u5173\u952e\u8bcd')),
                ('key_exclude', models.CharField(max_length=100, verbose_name='\u6392\u9664\u5173\u952e\u8bcd')),
                ('platform', models.ForeignKey(to='videosearch.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('create_at', models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 35, 40, 288786, tzinfo=utc), verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('configs', models.TextField()),
                ('video_platforms', models.ManyToManyField(to='videosearch.Platform')),
            ],
        ),
    ]
