from django.urls import path
from . import views

urlpatterns = [
    path('', views.Read, name='education_read')
]
