from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import *

menu = [{'title': 'Добавить заметку', 'url': 'newnote'},
        {'title': 'Мои заметки', 'url': 'notes'},
        {'title': 'Задачи', 'url': 'tasks'},
        {'title': 'Блокноты', 'url': 'notepads'},
]

from .models import *

class BeNoteMain(ListView):
    model = Content
    template_name = 'main/base.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить записку'
        return context

class New_note(ListView):
    model = Content
    template_name = 'main/newnote.html'
    def  get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = Add_newnote_form()
        context['menu'] = menu
        context['title'] = 'Добавить записку'
        context['form'] = form
        return context

def notes(request):
    content = Content.objects.all()
    return render(request, 'main/notes.html', {'menu': menu, 'title': 'Мои заметки', 'content': content})

def notepads(request):
    return render(request, 'main/notepads.html', {'menu': menu, 'title': 'Блокноты'})

def tasks(request):
    return render(request, 'main/tasks.html', {'menu': menu, 'title': 'Задачи'})


def login(request):
    return render(request, 'main/login.html', {'menu': menu, 'title': 'Задачи'})

class UserRegister(ListView):
    model = Content
    template_name = 'main/registration.html'
    def  get_context_data(self, *, object_list=None, **kwargs):
        form = Registration_form()
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить записку'
        context['form'] = form
        return context


