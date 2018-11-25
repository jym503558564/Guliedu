"""GuliEdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import user_register,user_login,user_logut,user_active,user_forget,user_reset,usercenter_info,usercenter_changeimage,usercenter_changeinfo,usercenter_changeemail,usercenter_mycourse,usercenter_fav_org,usercenter_fav_teacher,usercenter_fav_course,usercenter_message,usercenter_resetemail,usercenter_changemsg

urlpatterns = [
    url(r'^user_register/$',user_register,name='user_register'),
    url(r'user_login/$',user_login,name='user_login'),
    url(r'^user_logut/$',user_logut,name='user_logut'),
    url(r'^user_active/(\w+)/$',user_active,name='user_active'),
    url(r'^user_forget/$',user_forget,name='user_forget'),
    url(r'^user_reset/(\w+)/$',user_reset,name='user_reset'),

    url(r'^usercenter_info/$',usercenter_info,name='usercenter_info'),
    url(r'^usercenter_changeimage/$',usercenter_changeimage,name='usercenter_changeimage'),
    url(r'^usercenter_changeinfo/$',usercenter_changeinfo,name='usercenter_changeinfo'),
    url(r'^usercenter_changeemail/$',usercenter_changeemail,name='usercenter_changeemail'),
    url(r'^usercenter_resetemail/$',usercenter_resetemail,name='usercenter_resetemail'),

    url(r'^usercenter_mycourse/$',usercenter_mycourse,name='usercenter_mycourse'),
    url(r'^usercenter_fav_org/$',usercenter_fav_org,name='usercenter_fav_org'),
    url(r'^usercenter_fav_teacher/$',usercenter_fav_teacher,name='usercenter_fav_teacher'),
    url(r'^usercenter_fav_course/$',usercenter_fav_course,name='usercenter_fav_course'),
    url(r'^usercenter_message/$', usercenter_message, name='usercenter_message'),
    url(r'^usercenter_changemsg/$', usercenter_changemsg, name='usercenter_changemsg')


]
