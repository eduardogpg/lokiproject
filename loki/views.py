from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from .forms import LoginForm
from .forms import RegisterForm

from users.models import User


def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = User.objects.filter(username=form.data['username']).first()
        
        if user and authenticate(username=user.username, password=form.data['password']):
            django_login(request, user)
            
            messages.success(request, 'Te damos la bienvenida {}'.format(user.username))
            return redirect('wallets:list')
    
    if request.method == 'POST':
        messages.error(request, 'Usuario o contraseña incorrectos')
    
    context = { 'title': 'Login', 'form': form }

    return render(request, 'login.html', context)

def logout(request):
    django_logout(request)
    return redirect('index')


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()

        if user:
            django_login(request, user)
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('wallets:list')

    context = { 'form': form, 'title': 'Registro' }
    return render(request, 'register.html', context)


def index(request):
    return render(request, 'index.html', {})