from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class Add_newnote_form(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'named'}),
            'text': forms.Textarea(attrs={'class': 'input_text'}),
        }



class Registration_form(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': ''}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': ''}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': ''}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': ''}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Login_form(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


