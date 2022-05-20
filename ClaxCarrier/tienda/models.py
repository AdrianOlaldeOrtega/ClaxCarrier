from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    urlImagen = models.TextField(max_length=200, null = True)
    stock = models.IntegerField()