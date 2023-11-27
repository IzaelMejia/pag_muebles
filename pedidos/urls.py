from django.urls import path

# Trabajar vistas en el proyecto 
from . import views

urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
    
]
