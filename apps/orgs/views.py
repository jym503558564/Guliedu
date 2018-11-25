from django.shortcuts import render
from .models import OrgInfo,CityInfo,TeacherInfo
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from operations.models import UserLove
from django.db.models import Q
# Create your views here.

def org_list(request):
    all_orgs =OrgInfo.objects.all()
    all_citys = CityInfo.objects.all()
    sort_orgs = all_orgs.order_by('-click_num')[:3]

    #按照关键字搜索
    keyword = request.GET.get('keyword','')
    if keyword:
        all_orgs = all_orgs.filter(Q(name__icontains=keyword)|Q(desc__icontains=keyword)|Q(detail__icontains=keyword))

    #按照机构分页
    cat = request.GET.get('cat','')
    if cat:
        all_orgs = all_orgs.filter(category = cat )

    #按照地区分页
    cid = request.GET.get('cid','')
    if cid:
        all_orgs = all_orgs.filter(cityinfo_id = int(cid))

    #按照排序规则排序
    sorttype = request.GET.get('sorttype','')
    if sorttype:
        if sorttype == 'studynum':
            all_orgs = all_orgs.order_by('-study_num')
        if sorttype == 'coursenum':
            all_orgs = all_orgs.order_by('-course_num')

    pa = Paginator(all_orgs,3)
    pagenum = request.GET.get('pagenum','')
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'orgs/org-list.html',{
        'all_orgs':all_orgs,
        'all_citys':all_citys,
        'sort_orgs':sort_orgs,

        'pages':pages,
        'cat':cat,
        'cid':cid,
        'sorttype':sorttype,
        'keyword':keyword
    })

def org_detail(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id = int(org_id))[0]
        org.click_num +=1
        org.save()
        love_state = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1)
            if love and love[0].love_status:
                love_state = True
            else:
                love_state = False
        return render(request,'orgs/org-detail-homepage.html',{
            'org':org,
            'detail_type':'detail_home',
            'love_state':love_state
        })

def org_course(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id = int(org_id))[0]
        love_state = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1)
            if love and love[0].love_status:
                love_state = True
            else:
                love_state = False
        all_courses = org.courseinfo_set.all()

        pa = Paginator(all_courses, 4)
        pagenum = request.GET.get('pagenum', '')
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        return render(request,'orgs/org-detail-course.html',{
            'org':org,
            'pages':pages,
            'detail_type': 'detail_course',
            'love_state': love_state

        })

def org_desc(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        love_state = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1)
            if love and love[0].love_status:
                love_state = True
            else:
                love_state = False
        return render(request, 'orgs/org-detail-desc.html', {
            'org': org,
            'detail_type': 'detail_desc',
            'love_state':love_state
        })

def org_teacher(request,org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        love_state = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1)
            if love and love[0].love_status:
                love_state = True
            else:
                love_state = False
        return render(request, 'orgs/org-detail-teachers.html', {
            'org': org,
            'detail_type': 'detail_teacher',
            'love_state':love_state
        })

def teacher_list(request):
    all_teachers = TeacherInfo.objects.all()
    teachers_sort = all_teachers.order_by('-click_num')[:3]

    keyword = request.GET.get('keyword', '')
    if keyword:
        all_teachers = all_teachers.filter(name__icontains=keyword)

    sorttype = request.GET.get('sorttype','')
    if sorttype:
        if sorttype == 'hot':
            all_teachers = all_teachers.order_by('-love_num')

    pa = Paginator(all_teachers,2)
    pagenum = request.GET.get('pagenum','')
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'orgs/teachers-list.html',{
        'all_teachers':all_teachers,
        'teachers_sort':teachers_sort,
        'pages':pages,
        'sorttype':sorttype,
        'keyword':keyword
    })

def teacher_detail(request,teacher_id):
    if teacher_id:
        teacher = TeacherInfo.objects.filter(id = int(teacher_id))[0]
        teacher.click_num += 1
        teacher.save()
        love_state = False
        love_state1 = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user,love_id=int(teacher_id),love_type=3)
            if love and love[0].love_status:
                love_state = True
            love = UserLove.objects.filter(love_man=request.user,love_id=teacher.orginfo.id,love_type=1)
            if love and love[0].love_status:
                love_state1 = True

        all_teachers = TeacherInfo.objects.all()
        teachers_sort = all_teachers.order_by('-love_num')[:3]

        return render(request,'orgs/teacher-detail.html',{
            'teacher':teacher,
            'teachers_sort':teachers_sort,
            'love_state':love_state,
            'love_state1':love_state1
        })


