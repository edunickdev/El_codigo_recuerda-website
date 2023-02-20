from django.urls import path
from . import views

urlpatterns = [
	path('', views.read, name='my-blog_read')
]
