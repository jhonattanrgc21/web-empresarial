# Modelos de la app Blog
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    ''' Modelo de Categorias '''

    # Atributos
    name = models.CharField(
        max_length = 20,
        verbose_name = 'Etiqueta'
    )

    # Fechas
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ''' La clase Meta permite ordenar la lista de categorias
            por fecha de creacion y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    # Metodos
    def __str__(self):
        return self.name

class Post(models.Model):
    ''' Modelo de Post '''

    # Atributos
    title = models.CharField(
        max_length = 100,
        verbose_name = 'Titulo'
    )

    content = models.TextField(verbose_name = 'Contenido')
    published = models.DateTimeField(
        verbose_name = 'Fecha de publicacion',
        default = now()
    )

    image = models.ImageField(
        verbose_name = 'Imagen',
        upload_to = 'media/blog',
        null = True,
        blank = True
    )

    # Relaciones
    author = models.ForeignKey(
        User,
        verbose_name = 'Autor',
        on_delete = models.CASCADE
    )

    categories = models.ManyToManyField(
        Category,
        verbose_name = 'Categorias',
        related_name = 'get_posts'
    )

    # Fechas
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ''' La clase Meta permite ordenar la lista de posts
            por fecha de creacion y traduce el nombre de la
            entidad de ingles a español en el dashboard '''
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    # Metodos
    def __str__(self):
        return self.title