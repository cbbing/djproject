#coding:utf-8

from django import forms
from django.utils.timezone import now
from models import CureData

class CureDataForm(forms.Form):
    name = forms.CharField(label="名称")
    cureDuration = forms.IntegerField(label="时长")
    create_at = forms.DateTimeField(label="创建时间", initial=now())
    note = forms.CharField(label="备注", required=False)
    image = forms.FileField(label="图片", required=False)
    operator = forms.CharField(label="操作者")
    status = forms.IntegerField(label="状态")

class CureDataImageForm(forms.ModelForm):

    class Meta:
        model = CureData
        fields = '__all__'