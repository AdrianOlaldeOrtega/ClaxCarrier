import email
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    urlImagen = models.TextField(max_length=200, null = True)
    stock = models.IntegerField()

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100)
    apellidoCliente = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Domicilio = models.CharField(max_length=150)
    infoAdicional = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigoPostal = models.CharField(max_length=5)

class ArticuloVendido(models.Model):
    folioVenta = models.IntegerField()
    articulo = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

class Venta(models.Model):
    total = models.FloatField()
    idCliente = models.IntegerField()
    fechaRealizada = models.DateField(null=True)
    formaPago = models.CharField(max_length=30)
    nombrePropietario = models.CharField(max_length=100)
    numeroTarjeta = models.CharField(max_length=16)
    vencimiento = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    status = models.CharField(max_length=20)
