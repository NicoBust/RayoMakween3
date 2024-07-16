from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls import include # type: ignore
#from mecanicos import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mecanicos.urls')),
]
