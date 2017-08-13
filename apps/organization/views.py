# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from .models import CourseOrg, CityDict
from .forms import UserAskForm


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

class OrgView(View):
    """
    课程机构
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        all_citys = CityDict.objects.all()
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-courses_nums')

        org_nums = all_orgs.count()
        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1


        p = Paginator(all_orgs, 1, request=request)

        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort':sort
        })


class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form = userask_form.save(commit=True)
            return HttpResponse("{'status':'success'}", content_type="application/json")
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type="application/json")