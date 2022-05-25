from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import blogpost

# Create your views here.

@login_required(login_url='login')
def index(req):
    posts = blogpost.objects.all()
    return render(req, 'blog/index.html', context={'posts':posts})
