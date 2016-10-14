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


    platform = models.ForeignKey(Platform)
    operation_date = models.DateTimeField('更新时间',default=now())

    lentype_all = models.BooleanField('全部', default=True)
    lentype_0_10 = models.BooleanField('0-10分钟', default=False)
    lentype_10_30 = models.BooleanField('10-30分钟', default=False)
    lentype_30_60 = models.BooleanField('30-60分钟', default=False)
    lentype_60_More = models.BooleanField('60分钟以上', default=False)

    def __unicode__(self):
        return self.platform.name

class PlatformKeys(models.Model):
    platform = models.ForeignKey(Platform)
    key_include = models.CharField('包含关键词',max_length=100)
    key_exclude = models.CharField('排除关键词', max_length=100, null=True)


class Task(models.Model):
    name = models.CharField('名称', max_length=50)
    status = models.CharField('状态', max_length=30)
    progress = models.CharField('进度', max_length=50)
    actions = models.CharField('操作', max_length=50)
    create_at = models.DateTimeField("创建日期", default=now())
    video_platforms = models.CharField('平台', max_length=200, default='')
    configs = models.TextField('配置', default='')
    #config = models.ForeignKey(Config)

    def __unicode__(self):
        return self.name

class Job(models.Model):
    project = models.CharField(verbose_name='Project', max_length=30)
    spider = models.CharField(verbose_name='Spider', max_length=80)
    jobid = models.CharField(verbose_name='JobID', max_length=50)
    start_time = models.DateTimeField(verbose_name='开始日期')
    end_time = models.DateTimeField(verbose_name="结束日期")
    status = models.CharField(verbose_name='状态', max_length=30, default='')
    node_name = models.TextField(verbose_name='机器名', max_length=30, default='')
    log = models.TextField(verbose_name='Log', max_length=120, default='')
    item = models.TextField(verbose_name='Item', max_length=120, default='')
    scrapy_task_id = models.IntegerField(verbose_name='scrapy_task_id', default=0)

    class Meta:
        ordering = ['-start_time']

    def __unicode__(self):
        return self.project + " -> " + self.spider + " -> "+ self.jobid

class NewJob(models.Model):
    project = models.CharField(verbose_name='Project', max_length=30)
    spider = models.CharField(verbose_name='Spider', max_length=80)

    def __unicode__(self):
        return self.project + " -> " + self.spider

class Project(models.Model):
    project = models.CharField(verbose_name='Project', max_length=30)

    def __unicode__(self):
        return self.project

class Spider(models.Model):
    spider = models.CharField(verbose_name='Spider', max_length=80)

    def __unicode__(self):
        return self.spider
