from django import forms
from .models import UserAsk
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','phone','course']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        com = re.compile('^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$')
        if com.match(phone):
            return phone
        else:
            raise  forms.ValidationError('手机号码不合法')

class UserCommentAddForm(forms.Form):
    comment_id = forms.IntegerField(required=True)
    comment_text = forms.CharField(required=True,min_length=1,max_length=300)
