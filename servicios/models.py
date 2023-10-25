from django.db import models

# Create your models here. O sea Las Tablas 
# https://docs.djangoproject.com/en/4.2/ref/models/options/  -opciopnes adicionales la modelo

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=260)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True) #fecha automaticamente 
    updated = models.DateTimeField(auto_now=True)     #tiempo automaticamente 

    class Meta:
        verbose_name = 'servicio'    # Especifica el nombre singular que tendrá en la base de datos
        verbose_name_plural = 'servicios'  # Especifica el nombre plural que tendrá en la base de datos
    
    def __str__(self):
        return self.titulo  # Representación en cadena del objeto, devuelve el título del servicio como su representación legible