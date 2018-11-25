from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name='咨询姓名')
    phone = models.CharField(max_length=11,verbose_name='咨询电话')
    course = models.CharField(max_length=20,verbose_name='咨询课程')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户咨询信息'
        verbose_name_plural= verbose_name

class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile,verbose_name='收藏用户')
    #通过love_id和love_type一起确定收藏的是什么
    love_id = models.IntegerField(verbose_name='收藏id')
    love_type = models.IntegerField(choices=((1,'机构'),(2,'课程'),(3,'教师')),verbose_name='收藏类型')
    love_status = models.BooleanField(default=False,verbose_name='收藏状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.love_man.username

    class Meta:

        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_man = models.ForeignKey(UserProfile,verbose_name='评论人')
    comment_course = models.ForeignKey(CourseInfo,verbose_name='评论课程')
    comment_content = models.CharField(max_length=200,verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户评论信息'
        verbose_name_plural = verbose_name

class UserCourseInfo(models.Model):
    study_man = models.ForeignKey(UserProfile,verbose_name='学习用户')
    study_course = models.ForeignKey(CourseInfo,verbose_name='学习课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.study_man.username

    class Meta:
        unique_together = ('study_man','study_course')
        verbose_name = '用户学习课程信息'
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    #如果存入的是一个0，代表是系统发的消息是给每个人发的
    #如果存入的是一个正常id,代表的是专门给这个用户发的
    msg_man = models.IntegerField(verbose_name='接收人id')
    msg_content = models.CharField(max_length=200,verbose_name='消息内容')
    is_readed = models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.msg_content

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name



