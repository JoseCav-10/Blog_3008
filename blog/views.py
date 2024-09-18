from django.shortcuts import render
from .models import User,Post
from .forms import UserForm, PostForm
from django.utils import timezone
# Create your views here.

def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            mensage = form.cleaned_data['mensage']

            Post.objects.create(user=user, mensage=mensage, data_publicacao=timezone.now())

    form = PostForm()
    objs = Post.objects.all()
    context = {
        "posts": objs,
        "form": form
    }
    return render(request, 'index.html', context=context)



def about_user(request):
    objs = User.objects.all()

    context = {
        "users": objs
    }
    return render(request, "about.html", context=context)

def contact(request, *args, **kwargs):

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    form = UserForm()

    return render(request, "contact.html", {"form": form})