# Configuracion de la app Services para el dashboard
from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    # Convierte los campos de fecha en formato de solo lectura
    readonly_fields = ('created', 'updated',)

class PostAdmin(admin.ModelAdmin):
    # Convierte los campos de fecha en formato de solo lectura
    readonly_fields = ('created', 'updated',)

    # Lista las columnas especificadas por cada registro
    list_display = ('title', 'author', 'published', 'post_categories',)

    # Permite ordenar las columnas por los campos especificados
    ordering = ('author', 'published' ,)

    # Agrega un buscador con las opciones de los campos especificados
    search_fields = ('title', 'content', 'author__username', 'categories__name',)

    # Permite obtener una lista de registros por fechas
    date_hierarchy = 'published'

    # Permite crear filtros para el buscador
    list_filter = ('author__username', 'categories__name')

    # Este tipo de funcion es para los campos de muchos a muchos o uno a muchos
    def post_categories(self, obj):
        ''' Obtiene una lista de categorias asociadas al registro
            ordenadas por nombre y separadas por coma '''
        return (',').join([c.name for c in obj.categories.all().order_by('name')])

    # Asigna un nombre a la funcion para mostrar en la columna de los registros
    post_categories.short_description = 'Categorias'

# Registro de las configuraciones en el dashboard
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)