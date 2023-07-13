from django.urls import path

from .views import *

urlpatterns = [
    path('', BeNoteMain.as_view(), name='main'),
    path('newnote', New_note, name='newnote'),
    path('notes', notes, name='notes'),
    path('login',Login_user.as_view(), name='login'),
    path('registration', UserRegister.as_view(), name='registration'),
    path('logout', Logout.as_view(), name='logout'),
    path('check_note/<int:post_id>', Check_note, name='check_note'),
    path('basket', Basket, name='basket'),
    path('delete_note/<int:post_id>', delete_note, name='delete_note'),
    path('basket/check_trash_note/<int:post_id>', Check_trash_note, name ='check_trash_note'),
    path('basket/delete_trash_note/<int:post_id>', delete_trash_note, name='delete_trash_note'),
    path('basket/clear_basket', clear_basket, name='clear_basket'),
    path('tasks', tasks, name='tasks'),
    path('tasks/complete_task/<int:task_id>', complete_task, name='complete_task'),
]