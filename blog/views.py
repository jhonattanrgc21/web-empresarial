# Vistas de la app Blog
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
    ''' Obtiene una lista de los posts registrados
        en la BD y los renderiza a la vista blog.html'''
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, 'blog/category.html', {'category': category})