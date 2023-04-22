from django.urls import path

from .views import *

urlpatterns = [
    path('', BeNoteMain.as_view(), name='main'),
    path('newnote/', new_note, name='newnote'),
    path('notes/', notes, name='notes'),
    path('notepads/', notepads, name='notepads'),
    path('tasks/', tasks, name='tasks')
]