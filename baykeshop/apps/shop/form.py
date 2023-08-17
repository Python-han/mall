from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    """ 登录表单 """
    username = UsernameField(
        widget=forms.TextInput(attrs={
            "autofocus": True, 
            "class": "input", 
            "placeholder":" 请输入用户名..."
        }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password", 
            "class": "input", 
            "placeholder":" 请输入密码..."
        }),
    )