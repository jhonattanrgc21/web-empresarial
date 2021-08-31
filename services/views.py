# Vistas de la app Services
from django.shortcuts import render
from .models import Service

def services(request):
    ''' Obtiene una lista de los servicios registrados
        en la BD y los renderiza a la vista services.html'''
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services })