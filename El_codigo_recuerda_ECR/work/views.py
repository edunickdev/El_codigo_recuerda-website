from django.shortcuts import render
from work.models import Employee


# Create your views here.
def Read(request):
    employee = Employee.objects.all()
    return render(request, 'work.html', {})
