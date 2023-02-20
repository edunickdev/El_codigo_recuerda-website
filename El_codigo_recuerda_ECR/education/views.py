from django.shortcuts import render
from .models import Education


# Create your views here.
def Read(request):
    course = Education.objects.all()
    return render(request, 'education.html', {'course': course})
