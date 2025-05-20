from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorías'
        ordering = ['-created'] # ordeno por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicación') # Establecida por el usuario
    category = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts') # Relaciona la categoria con el post, el related_name es para acceder a los posts desde la categoria
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='Imagen') # null y blank si el usuario no quiere subir una imagen
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE) # Relaciona el autor con el usuario que creó la entrada
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created'] # ordeno por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        return self.title
