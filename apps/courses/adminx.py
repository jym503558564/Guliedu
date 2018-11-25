import xadmin
from .models import CourseInfo,LessonInfo,VideoInfo,SourceInfo
# Create your models here.

class CourseInfoXadmin(object):
    list_display = ['name','image','study_time','level','lesson_num','category','teacherinfo','desc']



class LessonInfoXadmin(object):
    list_display = ['name','courseinfo','add_time']



class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'url','lessoninfo','add_time']



class SourceInfoXadmin(object):
    list_display = ['name','down_load','courseinfo','add_time']


xadmin.site.register(CourseInfo,CourseInfoXadmin)
xadmin.site.register(LessonInfo,LessonInfoXadmin)
xadmin.site.register(VideoInfo,VideoInfoXadmin)
xadmin.site.register(SourceInfo,SourceInfoXadmin)

