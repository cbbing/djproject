# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('videosearch', '0003_auto_20160512_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfig',
            name='operation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 42, 6, 513571, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='platformconfig',
            name='operation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 42, 6, 514065, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 12, 6, 42, 6, 515227, tzinfo=utc), verbose_name='\u521b\u5efa\u65e5\u671f'),
        ),
    ]