#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.
class Platform(models.Model):
    site = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "{}".format(self.name)

class GeneralConfig(models.Model):
    page_count = models.IntegerField('搜索页数')
    key_from = models.IntegerField('关键词来源')
    operation_date = models.DateTimeField('更新时间',default=now())

    def __unicode__(self):
        return '搜索页数:{} 关键词来源:{}'.format(self.page_count, self.key_from)

class PlatformConfig(models.Model):
    # 0: 全部， 1：0-10分钟，2：10-30分钟，3：30-60分钟，4：60分钟以上
    platform = models.ForeignKey(Platform)
    lentype_all = models.BooleanField('全部', default=True)
    lentype_0_10 = models.BooleanField('0-10分钟')
    lentype_10_30 = models.BooleanField('10-30分钟')
    lentype_30_60 = models.BooleanField('30-60分钟')
    lentype_60_More = models.BooleanField('60分钟以上')
    operation_date = models.DateTimeField('更新时间',default=now())

    def __unicode__(self):
        return self.platform.name

class PlatformKeys(models.Model):
    platform = models.ForeignKey(Platform)
    key_include = models.CharField('包含关键词',max_length=100)
    key_exclude = models.CharField('排除关键词', max_length=100)


class Task(models.Model):
    name = models.CharField('名称', max_length=50)
    create_at = models.DateTimeField("创建日期", default=now())
    video_platforms =models.ManyToManyField(Platform)
    configs = models.TextField()
    #config = models.ForeignKey(Config)

    def __unicode__(self):
        return self.name

