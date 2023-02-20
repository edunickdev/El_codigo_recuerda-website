from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def read(request):
	return HttpResponse('Blog is building')
