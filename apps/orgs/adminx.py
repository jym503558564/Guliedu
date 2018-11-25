import xadmin
from .models import OrgInfo,CityInfo,TeacherInfo

# Create your models here.
class CityInfoXadmin(object):
    list_display = ['name','add_time']
    model_icon = 'fa fa-university'



class OrgInfoXadmin(object):
    list_display = ['name','image','address','cityinfo','category']
    style_fields = {'detail':'ueditor'}


class TeacherInfoXadmin(object):
    list_display = ['name', 'image', 'age', 'orginfo', 'work_year']

xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(TeacherInfo,TeacherInfoXadmin)