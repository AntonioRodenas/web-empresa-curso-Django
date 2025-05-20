from django.contrib import admin
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj = None): # si en tiempo de eecucion, el usuario es del grupo personal...
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name') #
        else:
            return ('created', 'updated') # si no es del grupo personal, no puede editar el campo key y name
    

admin.site.register(Link, LinkAdmin) # Activamos el modelo Link en el admin de Django

