from PIL import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, info
from django.shortcuts import redirect, render



from .authform import ProfileForm, UpdateForm, loginForm, signupForm
from .isauth import is_authenticated
# Create your views here.
from .models import Profile


@is_authenticated
def loginPage(request):
    if request.method == 'POST':

        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
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
        p_form = ProfileForm(request.POST)

        if form.is_valid() and p_form.is_valid():
            # username,firstname,lastname,email, password1, password2 = form.cleaned_data.get('username'), form.cleaned_data.get('firstname') ,form.cleaned_data.get('lastname'), form.cleaned_data.get('email'), form.cleaned_data.get('password1'),form.cleaned_data.get('password2')
            user = form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()

            info(request, "User created successfully, Login Now")
            return redirect('login')
        else:
            error(request, form.errors.as_text())
    return render(request, 'Authentication/SignupPage.html')


def Logout(request):
    logout(request)
    return redirect('login')


def update_user_information(request, **kwargs):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user)
        update_form = UpdateForm(request.POST, instance=request.user)
        print(profile_form.errors)
        if profile_form.is_valid() and update_form.is_valid():
            user = Profile.objects.get(user=request.user)
            print(user)
            user.username = profile_form.cleaned_data['username']
            user.last_name = profile_form.cleaned_data['last_name']
            user.first_name = profile_form.cleaned_data['first_name']
            if request.FILES:
                user.profile_img =profile_form.cleaned_data['profile_img']
            user.save()
            update_form.save()

            return redirect('profile')
        else:
            error(request, 'failed')
            return redirect('profile')
