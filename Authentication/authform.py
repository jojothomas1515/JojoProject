from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class loginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class signupForm(UserCreationForm):
    # username = forms.CharField(max_length=200)
    # firstname = forms.CharField(max_length=200)
    # lastname = forms.CharField(max_length=200)
    # email = forms.EmailField(max_length=200)
    # password1 = forms.CharField(max_length=200)
    # password2 = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]

    def clean(self):
        super(signupForm, self).clean()


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ['username', 'first_name', 'last_name', 'profile_img']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email"]

