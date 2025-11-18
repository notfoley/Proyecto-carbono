from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form':UserCreationForm
        })
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form':UserCreationForm,
                    'error': 'Username is already taken'
                    })
        else:
            return render(request, 'signup.html', {
            'form': form,
            })
    
def tasks(request):
    return render(request, 'tasks.html', {
        "username": request.user.username
    })

def signout(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method == "GET":
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else: 
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')    