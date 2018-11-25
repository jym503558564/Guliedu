from django import forms
from .models import UserProfile
import re

#导入验证码字段
from captcha.fields import CaptchaField
class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True,min_length=10,error_messages={
        'required':'邮箱必须填写',
        'min_length':'邮箱最小长度必须10位'
    })

    password = forms.CharField(required=True, min_length=3, error_messages={
        'required': '密码必须填写',
        'min_length': '密码最小长度必须3位'
    })

    captcha = CaptchaField()

class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True,min_length=10,error_messages={
        'required':'邮箱必须填写',
        'min_length':'邮箱最小长度必须10位'
    })

    password = forms.CharField(required=True, min_length=3, error_messages={
        'required': '密码必须填写',
        'min_length': '密码最小长度必须3位'
    })


class UserForgetForm(forms.Form):
    email = forms.EmailField(required=True, min_length=10, error_messages={
        'required': '邮箱必须填写',
        'min_length': '邮箱最小长度必须10位'
    })

    captcha = CaptchaField()

class UserResetForm(forms.Form):
    password = forms.CharField(required=True, min_length=3, error_messages={
        'required': '密码必须填写',
        'min_length': '密码最小长度必须3位'
    })
    password1 = forms.CharField(required=True, min_length=3, error_messages={
        'required': '重复密码必须填写',
        'min_length': '重复密码最小长度必须3位'
    })

class UserChangeImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class UserChangeInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','birthday','gender','address','phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        com = re.compile('^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$')
        if com.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号码不合法')

class UserChangeEmailForm(forms.Form):
    email = forms.EmailField(required=True)

class UseResetEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    code = forms.CharField(required=True,min_length=6,max_length=6)