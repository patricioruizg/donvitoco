from django.db import models

# Create your models here.

class usuario(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)

class cliente(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    correo=models.EmailField()
    telefono=models.IntegerField()

class pedido(models.Model):
    fechaPedido=models.CharField(max_length=50)
    nombreCliente=models.CharField(max_length=50)
    tipoEntrega=models.CharField(max_length=50)

class carrito(models.Model):
    fecha=models.DateField()

class administrado(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    password=models.CharField(max_length=50)