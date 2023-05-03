from django import forms
from .models import *

class Add_newnote_form(forms.ModelForm):
   class Meta:
        model = Content
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'named'}),
            'text': forms.Textarea(attrs={'class': 'input_text'}),
        }

class Registration_form(forms.Form):
    user_first_name = forms.CharField(max_length=255, label="Имя")
    user_last_name = forms.CharField(max_length=255, label="Фимилия")
    user_nickname = forms.CharField(max_length=255, label="Никнейм")
    user_password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class Logit_form(forms.Form):
    pass