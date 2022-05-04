from django.db import models


# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    km = models.CharField(max_length=150)
    valor = models.CharField(max_length=150)
