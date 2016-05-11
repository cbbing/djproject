#coding=utf-8
from django import forms
from django.forms import ModelForm
from .models import PlatformConfig, GeneralConfig

class GeneralConfigForm(forms.Form):


    page_count = forms.IntegerField(label='搜索页数')
    key_from = forms.IntegerField(label='关键词来源')

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print 'post data'
        pass

class PlatformConfigForm(forms.Form):
    # 0: 全部， 1：0-10分钟，2：10-30分钟，3：30-60分钟，4：60分钟以上
    platform_name = forms.BooleanField(label='平台')
    type0 = forms.BooleanField(label='全部')
    type1 = forms.BooleanField(label='0-10分钟')
    type2 = forms.BooleanField(label='10-30分钟')
    type3 = forms.BooleanField(label='30-60分钟')
    type4 = forms.BooleanField(label='60分钟以上')


    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class ConfigForm(ModelForm):
    class Meta:
        model = PlatformConfig
        fields = ['platform', 'lentype_all', 'lentype_0_10','lentype_10_30','lentype_30_60','lentype_60_More']

class GeneralConfigForm(ModelForm):
    class Meta:
        model = GeneralConfig
        fields = ['page_count', 'key_from']
        # widgets = {
        #
        #     'operation_date': forms.DateTimeField,
        # }