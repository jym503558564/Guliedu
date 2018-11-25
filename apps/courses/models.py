from django.db import models
from datetime import datetime
from orgs.models import OrgInfo,TeacherInfo
# Create your models here.

class CourseInfo(models.Model):
    name = models.CharField(max_length=200,verbose_name="课程名称")
    image = models.ImageField(upload_to='course/',max_length=200,verbose_name='课程封面')
    study_time = models.IntegerField(default=0,verbose_name='学习时长')
    study_num = models.IntegerField(default=0,verbose_name='学习人数')
    click_num = models.IntegerField(default=0, verbose_name="浏览量")
    love_num = models.IntegerField(default=0, verbose_name="收藏数")
    level = models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=10,verbose_name="课程难度",default='zj')
    desc = models.CharField(max_length=200,verbose_name='课程简介')
    detail = models.TextField(verbose_name='课程详情')
    is_banner = models.BooleanField(default=False,verbose_name='是否轮播')
    lesson_num = models.IntegerField(default=0,verbose_name='章节数')
    category = models.CharField(choices=(('qd','前端'),('ht','后台')),verbose_name='课程类别',max_length=10)
    course_tell = models.CharField(max_length=200,verbose_name='课程公告')
    need_known= models.CharField(max_length=200,verbose_name='课程须知')
    is_famous = models.BooleanField(default=0, verbose_name='是否经典')
    orginfo = models.ForeignKey(OrgInfo,verbose_name='所属机构')
    teacherinfo = models.ForeignKey(TeacherInfo,verbose_name='所属教师')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class LessonInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='章节名称')
    courseinfo = models.ForeignKey(CourseInfo,verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class VideoInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name='视频名称')
    study_time = models.IntegerField(default=0,verbose_name='学习时长')
    url = models.URLField(max_length=200,verbose_name='视频链接',default='https://www.baidu.com')
    lessoninfo = models.ForeignKey(LessonInfo,verbose_name='所属章节')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name

class SourceInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='资源名称')
    down_load = models.FileField(upload_to='source/',verbose_name='下载链接',max_length=200)
    courseinfo = models.ForeignKey(CourseInfo,verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name