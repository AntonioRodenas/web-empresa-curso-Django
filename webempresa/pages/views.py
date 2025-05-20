from django.shortcuts import render, get_object_or_404
from .models import Page


# Create your views here.
def page(request, page_id):
    # Obtengo la página por su id
    page = get_object_or_404(Page, id=page_id)
    
    # Renderizo la plantilla con el contexto
    return render(request, 'pages/sample.html', {'page': page}) # paso el objeto page al template para que lo use

