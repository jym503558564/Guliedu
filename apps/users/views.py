from django.shortcuts import render,redirect,reverse,HttpResponse
from .forms import UserRegisterForm,UserLoginForm,UserForgetForm,UserResetForm,UserChangeImageForm,UserChangeInfoForm,UserChangeEmailForm,UseResetEmailForm
from django.contrib.auth import authenticate,logout,login
from .models import EmailVerifyCode,UserProfile,BannerInfo
from courses.models import CourseInfo
from django.db.models import Q
from help_tools.send_email_tools import send_email_code
from django.http import JsonResponse
from operations.models import UserCourseInfo,UserLove,UserMessage
from orgs.models import OrgInfo,TeacherInfo
from datetime import datetime
from .models import BannerInfo

# Create your views here.
def index(request):
    all_banners = BannerInfo.objects.all()
    course_bannercourses = CourseInfo.objects.filter(is_banner = True).order_by('-add_time')[:2]
    all_courses = CourseInfo.objects.filter(is_banner=False).order_by('-add_time')[:6]
    all_orgs = OrgInfo.objects.all()[:15]


    return render(request,'index.html',{
        'all_banners':all_banners,
        'course_bannercourses':course_bannercourses,
        'all_courses':all_courses,
        'all_orgs':all_orgs
    })


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request,'users/register.html',{
            'user_register_form': user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username = email)|Q(email = email))
            if user_list:
                return render(request,'users/register.html',{
                    'msg':'用户已经存在'
                })
            else:
                a = UserProfile()
                a.username = email
                a.email = email
                a.set_password(password)
                a.save()
                send_email_code(email,1)
                return HttpResponse('邮件发送成功，请尽快登录您的邮箱进行激活')

        else:
            return render(request,'users/register.html',{
                'user_register_form':user_register_form
            })

def user_login(request):
    if request.method == 'GET':
        return render(request,'users/login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            email = user_login_form.cleaned_data['email']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username = email,password = password)
            if user:
                if user.is_start:
                    login(request,user)
                    a = UserMessage()
                    a.msg_man = request.user.id
                    a.msg_content = '欢迎登录'
                    a.save()
                    url = request.COOKIES.get('url','/')
                    return redirect(url)
                else:
                    return HttpResponse('请尽快去您的邮箱激活账号，否则不能登录')
            else:
                return render(request,'users/login.html',{
                    'msg':'用户名或者密码错误'
                })
        else:
            return render(request, 'users/login.html', {
                    'user_login_form':user_login_form
                })

def user_logut(request):
    logout(request)
    ret = redirect('/')
    ret.delete_cookie('url')
    return ret


def user_active(request,code):
    if code:
        email_ver = EmailVerifyCode.objects.filter(code = code)
        if email_ver:
            email = email_ver[0].email
            user = UserProfile.objects.filter(email = email)[0]
            user.is_start = True
            user.save()
            email_ver.delete()
            return redirect(reverse('users:user_login'))
        else:
            return HttpResponse('验证码无效')
    else:
        return HttpResponse('验证码不存在')



def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request,'users/forgetpwd.html',{
            'user_forget_form':user_forget_form
        })
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email = user_forget_form.cleaned_data['email']
            user = UserProfile.objects.filter(email = email)
            if user:
                send_email_code(email,2)
                return HttpResponse('邮件发送成功，请尽快前往邮箱进行重置密码')
            else:
                return render(request,'users/forgetpwd.html',{
                    'msg':'您输入的邮箱有误！'
                })
        else:
            return render(request, 'users/forgetpwd.html', {
                'user_forget_form':user_forget_form})


def user_reset(request,code):
    if code:
        if request.method == 'GET':
            return render(request,'users/password_reset.html',{
                'code':code
            })
        else:
            user_reset_form = UserResetForm(request.POST)
            if user_reset_form.is_valid():
                password = user_reset_form.cleaned_data['password']
                password1 = user_reset_form.cleaned_data['password1']
                if password1 == password:
                    email_ver = EmailVerifyCode.objects.filter(code = code)
                    if email_ver:
                        email = email_ver[0].email
                        user = UserProfile.objects.filter(email = email)[0]
                        user.set_password(password)
                        user.save()
                        return redirect(reverse('users:user_login'))
                    else:
                        return render(request,'users/password_reset.html',{
                            'mag':'验证码不存在',
                            'code':code

                        })
                else:
                    return render(request,'users/password_reset.html',{
                        'msg':'两次输入的密码不一致',
                        'code':code
                    })
            else:
                return render(request,'users/password_reset.html',{
                    'user_reset_form':user_reset_form,
                    'code': code
                })

