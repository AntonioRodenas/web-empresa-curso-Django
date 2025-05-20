from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    services = Service.objects.all()  # Obtengo todos los servicios de la base de datos
    return render(request, "services/services.html", {'services': services})  # Renderizo la plantilla y le paso los servicios como contexto
