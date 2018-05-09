from django import forms

class UserRegisterForm(forms.Form):
    Name = forms.CharField(label='用户名',max_length=20)
    Password1 = forms.CharField(label='密 码',widget=forms.PasswordInput(),max_length=20)
    Password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    Email = forms.EmailField(label='邮 箱')
class UserLoginForm(forms.Form):
    Nmae = forms.CharField(label='用户名',max_length=20)
    Password = forms.CharField(label='密 码',widget=forms.PasswordInput(),max_length=20)
    