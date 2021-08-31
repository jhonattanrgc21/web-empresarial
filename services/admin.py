# Configuracion de la app Services para el dashboard
from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    # Convierte los campos de fecha en formato de solo lectura
    readonly_fields = ('created', 'updated')

# Registro de las configuraciones en el dashboard
admin.site.register(Service, ServiceAdmin)