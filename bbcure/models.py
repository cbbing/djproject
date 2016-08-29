#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django import forms

# Create your models here.
class CureData(models.Model):
    STATUS_SIZES = (
        (0, '进行中'),
        (1, '已完成'),
    )

    name = models.CharField('名称', max_length=50)
    cureDuration = models.IntegerField('时长')
    create_at = models.DateTimeField("日期", default=now())
    note = models.CharField('备注', max_length=200, blank=True)
    image = models.ImageField('图片', upload_to='photos', blank=True)
    operator = models.CharField('操作者', max_length=50, blank=True)
    status = models.IntegerField('状态', default=0, choices=STATUS_SIZES) # 0,进行中; 1,已完成

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class CureDataImageForm(forms.ModelForm):

    class Meta:
        model = CureData
        fields = '__all__'