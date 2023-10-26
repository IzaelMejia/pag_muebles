from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)     
    
    class Meta:
        verbose_name = 'categoria'    # Especifica el nombre singular que tendrá en la base de datos
        verbose_name_plural = 'categorias'  # Especifica el nombre plural que tendrá en la base de datos
    
    def __str__(self):
        return self.nombre  # Representación en cadena del objeto, devuelve el nombre del servicio como su representación legible
    

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=260)
    imagen = models.ImageField(upload_to='blog', null=True , blank=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    #Un Post puede tener diferentes categorias entonces establecemos lazo con Categorias, 
    # relacion varios a varios
    categorias=models.ManyToManyField(Categoria) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)     
    
    class Meta:
        verbose_name = 'post'    # nombre tendra en base de datos
        verbose_name_plural = 'posts'  # Especifica el nombre plural que tendrá en la base de datos
    
    def __str__(self):
        return self.titulo
