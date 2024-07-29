from django.urls import path
from productos import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("listaProductos/", views.listaProductos, name="ListaProductos"),
    path('formularioProductos/', views.formularioProductos, name="FormularioProductos"),
    path("busquedaProductos/", views.busquedaProductos, name="BusquedaProductos"),
    path("listaVendedores/", views.listaVendedores, name="ListaVendedores"),
    path('formularioVendedores/', views.formularioVendedores, name="FormularioVendedores"),
    path("busquedaVendedores/", views.busquedaVendedores, name="BusquedaVendedores"),
    path("listaClientes/", views.listaClientes, name="ListaClientes"),
    path('formularioClientes/', views.formularioClientes, name="FormularioClientes"),
    path("busquedaClientes/", views.busquedaClientes, name="BusquedaClientes"),
]