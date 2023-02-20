from django.urls import path
from . import views

urlpatterns = [
    path('', views.Read, name='portfolio_read')
]
