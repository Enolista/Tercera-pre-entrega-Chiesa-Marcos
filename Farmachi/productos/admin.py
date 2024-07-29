from django.contrib import admin
from productos.models import Producto,Vendedor,Cliente

# Register your models here.
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Cliente)