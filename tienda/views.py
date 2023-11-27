from django.shortcuts import render
from .models import Producto
# Create your views here.

def tienda(request):
    # variable para alamacenar lista de productos y pasamos ese "diccionario"
    productos= Producto.objects.all()
    return render (request, "tienda/tienda.html",{"productos":productos})
