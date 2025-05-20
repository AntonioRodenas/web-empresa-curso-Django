from django.contrib import admin
from .models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order') # Campos que se verán en la lista de páginas


admin.site.register(Page, PageAdmin) # Activamos el modelo Page en el admin de Django

