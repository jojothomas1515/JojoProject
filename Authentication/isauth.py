from functools import wraps


from django.shortcuts import redirect

def is_authenticated(view_func):
    @wraps(view_func)
    def wrapper(request , *args , **kwargs):
        if request.user.is_authenticated :
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper
