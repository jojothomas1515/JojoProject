from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

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
    post = get_object_or_404(blogpost.objects.all(), pk=pk)
    context = {'post': post}
    if req.user.is_staff:
        context['is_admin'] = True
    else:
        pass
    return render(req, 'blog/post.html', context=context)
