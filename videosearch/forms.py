#coding=utf-8
from django import forms


class PlatformConfigForm(forms.Form):
    # 0: 全部， 1：0-10分钟，2：10-30分钟，3：30-60分钟，4：60分钟以上
    platform_name = forms.BooleanField(label='平台')
    type0 = forms.BooleanField(label='全部')
    type1 = forms.BooleanField(label='0-10分钟')
    type2 = forms.BooleanField(label='10-30分钟')
    type3 = forms.BooleanField(label='30-60分钟')
    type4 = forms.BooleanField(label='60分钟以上')
