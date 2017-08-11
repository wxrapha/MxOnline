# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_citys = CityDict.objects.all()
        return render(request, 'org-list.html', {
            'all_orgs':all_orgs,
            'all_citys':all_citys,
            'org_nums':org_nums
        })