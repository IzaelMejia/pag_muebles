from django.contrib import admin
from .models import LineaPedido, Pedido

    
# Registrar modelos
admin.site.register([Pedido, LineaPedido])