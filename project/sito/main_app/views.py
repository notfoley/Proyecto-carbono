from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def main_app(request):
    template = loader.get_template('home.html')
    context = {'user': request.user}
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    template = loader.get_template('register.html')
    return HttpResponse(template.render({'form': form}, request))
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    template = loader.get_template('login.html')
    return HttpResponse(template.render({'form': form}, request))

def logout_view(request):
    logout(request)
    return redirect('/')
    
def preguntas(request):
    template = loader.get_template('preguntas.html')
    return HttpResponse(template.render({}, request))
