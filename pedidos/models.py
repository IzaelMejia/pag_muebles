from django.db import models 
from django.contrib.auth import get_user_model
from tienda.models import Producto #clase producto
from django.db.models import F, Sum, FloatField 

User=get_user_model() # Obtiene el modelo de usuario activo de Django

# Create your models here.
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at  = models.DateTimeField(auto_now_add=True)
    #estado = models.CharField(max_length=20, default='Pendiente')

    class Meta:
        db_table = 'pedidos' 
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id'] #ordenar por id

    def __str__(self):
        return self.id
    
    @property  #propiedad para que devuelva el total del pedido
    def total(self):
        # Calcula el total del pedido sumando el producto de precio y cantidad para cada línea de pedido
        return self.lineapedidos_set.aggregate(
            total=Sum(F('precio') * F('cantidad'), output_field=FloatField())
        )["total"]



class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']

    # Representación en cadena de la línea de pedido
    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto_id.nombre}"
    
    @property
    def total(self): # Calcula el total de la línea de pedido multiplicando el precio por la cantidad
        return self.precio * self.cantidad
    
