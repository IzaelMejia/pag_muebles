from django.contrib import admin
from .models import Servicio   #mover dentro del mismo directorio 

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    # Campos de solo LECTURA, nom campos de models.py
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)