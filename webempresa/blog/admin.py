from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # solo se puede editar el nombre de la categoría

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # solo se puede editar el título, contenido y categorías
    list_display = ('title', 'author', 'published', 'post_category') # columnas que se muestran en el admin
    ordering = ('author', 'published') # ordena por fecha de publicación de forma descendente
    search_fields = ('title','content', 'author__username', 'category__name') # permite buscar por título y contenido
    date_hierarchy = 'published' # permite filtrar por fecha de publicación
    list_filter = ('author__username', 'category__name') # permite filtrar por autor y categoría

    def post_category(self, obj):
        return ", ".join([c.name for c in obj.category.all()]) # devuelve el nombre de la categoría como una cadena separada por comas
    post_category.short_description = 'Categorías' # nombre de la columna en el admin
    


admin.site.register(Category, CategoryAdmin) # registro el modelo Category con su respectivo admin
admin.site.register(Post, PostAdmin) # registro el modelo Post con su respectivo admin

