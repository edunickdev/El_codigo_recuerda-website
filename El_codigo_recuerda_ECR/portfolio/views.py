from django.shortcuts import render
from portfolio.models import *


# Create your views here.
def Read(request):
    works = Portfolio.objects.all()
    return render(request, 'portfolio.html', {})
