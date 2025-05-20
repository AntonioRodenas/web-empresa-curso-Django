from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm() # instanciamos el formulario. Creamos la plantilla vacia

    if request.method == 'POST': # si el método de la petición es POST. Si se ha enviado algún dato
        contact_form = ContactForm(data=request.POST) # Rellenamos la plantilla con los datos enviados
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            # Suponemos que todo has ido bien y enviamos un mensaje de éxito
            return redirect(reverse('contact')+'?ok') # redirigimos a la vista de contacto. Esto es como un template-tag-url


    return render(request, "contact/contact.html", {'form': contact_form}) 
        # renderizamos la plantilla contact.html y le pasamos el formulario

