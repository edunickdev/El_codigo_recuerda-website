from django.urls import path
from . import views

urlpatterns = [
	#    path('create/', views.Create, name='create'),
	path('', views.Read, name='about-me_read'),
	#    path('update/', views.Update, name='update'),
	#    path('delete/', views.Delete, name='delete')
]
