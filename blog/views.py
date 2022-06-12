from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import BlogPost


# Create your views here.

@login_required(login_url='login')
def index(req):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    if req.user.is_staff:
        context['is_admin'] = True
    else:
        pass

    return render(req, 'blog/index.html', context=context)


@login_required(login_url='login')
def view_post(req, pk):
    post = get_object_or_404(BlogPost.objects.all(), pk=pk)
    context = {'post': post}
    if req.user.is_staff:
        context['is_admin'] = True
    else:
        pass
    return render(req, 'blog/post.html', context=context)


@login_required(login_url='login')
def profile_page(req):
    user = req.user
    user_post = BlogPost.objects.filter(Author=req.user.profile)

    context: dict = {'user': user, 'posts': user_post}

    return render(req, 'blog/profile.html', context=context)


@login_required(login_url='login')
def add_post(req) -> HttpResponse:
    form: PostForm = PostForm(instance=req.user.profile)
    context: dict = {'post': form}

    return render(req, 'blog/add_post.html', context=context)


@login_required(login_url='login')
def about_page(req):
    return render(req, 'blog/about.html')


def add_post_db(req):
    if req.method == 'POST':
        post = PostForm(req.POST, req.FILES)

        if post.is_valid():
            post = post.save(commit=False)
            print(req.FILES.get('logo'))
            post.Author = req.user.profile
            post.save()

            return redirect('home')
    else:
        return redirect('addpost')
