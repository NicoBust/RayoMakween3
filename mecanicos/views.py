from django.shortcuts import render

# Create your views here.

#index django
def index(request):
    context={}
    return render(request, 'mecanicos/index.html', context)




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


