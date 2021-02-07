from django import forms
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from myuser.models import MyUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


