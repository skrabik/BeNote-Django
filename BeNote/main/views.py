from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import logout, login

menu = [{'title': 'Добавить заметку', 'url': 'newnote'},
        {'title': 'Мои заметки', 'url': 'notes'},
        #{'title': 'Задачи', 'url': 'tasks'},
        #{'title': 'Блокноты', 'url': 'notepads'},
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


# class New_note(CreateView):
#     # def get_user_id(self):
#     #     user_id = self.request.user.id
#     #     return user_id
#
#     form_class = Add_newnote_form
#     template_name = 'main/newnote.html'
#     success_url = reverse_lazy('main')
#     def  get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Добавить записку'
#         return context

def New_note(request):
    if request.method == 'POST':
        form =Add_newnote_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = Add_newnote_form()
    return render(request, "main/newnote.html", context={'form': form, 'menu': menu, 'title': "Добавить заметку"})


def notes(request):
    content = Content.objects.filter(user_id=request.user.id)
    return render(request, 'main/notes.html', {'menu': menu, 'title': 'Мои заметки', 'content': content})

class Login_user(LoginView):
    form_class = Login_form
    template_name = "main/login.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Войти'
        return context
    def get_success_url(self):
        return reverse_lazy('main')


class UserRegister(CreateView):
    form_class = Registration_form
    template_name = 'main/registration.html'
    #success_url = reverse_lazy('login')
    def  get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить записку'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

# def tasks(request):
#     return render(request, 'main/tacks.html', {'menu': menu, 'title': 'Мои заметки'})
#
# def notepads(request):
#     return render(request, 'main/tacks.html', {'menu': menu, 'title': 'Мои заметки'})

# def logout_user(request):
#     logout(request)
#     return reverse_lazy('main')


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('main')
