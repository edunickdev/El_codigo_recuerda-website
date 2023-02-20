from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def Read(request):
    works = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'works': works})
