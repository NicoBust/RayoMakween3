from django.shortcuts import render # type: ignore
#from django.http import HttpResponse

# Create your views here.
TEMPLATE_DIRS = (
    'OS.PATH.JOIN(base_dir, "TEMPLATES),'
)

def index (request) :
    #context = { }
    return render(request, "index.html")

def qSomos (request) :
    #context = { }
    return render(request, "qSomos.html")

def contacto (request) :
    #context = { }
    return render(request, "contacto.html")

def Ingreso (request) :
    #context = { }
    return render(request, "Ingreso.html")

def registro (request) :
    #context = { }
    return render(request, "registro.html")

def galeria (request) :
    #context = { }
    return render(request, "galeria.html")

def ultimoT1 (request) :
    #context = { }
    return render(request, "ultimoT1.html")

def ultimoT2 (request) :
    #context = { }
    return render(request, "ultimoT2.html")

def ultimoT3 (request) :
    #context = { }
    return render(request, "ultimoT3.html")

#registro django
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('index')  # Asegúrate de que esta sea la URL correcta para tu página de inicio
        else:
            messages.error(request, 'Registro fallido. Información inválida.')
    else:
        form = RegisterForm()
    return render(request, 'registro.html', {'form': form})