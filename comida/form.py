from django.forms import ModelForm
from .models import *
from django.forms import widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
  pass

class productoForm(ModelForm):
    class Meta:
        model=producto 
        fields=['nombre',
        'precio',
         ]
      
class UsuarioForm(ModelForm):
    class Meta:
        model=usuario 
        fields='__all__'