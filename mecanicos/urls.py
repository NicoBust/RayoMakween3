<<<<<<< HEAD
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
=======
#from django.conf.urls import url

from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
>>>>>>> f3980110773089c3339abe54f03f1f97cba75c55
from . import views
from .views import image_list, image_create, image_update, image_delete, logout_view, galeria

urlpatterns = [
    path('', views.index, name="index"),
    path('qSomos/', views.qSomos, name="qSomos"),
    path('contacto/', views.contacto, name="contacto"),
<<<<<<< HEAD
    path('registro/', views.registro, name="registro"),
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('galeria/', galeria, name="galeria"),
    path('ultimoT1/', views.ultimoT1, name="ultimoT1"),
    path('ultimoT2/', views.ultimoT2, name="ultimoT2"),
    path('ultimoT3/', views.ultimoT3, name="ultimoT3"),
    path('carrito/', views.carrito_view, name="carrito"),
    path('producto_ampolleta/', views.producto_ampolleta, name="producto_ampolleta"),
    path('producto_panos/', views.producto_panos, name="producto_panos"),
    path('producto_plumillas/', views.producto_plumillas, name="producto_plumillas"),
    path('products/', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name="logout"),
    path('crud/', views.crud, name="crud"),
    path('images/', image_list, name='image_list'),
    path('images/add/', image_create, name='image_create'),
    path('images/update/<int:pk>/', image_update, name='image_update'),
    path('images/delete/<int:pk>/', image_delete, name='image_delete')
=======
    path('Ingreso/', views.Ingreso, name="Ingreso"),
    path('registro/', views.registro, name="registro"),
    path('galeria/', views.galeria, name="galeria"),
    path('galeria/', galeria, name='galeria'),
    path('ultimoT1/', views.ultimoT1, name="ultimoT1"),
    path('ultimoT2/', views.ultimoT2, name="ultimoT2"),
    path('ultimoT3/', views.ultimoT3, name="ultimoT3"),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),  # Redirige a 'index' después de cerrar sesión

    path('crud', views.crud, name="crud"),

    path('images/', image_list, name='image_list'),
    path('images/add/', image_create, name='image_create'),
    path('images/edit/<int:pk>/', image_update, name='image_update'),
    path('images/delete/<int:pk>/', image_delete, name='image_delete'),

    path('logout/', logout_view, name='logout'),
>>>>>>> f3980110773089c3339abe54f03f1f97cba75c55
]
