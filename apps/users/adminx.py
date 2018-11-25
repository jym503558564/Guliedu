import xadmin
from .models import BannerInfo,EmailVerifyCode



class BannerInfoXadmin(object):
    list_display = ['image','url','add_time']


class EmailVerifyCodeAdmin(object):
    list_diaplay = ['email','code','send_type','add_time']


xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeAdmin)
