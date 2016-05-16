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

    # '10000': {'全部':True, '0-10分钟':False, '10-30分钟':False, ''30-60分钟':False, '60分钟以上':'False'}
    # platform_youku = models.ForeignKey(Platform)
    # lentype_youku = models.CharField('时长类型', max_length=10)
    #
    # platform_tudou = models.ForeignKey(Platform)
    # lentype_tudou = models.CharField('时长类型', max_length=10)
    #
    # platform_iqiyi = models.ForeignKey(Platform)
    # lentype_iqiyi = models.CharField('时长类型', max_length=10)
    #
    # platform_letv = models.ForeignKey(Platform)
    # lentype_letv = models.CharField('时长类型', max_length=10)
    #
    # platform_sohu = models.ForeignKey(Platform)
    # lentype_sohu = models.CharField('时长类型', max_length=10)
    #
    # platform_qq = models.ForeignKey(Platform)
    # lentype_qq = models.CharField('时长类型', max_length=10)
    #
    # platform_sina = models.ForeignKey(Platform)
    # lentype_sina = models.CharField('时长类型', max_length=10)
    #
    # platform_huashu = models.ForeignKey(Platform)
    # lentype_huashu = models.CharField('时长类型', max_length=10)
    #
    # platform_kankan = models.ForeignKey(Platform)
    # lentype_kankan = models.CharField('时长类型', max_length=10)
    #
    # platform_56 = models.ForeignKey(Platform)
    # lentype_56 = models.CharField('时长类型', max_length=10)
    #
    # platform_ku6 = models.ForeignKey(Platform)
    # lentype_ku6 = models.CharField('时长类型', max_length=10)
    #
    # platform_baomihua = models.ForeignKey(Platform)
    # lentype_baomihua = models.CharField('时长类型', max_length=10)
    #
    # platform_cctv = models.ForeignKey(Platform)
    # lentype_cctv = models.CharField('时长类型', max_length=10)
    #
    # platform_163 = models.ForeignKey(Platform)
    # lentype_163 = models.CharField('时长类型', max_length=10)
    #
    # platform_bilibili = models.ForeignKey(Platform)
    # lentype_bilibili = models.CharField('时长类型', max_length=10)
    #
    # platform_hunantv = models.ForeignKey(Platform)
    # lentype_hunantv = models.CharField('时长类型', max_length=10)
    #
    # platform_baofeng = models.ForeignKey(Platform)
    # lentype_baofeng = models.CharField('时长类型', max_length=10)
    #
    # platform_fun = models.ForeignKey(Platform)
    # lentype_fun = models.CharField('时长类型', max_length=10)
    #
    # platform_pptv = models.ForeignKey(Platform)
    # lentype_pptv = models.CharField('时长类型', max_length=10)
    #
    # platform_tv189 = models.ForeignKey(Platform)
    # lentype_tv189 = models.CharField('时长类型', max_length=10)
    #
    # platform_baidu = models.ForeignKey(Platform)
    # lentype_baidu = models.CharField('时长类型', max_length=10)
    #
    # platform_pipi = models.ForeignKey(Platform)
    # lentype_pipi = models.CharField('时长类型', max_length=10)
    #
    # platform_tangdou = models.ForeignKey(Platform)
    # lentype_tangdou = models.CharField('时长类型', max_length=10)
    #
    # platform_acfun = models.ForeignKey(Platform)
    # lentype_acfun = models.CharField('时长类型', max_length=10)


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
    key_exclude = models.CharField('排除关键词', max_length=100)


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

