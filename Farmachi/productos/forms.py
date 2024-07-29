from django import forms

class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    cantidad = forms.IntegerField()
    precio = forms.FloatField()

class BusquedaProducto(forms.Form):
    nombre = forms.CharField()
    

class FormularioVendedor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    
class BusquedaVendedor(forms.Form):
    apellido = forms.CharField()


class FormularioCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    
class BusquedaCliente(forms.Form):
    apellido = forms.CharField()
