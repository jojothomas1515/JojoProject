import django.contrib.auth.forms
from django.shortcuts import redirect, render
from django.contrib.messages import error

from django.contrib.auth import login, logout, authenticate

from .isauth import is_authenticated
from .authform import loginForm, signupForm
# Create your views here.
@is_authenticated
def loginPage(request):
    if request.method == 'POST':

        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            print(f'username : {username} , password : {password}')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error(request, 'The username or password is incorrect')

    return render(request, 'Authentication/LoginPage.html')


def signupPage(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            # username,firstname,lastname,email, password1, password2 = form.cleaned_data.get('username'), form.cleaned_data.get('firstname') ,form.cleaned_data.get('lastname'), form.cleaned_data.get('email'), form.cleaned_data.get('password1'),form.cleaned_data.get('password2')
            form.save()
        else:
            error(request, form.errors.as_text())





    return render(request, 'Authentication/SignupPage.html')
