from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

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
    return render(request, 'index.html')
