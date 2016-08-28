#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.
class CureData(models.Model):
    name = models.CharField('名称', max_length=50)
    cureDuration = models.CharField('时长', max_length=50)
    create_at = models.DateTimeField("日期", default=now())
    note = models.CharField('备注', max_length=200, default='')
    image = models.ImageField('图片', )
    operator = models.CharField('操作者', max_length=50)
    status = models.IntegerField('状态') # 0,进行中; 1,已完成
    #config = models.ForeignKey(Config)

    def __unicode__(self):
        return self.name