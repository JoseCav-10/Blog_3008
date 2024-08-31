from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    objs = Post.objects.all()
    context = {
        "posts": objs
    }
    return render(request, 'index.html', context=context)



def about_user(request):
    objs = User.objects.all()

    context = {
        "users": objs
    }
    return render(request, "about.html", context=context)