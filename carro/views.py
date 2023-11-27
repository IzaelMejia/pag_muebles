from django.shortcuts import render

# Importar clase carro y importar productos de modelos 
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect  #para redicreccionar 

# Create your views here.
def agregar_producto(request, producto_id):
    carro = Carro(request)  #crear carro 
    producto = Producto.objects.get(id=producto_id)  #obtener producto
    carro.agregar(producto=producto)  #agregar producto al carro
    return redirect("tienda")  #redireccionar a tienda

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")



