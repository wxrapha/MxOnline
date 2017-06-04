# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/3 上午10:59'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
