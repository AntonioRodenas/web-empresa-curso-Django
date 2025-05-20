from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all() # todos los post de la base de datos
    return render(request, "blog/blog.html", {'posts': posts}) 
    # renderiza el template blog.html y le pasa la variable posts que contiene todos los post de la base de datos


def categori(request, categori_id):
    categori = get_object_or_404(Category, id=categori_id) # filtra los post por categoria
    
    return render(request, "blog/categori.html", {'categori': categori})
    # renderiza el template categori.html y le pasa la variable categori que contiene los post filtrados por categoria