def usercenter_info(request):
    return render(request,'users/usercenter-info.html')

def usercenter_changeimage(request):
    user_change_image_form = UserChangeImageForm(request.POST,request.FILES,instance=request.user)
    if user_change_image_form.is_valid():
        user_change_image_form.save(commit=True)
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'fail'})


def usercenter_changeinfo(request):
    usercenter_changeinfo_form = UserChangeInfoForm(request.POST,instance=request.user)
    if usercenter_changeinfo_form.is_valid():
        usercenter_changeinfo_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'修改成功'})

    else:
        return JsonResponse({'status':'fail','msg':'修改失败'})

def usercenter_changeemail(request):
    usercenter_changeemail_form =UserChangeEmailForm(request.POST)
    if usercenter_changeemail_form.is_valid():
        email = usercenter_changeemail_form.cleaned_data['email']
        user_list = UserProfile.objects.filter(Q(username = email)|Q(email = email))
        if user_list:
            return JsonResponse({'status': 'fail', 'msg': '邮箱已经被绑定'})
        else:
            email_ver =EmailVerifyCode.objects.filter(email=email,send_type=3)
            if email_ver:
                email_info = email_ver.order_by('-add_time')[0]
                if(datetime.now() - email_info.add_time).seconds<60:
                    return JsonResponse({'status': 'fail', 'msg': '不要重复发送'})

                email_info.delete()
                send_email_code(email, 3)
            else:
                send_email_code(email,3)
            return JsonResponse({'status':'ok','msg':'请尽快去您的邮箱查询验证码'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '邮箱有问题'})

def usercenter_resetemail(request):
    usercenter_resetemail_form = UseResetEmailForm(request.POST)
    if usercenter_resetemail_form.is_valid():
        email = usercenter_resetemail_form.cleaned_data['email']
        code = usercenter_resetemail_form.cleaned_data['code']
        if email and code:
            email_ver = EmailVerifyCode.objects.filter(email=email, code=code)
            if email_ver:
                request.user.username = email
                request.user.email = email
                request.user.save()
                return JsonResponse({'status': 'ok', 'msg': '修改成功'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '邮箱或验证码错误'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '邮箱或验证码错误'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '邮箱或验证码错误'})


def usercenter_mycourse(request):
    all_usercourses = UserCourseInfo.objects.filter(study_man = request.user)
    all_courses =[usercourse.study_course for usercourse in all_usercourses]
    return render(request,'users/usercenter-mycourse.html',{
        'all_courses':all_courses
    })

def usercenter_fav_org(request):
    all_userloves = UserLove.objects.filter(love_man=request.user, love_type=1, love_status=True)
    all_orgids = [userlove.love_id for userlove in all_userloves]
    all_orgs = OrgInfo.objects.filter(id__in=all_orgids)
    return render(request, 'users/usercenter-fav-org.html', {
        'all_orgs': all_orgs
    })


def usercenter_fav_teacher(request):
    all_userloves = UserLove.objects.filter(love_man=request.user, love_type=3, love_status=True)
    all_teacherids = [userlove.love_id for userlove in all_userloves]
    all_teachers = TeacherInfo.objects.filter(id__in=all_teacherids)
    return render(request,'users/usercenter-fav-teacher.html',{
        'all_teachers':all_teachers
    })

def usercenter_fav_course(request):
    all_userloves = UserLove.objects.filter(love_man=request.user, love_type=2, love_status=True)
    all_courseids = [userlove.love_id for userlove in all_userloves]
    all_courses = CourseInfo.objects.filter(id__in=all_courseids)
    return render(request, 'users/usercenter-fav-course.html', {
        'all_courses': all_courses
    })


def usercenter_message(request):
    all_messages = UserMessage.objects.filter(msg_man= request.user.id)
    return render(request,'users/usercenter-message.html',{'all_messages':all_messages})

def usercenter_changemsg(request):
    msgid = request.GET.get('msgid', '')
    if msgid:
        msg = UserMessage.objects.filter(id=int(msgid))[0]
        msg.is_readed = True
        msg.save()
        return JsonResponse({'status': 'ok', 'msg': '已经读取'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '读取失败'})



def handler_404(request):
    return render(request,'users/handler_404.html')

def handler_500(request):
    return render(request,'users/handler_500.html')










