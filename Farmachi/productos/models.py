from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    cantidad = models.IntegerField()
    precio = models.FloatField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Codigo: {self.codigo} - Cantidad: {self.cantidad} - Precio: {self.precio}"
        

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI:{self.dni} - Email: {self.email}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI:{self.dni} - Email: {self.email}"