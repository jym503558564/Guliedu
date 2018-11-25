import xadmin

# Register your models here.
from .models import *

class UserAskXamin(object):
    list_display = ['name','phone','course','add_time']


class UserLoveXadmin(object):
    list_display =['love_man','love_id','love_type','love_status','add_time']



class CommentXadmin(object):
    list_display = ['comment_man','comment_course','comment_content','add_time']


class UserCourseInfoXadmin(object):
    list_display = ['study_man','study_course','add_time']


class UserMessageXadmin(object):
    #如果存入的是一个0，代表是系统发的消息是给每个人发的
    #如果存入的是一个正常id,代表的是专门给这个用户发的
    list_display =['msg_man','msg_content','is_readed','add_time']



xadmin.site.register(UserAsk,UserAskXamin)
xadmin.site.register(UserLove,UserLoveXadmin)
xadmin.site.register(Comment,CommentXadmin)
xadmin.site.register(UserCourseInfo,UserCourseInfoXadmin)
xadmin.site.register(UserMessage,UserMessageXadmin)





