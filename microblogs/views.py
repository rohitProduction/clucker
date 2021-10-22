from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, PostForm, LogInForm
from .models import User, Post

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method =='POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')

def new_post(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            post = Post(author = user, text = form['text'].value())
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts': posts})

def user_list(request):
    u_list = User.objects.all()
    return render(request, 'user_list.html', {'u_list': u_list})

def show_user(request, user_id):
    user = User.objects.all()[user_id]
    return render(request, 'show_user.html', {'user': user})
