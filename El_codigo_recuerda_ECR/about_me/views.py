from django.shortcuts import render
from django.http import HttpResponse
from .models import About_me, Network


# Create your views here.
#def home(request):
#    return render(request, 'index.html', {})


# OPERACIONES CRUD
# operacion para crear registros dentro de la tabla about_me
#def Create(request):
#    person = About_me.objects.create(document='1014218980', names='Eduard Nicolás', last_names='Sarmiento Herrera', address='Calle 69a 112a - 13')


def Read(request):
    person = About_me.objects.all()
    url = Network.objects.get(shortname='LinkedIn')
    return render(request, 'index.html', {'person': person, 'url': url})


#def Update(request):
#    person = About_me.objects.get(document='1014218980')
#    return render(request, 'layouts/edit_user.html', {'person': person})

# esta es la query para eliminar el registro contenido en la tabla de about_me, se deja comentariada pues no
# deberia ser necesaria de usar actualmente


#def Delete(request):
#    person = About_me.objects.filter(document='1014218980').delete()
#    return render(request, 'index.html', {'person': person})

