from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,AuthenticationForm

# profile
class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'write your firstname'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'write your username'}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','profile_image','bio']

        widgets ={
            'last_name':forms.TextInput(attrs={'placeholder':'write your lastname'}),
            'email':forms.EmailInput(attrs={'placeholder':'write your email'}),
            'bio':forms.TextInput(attrs={'placeholder':'write your bio'})
        }

# registration
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'write your name'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'write your name'}))
    username =  forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'write your username'}))
    password1 =  forms.CharField(label='Enter password',widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
    password2 =  forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'write your username'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':'write your password'}))
