from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('newnote/', views.new_note, name = 'newnote')
]