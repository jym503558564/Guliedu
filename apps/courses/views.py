from django.shortcuts import render
from .models import CourseInfo
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from operations.models import UserLove,UserCourseInfo
from help_tools.decorations import login_decortions
from django.db.models import Q
# Create your views here.
def course_list(request):
    all_course = CourseInfo.objects.all()
    recomment_sort = all_course.order_by('-study_num')[:3]

    keyword = request.GET.get('keyword', '')
    if keyword:
        all_course = all_course.filter(Q(name__icontains=keyword)|Q(desc__icontains=keyword)|Q(detail__icontains=keyword))
    sorttype = request.GET.get('sorttype','')
    if sorttype:
        if sorttype == 'hot':
            all_course = all_course.order_by('-click_num')
        if sorttype == 'students':
            all_course = all_course.order_by('-study_num')

    pagenum = request.GET.get('pagenum','')
    pa = Paginator(all_course,3)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'courses/course-list.html',{
        'all_course':all_course,
        'pages':pages,
        'recomment_sort':recomment_sort,
        'sorttype':sorttype,
        'keyword':keyword
    })

def course_detail(request,course_id):
    if course_id:
     course = CourseInfo.objects.filter(id = int(course_id))[0]
     course.click_num += 1
     course.save()
     love_state =  False
     love_state1 = False
     if request.user.is_authenticated():
         love = UserLove.objects.filter(love_man=request.user,love_id=int(course_id),love_type=2)
         if love and love[0].love_status:
             love_state =True
         love = UserLove.objects.filter(love_man=request.user, love_id=course.orginfo.id, love_type=1)
         if love and love[0].love_status:
             love_state1 =  True

     recomment_courses = CourseInfo.objects.filter(category=course.category).exclude(id = int(course_id))[:3]
     return render(request,'courses/course-detail.html',{
         'course':course,
         'recomment_courses':recomment_courses,
         'love_state':love_state,
         'love_state1': love_state1,

     })

@login_decortions
def course_video(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(id = int(course_id))[0]


        usercourse = UserCourseInfo.objects.filter(study_man=request.user,study_course=course)
        if not usercourse:
            a = UserCourseInfo()
            a.study_man = request.user
            a.study_course = course
            a.save()
            course.study_num += 1
            course.save()

            course.orginfo.study_num += 1
            course.orginfo.save()


        all_usercourses = UserCourseInfo.objects.filter(study_course=course)
        all_users = [usercourse.study_man for usercourse in all_usercourses]
        all_usercourses = UserCourseInfo.objects.filter(study_man__in=all_users).exclude(study_course=course)
        all_courses = list(set([usercourse.study_course for usercourse in all_usercourses]))
        return render(request,'courses/course-video.html',{
            'course':course,
            'all_courses':all_courses,
        })



