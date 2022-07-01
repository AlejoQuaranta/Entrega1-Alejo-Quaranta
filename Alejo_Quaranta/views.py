from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from Alejo_Quaranta.forms import User_registration_form
from django.contrib.auth.decorators import login_required

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {'message': f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)
            
            else:
                context = {'error':'No hay ningun usuario con esas credenciales!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors': errors, 'form': form}
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate( username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form
            context = {'errors' = errors, 'form' = form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register', context = context)

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def familiares(request):
    context = {
        'people' : [
            {
            'name': 'Alejo',
            'surname' : 'Quaranta',
            'age' : 23
            },
            {
            'name': 'Andres',
            'surname' : 'Perez',
            'age' : 32
            }
        ],
        }
    return render(request, 'templates.html', context = context)

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f"Hoy es el dia {fecha}"
    return HttpResponse(mensaje)

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'index.html')
