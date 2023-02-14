from django.shortcuts import render
from django.http import HttpResponse
from .models import About_me


# Create your views here.
def home(request):
    return render(request, 'layouts/base.html', {})


def start(request):
    register = About_me.objects.all()
    return render(request, 'index.html', {'register': register})

# esta es la query para eliminar el registro contenido en la tabla de about_me, se deja comentariada pues no
# deberia ser necesaria de usar actualmente

# def Delete(request):
#    enough = About_me.objects.get(document='1014218980')
#    enough.delete()
#    return render(request, 'index.html', {'enough': enough})
