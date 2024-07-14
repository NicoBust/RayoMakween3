#from django.conf.urls import url

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('qSomos/', views.qSomos, name="qSomos"),
    path('contacto/', views.contacto, name="contacto"),
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('registro/', views.registro, name="registro"),
    path('galeria/', views.galeria, name="galeria"),
    path('ultimoT1/', views.ultimoT1, name="ultimoT1"),
    path('ultimoT2/', views.ultimoT2, name="ultimoT2"),
    path('ultimoT3/', views.ultimoT3, name="ultimoT3"),
]