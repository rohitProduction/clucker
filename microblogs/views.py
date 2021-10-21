from django.shortcuts import render
from .forms import SignUpForm, PostForm

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def feed(request):
    form = PostForm()
    return render(request, 'feed.html', {'form': form})
