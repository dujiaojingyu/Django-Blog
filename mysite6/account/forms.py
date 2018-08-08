from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("密码不匹配")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth','phone')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school','company','profession','address','aboutme','photo')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

