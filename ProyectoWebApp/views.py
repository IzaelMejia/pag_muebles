from django.shortcuts import render, HttpResponse

# Importar servicios que pudimos haber cargado desde panel de administración de django

# Create your views here.

def home(request):
    return render (request, "ProyectoWebApp/home.html")


def tienda(request):
    return render (request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render (request, "ProyectoWebApp/blog.html")
  

def contacto(request):
    return render (request, "ProyectoWebApp/contacto.html")
