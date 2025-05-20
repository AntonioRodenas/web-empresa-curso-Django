from .models import Link


def ctx_dict(request): # dicionario de contexto
    ctx = {} # dicionario de contexto
    links = Link.objects.all() # obtenemos todos los links de la base de datos
    for link in links: # recorremos los links
        ctx[link.key] = link.url
    return ctx 
