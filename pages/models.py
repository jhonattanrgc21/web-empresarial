from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(
        max_length = 200,
        verbose_name = 'Titulo',
        unique = True
    )

    content = RichTextField(
        verbose_name = 'Contenido'
    )

    order = models.SmallIntegerField(verbose_name = 'Orden', default = 0)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ''' La clase Meta permite ordenar la lista de paginas
            por nombre y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order','title']

    # Metodos
    def __str__(self):
        return self.title