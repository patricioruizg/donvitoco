from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'carta.html')




def inicio(request):
    return render(request, 'index.html')

def usuarios(request):
    form_class=UsuarioForm
    formulario=form_class(request.POST or None)

    if request.method == 'POST':
       

        if formulario.is_valid():
            formulario.save()

    else:
       pass

    lista =usuario.objects.all()
    context={'form':formulario,
           'lista':lista, }
    return render(request, 'usuarios.html',context)

def orden(request):
    form_class=productoForm
    formulario=form_class(request.POST or None)

    if request.method == 'POST':
       

        if formulario.is_valid():
            formulario.save()

    else:
       pass

    lista =producto.objects.all()
    form={'form':formulario,
           'lista':lista, }

    return render(request, 'orden.html',form)

def register(request):
    data = {
        'form':UserCreationForm()
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)

            
            
            return redirect('inicio')
        data["form"] = formulario

    return render(request, 'registration/register.html', data)

