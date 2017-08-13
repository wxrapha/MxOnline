# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/8/13 上午10:01'


from django.conf.urls import url, include


from .views import OrgView,AddUserAskView


urlpatterns = [
#课程机构首页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]