from users.models import EmailVerifyCode
from random import randrange
from django.core.mail import send_mail
from GuliEdu.settings import EMAIL_FROM

def get_random_code(code_length):
    code = ''
    code_source = '123456790qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(code_length):
        code += code_source[randrange(0,len(code_source)-1)]
    return code

def send_email_code(email,send_type,):
    code = get_random_code(8)
    if send_type == 3:
        code = get_random_code(6)
    a = EmailVerifyCode()
    a.email = email
    a.send_type =  send_type
    a.code = code
    a.save()

    send_title = ''
    send_body = ''

    if send_type == 1:
        send_title = '欢迎注册谷粒教育'
        send_body = '请点击以下链接进行激活：\n http://127.0.0.1:8000/users/user_active/'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])

    if send_type == 2:
        send_title = '谷粒教育重置密码邮件'
        send_body = '谷粒教育重置密码邮件:\n http://127.0.0.1:8000/users/user_reset/'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])

    if send_type == 3:
        send_title = '谷粒教育修改邮箱'
        send_body = '请查收您的验证码:'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])
