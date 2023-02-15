from django.urls import path
from . import views

urlpatterns = [
    path('', views.Read, name='Work_read')
]
