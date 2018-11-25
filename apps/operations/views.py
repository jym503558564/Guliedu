from django.shortcuts import render
from .forms import UserAskForm,UserCommentAddForm
from  django.http import JsonResponse
from .models import UserLove,UserCourseInfo,Comment
from courses.models import CourseInfo
from orgs.models import OrgInfo,TeacherInfo
from help_tools.decorations import login_decortions
# Create your views here.
def user_ask(request):
    user_ask_form = UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'咨询成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '咨询失败'})
@login_decortions
def user_love(request):
    loveid = request.GET.get('loveid','')
    lovetype = request.GET.get('lovetype','')

    if loveid and lovetype:
        if int(lovetype) == 1:
            obj = OrgInfo.objects.filter(id=int(loveid))[0]
        elif int(lovetype) == 2:
            obj = CourseInfo.objects.filter(id=int(loveid))[0]
        else:
            obj = TeacherInfo.objects.filter(id=int(loveid))[0]
        love = UserLove.objects.filter(love_man = request.user,love_id = int(loveid),love_type = int(lovetype) )
        if love:
            if love[0].love_status:
                love[0].love_status = False
                love[0].save()
                obj.love_num -= 1
                obj.save()
                return JsonResponse({
                    'status':'ok',
                    'msg':'收藏'
                })
            else:
                love[0].love_status = True
                love[0].save()
                obj.love_num += 1
                obj.save()
                return JsonResponse({
                    'status':'ok',
                    'msg':'取消收藏'
                })
        else:
            a = UserLove()
            a.love_man = request.user
            a.love_id = int(loveid)
            a.love_type = int(lovetype)
            a.love_status = True
            a.save()
            obj.love_num += 1
            obj.save()
            return JsonResponse({
                'status':'ok',
                'msg':'取消收藏'
            })
    else:
        return JsonResponse({
            'status':'fail',
            'msg':'收藏失败'
        })

def course_comment(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(id = int(course_id))[0]
        all_usercourses = UserCourseInfo.objects.filter(study_course=course)
        all_users = [usercourse.study_man for usercourse in all_usercourses]
        all_usercourses = UserCourseInfo.objects.filter(study_man__in=all_users).exclude(study_course=course)
        all_courses = list(set([usercourse.study_course for usercourse in all_usercourses]))
        all_comments = Comment.objects.filter(comment_course=course)
        return render(request,'courses/course-comment.html',{
            'course':course,
            'all_courses': all_courses,
            'all_comments':all_comments
        })
def comment_add(request):
    user_comment_add_from =UserCommentAddForm(request.POST)
    if user_comment_add_from.is_valid():
        comment_id = user_comment_add_from.cleaned_data['comment_id']
        comment_text = user_comment_add_from.cleaned_data['comment_text']

        a = Comment()
        a.comment_man = request.user
        a.comment_content = comment_text
        a.comment_course_id = int(comment_id)
        a.save()

        return JsonResponse({
            'status':'ok',
            'msg':'评论成功'
        })
    else:
        return JsonResponse({
            'status': 'fail',
            'msg': '评论失败'
        })


def user_deletelove(request):
    loveid = request.GET.get('loveid','')
    lovetype = request.GET.get('lovetype','')

    if loveid and lovetype:
        love = UserLove.objects.filter(love_man=request.user,love_id=int(loveid),love_type=int(lovetype),love_status=True)
        if love:
            love[0].love_status=False
            love[0].save()
        return JsonResponse({'status':'ok','msg':'删除成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '删除失败'})