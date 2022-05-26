from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import blogpost


# Create your views here.

@login_required(login_url='login')
def index(req):
    posts = blogpost.objects.all()
    context = {'posts': posts}
    if req.user.is_staff:
        context['is_admin'] = True
    else:
        pass

    return render(req, 'blog/index.html', context=context)

@login_required(login_url='login')
def view_post(req, pk):
    post = blogpost.objects.get(pk=pk)
    context = {'post': post.Post}
    if req.user.is_staff:
        context['is_admin'] = True
    else:
        pass
    return render(req, 'blog/post.html', context=context)
