from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(
        max_length = 100,
        verbose_name = 'Nombre clave',
        unique = True
    )

    name = models.CharField(
        verbose_name = 'Red social',
        max_length = 100
    )

    url = models.URLField(
        max_length = 200,
        verbose_name = 'Enlace',
        null = True,
        blank = True
    )

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ''' La clase Meta permite ordenar la lista de links
            por nombre y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    # Metodos
    def __str__(self):
        return self.name