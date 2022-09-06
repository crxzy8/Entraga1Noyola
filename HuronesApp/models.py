from django.db import models

class hurones(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    raza=models.CharField(max_length=30)

class comida(models.Model):
    tipo=models.CharField(max_length=30)
    proteinas=models.IntegerField()

class accesorio(models.Model):
    tipo=models.CharField(max_length=30)
    precio=models.IntegerField()
    colores=models.CharField(max_length=30)