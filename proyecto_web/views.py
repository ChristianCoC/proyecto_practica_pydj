from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from datetime import datetime


# Create your views here.
"""def index(request):
    template = loader.get_template('index.html')
    context = {"hoy": datetime.now()}
    return HttpResponse(template.render(context,request))"""

def index (request):
    return render(request, 'index.html', {'hoy': datetime.now()})

def demo(request):
    return HttpResponse("<h1 style='color:blue'>Hola mundo, Django.</h1>")

def ingles(request):
    return HttpResponse("Hello world, Django.")

def frances(request):
    return HttpResponse("Bonjour le monde, Django.")

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre.upper()}")

# Expresiones regulares
def case_2003(request):
    return HttpResponse("Case 2003")

def year_archive(request, year):
    if year == '2003':
        return HttpResponse("Case 2003")
    else:
        return HttpResponseRedirect(reverse('index'))

def month_archive(request, year, month):
    return HttpResponse(f"Case {year}/{month}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Article {year}/{month}/{slug}")

def despedir(request, nombre):
    nombre_mayuscula = nombre.capitalize()
    return HttpResponse(f"<h1>Hasta luego {nombre_mayuscula}!</h1>")

def productos(request, id):
   return HttpResponse(f"Producto {id}")
   
