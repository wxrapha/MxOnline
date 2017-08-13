# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/8/13 上午9:48'
import re
from django import forms


from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    #此处可添加字段
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}%|^176\d{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法',code='mobil_invalid')