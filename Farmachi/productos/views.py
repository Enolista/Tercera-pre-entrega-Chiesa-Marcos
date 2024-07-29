from django.shortcuts import render
from django.http import HttpResponse
#from .models import Producto
#from django.views.generic import ListView
from productos.models import Producto, Vendedor, Cliente
from productos.forms import FormularioProducto, BusquedaProducto, FormularioVendedor, BusquedaVendedor, FormularioCliente, BusquedaCliente


# Create your views here.
def inicio(request):
    return render(request, 'productos/index.html')


def listaProductos(request):
    productos = Producto.objects.all()
    # dejarlo siempre aca y me ahorro hacer el shell con este veo si me trajo o no algo del modelo
    #print(productos)  
    context = {'productos': productos}
    return render(request, 'productos/listaProductos.html', context)

    #nombre = forms.CharField(max_length=40)
    #codigo = forms.IntegerField()
    #cantidad = forms.IntegerField()
    #precio = forms.FloatField()

def formularioProductos(request):
    if request.method == "POST":
        mi_formulario = FormularioProducto(request.POST) 
        # Veo si llego la info del formulario
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            producto = Producto(nombre=informacion["nombre"], codigo=informacion["codigo"], cantidad=informacion["cantidad"], precio=informacion["precio"])
            producto.save()

            return render(request, "productos/index.html")
    else:
        mi_formulario = FormularioProducto()

    return render(request, "productos/formularioProductos.html", {"mi_formulario": mi_formulario})


def busquedaProductos(request):
    if request.method == "POST":
        mi_formulario = BusquedaProducto(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            productos = Producto.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "productos/mostrarProductos.html", {"productos": productos})
    else:
        mi_formulario = BusquedaProducto()

    return render(request, "productos/busquedaProductos.html", {"mi_formulario": mi_formulario})

   #nombre = models.CharField(max_length=40)
   # apellido = models.CharField(max_length=40)
   # dni = models.IntegerField()
   # email = models.EmailField()


def listaVendedores(request):
    vendedores = Vendedor.objects.all()
    # dejarlo siempre aca y me ahorro hacer el shell con este veo si me trajo o no algo del modelo
    #print(vendedores)  
    context = {'vendedores': vendedores}
    return render(request, 'productos/listaVendedores.html', context)

def formularioVendedores(request):
    if request.method == "POST":
        mi_formulario = FormularioVendedor(request.POST) 
        # Veo si llego la info del formulario
        # print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            vendedor = Vendedor(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"])
            vendedor.save()

            return render(request, "productos/index.html")
    else:
        mi_formulario = FormularioVendedor()

    return render(request, "productos/formularioVendedores.html", {"mi_formulario": mi_formulario})


def busquedaVendedores(request):
    if request.method == "POST":
        mi_formulario = BusquedaVendedor(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            vendedores = Vendedor.objects.filter(apellido__icontains=informacion["apellido"])

            return render(request, "productos/mostrarVendedores.html", {"vendedores": vendedores})
    else:
        mi_formulario = BusquedaVendedor()

    return render(request, "productos/busquedaVendedores.html", {"mi_formulario": mi_formulario})

   #nombre = models.CharField(max_length=40)
   # apellido = models.CharField(max_length=40)
   # dni = models.IntegerField()
   # email = models.EmailField()


def listaClientes(request):
    clientes = Cliente.objects.all()
    # dejarlo siempre aca y me ahorro hacer el shell con este veo si me trajo o no algo del modelo
    #print(clientes)  
    context = {'clientes': clientes}
    return render(request, 'productos/listaClientes.html', context)


def formularioClientes(request):
    if request.method == "POST":
        mi_formulario = FormularioCliente(request.POST) 
        # Veo si llego la info del formulario
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"])
            cliente.save()

            return render(request, "productos/index.html")
    else:
        mi_formulario = FormularioCliente()

    return render(request, "productos/formularioClientes.html", {"mi_formulario": mi_formulario})


def busquedaClientes(request):
    if request.method == "POST":
        mi_formulario = BusquedaCliente(request.POST) 
        # print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            clientes = Cliente.objects.filter(apellido__icontains=informacion["apellido"])
            #print(informacion)
            return render(request, "productos/mostrarClientes.html", {"clientes": clientes})
    else:
        mi_formulario = BusquedaCliente()

    return render(request, "productos/busquedaClientes.html", {"mi_formulario": mi_formulario})