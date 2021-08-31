# Modelos de la app Services
from django.db import models
from django.db.models.base import Model

class Service(models.Model):
    ''' Modelo de Servicios'''

    # Atributos
    title = models.CharField(
        max_length = 50,
        verbose_name = 'Titulo'
    )

    subtitle = models.CharField(
        max_length = 200,
        verbose_name = 'Subtitulo'
    )

    content = models.TextField(verbose_name ='Contenido')

    image = models.ImageField(
        verbose_name ='Imagen',
        upload_to = 'media/services'
    )

    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Fecha de creacion'
    )

    updated = models.DateTimeField(
        auto_now = True,
        verbose_name = 'Fecha de actualizacion'
    )

    class Meta:
        ''' La clase Meta permite ordenar la lista de servicios
            por fecha de creacion y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    # Metodos
    def __str__(self):
        return self.title