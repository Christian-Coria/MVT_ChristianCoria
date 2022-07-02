from django.db import models

class Parentezco(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad= models.CharField(max_length=40)
    parentezco= models.CharField(max_length=40)

class MisDatos(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad= models.IntegerField()
    telefono=models.IntegerField()
    email=models.EmailField()