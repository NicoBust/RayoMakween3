from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.contrib.auth import logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponse # type: ignore
from .models import ImageEntry
from .forms import ImageEntryForm

# Create your views here.
#TEMPLATE_DIRS = (
#    'OS.PATH.JOIN(base_dir, "TEMPLATES),'
#)

def index (request) :
    latest_images = ImageEntry.objects.order_by('-id')[:3]  # Obtiene las 3 últimas imágenes
    #context = { }
    return render(request, 'index.html', {'latest_images': latest_images})

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

def crud (request):
    cliente = cliente.objects.all()
    context = {'cliente': cliente}
    return render (request, 'eliminarU.html', context)

#vista para manejar
@login_required
def image_list(request):
    images = ImageEntry.objects.all()
    return render(request, 'image_list.html', {'images': images})

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageEntryForm(request.POST, request.FILES)
        if form.is_valid():
            materials = request.POST.getlist('materials')
            image_entry = form.save(commit=False)
            image_entry.materials = ','.join(materials)
            image_entry.save()
            return redirect('image_list')
    else:
        form = ImageEntryForm()
    return render(request, 'image_form.html', {'form': form})

@login_required
def image_update(request, pk):
    image = get_object_or_404(ImageEntry, pk=pk)
    if request.method == 'POST':
        form = ImageEntryForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            materials = request.POST.getlist('materials')
            image_entry = form.save(commit=False)
            image_entry.materials = ','.join(materials)
            image_entry.save()
            return redirect('image_list')
    else:
        form = ImageEntryForm(instance=image)
    return render(request, 'image_form.html', {'form': form})

@login_required
def image_delete(request, pk):
    image = get_object_or_404(ImageEntry, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'image_confirm_delete.html', {'image': image})

def logout_view(request):
    logout(request)
    return redirect('index')

#registro django
# views.py
#from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib import messages
#from .forms import RegisterForm

#def register(request):
#    if request.method == 'POST':
#        form = RegisterForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            login(request, user)
#            messages.success(request, 'Registro exitoso.')
#            return redirect('index')  # Asegúrate de que esta sea la URL correcta para tu página de inicio
#        else:
#            messages.error(request, 'Registro fallido. Información inválida.')
#    else:
#        form = RegisterForm()
#    return render(request, 'registro.html', {'form': form})