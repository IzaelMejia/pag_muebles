from django.urls import path

# Trabajar vistas en el proyecto 
from . import views

urlpatterns = [
    path('', views.pedidos, name="pedidos"),
    
]
