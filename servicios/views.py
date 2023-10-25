from django.shortcuts import render
from servicios.models import Servicio


# Create your views here.
def servicios(request):
    # Obtener todos los servicios que construimos en models.py
    servicios = Servicio.objects.all()
    # Devuevle plantilla Rernderizada y incluir los servicios construidos
    return render (request, "servicios/servicios.html", {"servicios": servicios})
