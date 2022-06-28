from django.db import models


# Create your models here.

class Family(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_de_nac=models.DateField()

class VideoCards(models.Model):
    marca= models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    memoria=models.IntegerField()

class Prueba(models.Model):
    cambioNombre=models.CharField(max_length=10)
    prueba2=models.CharField(max_length=10)

class VideoJuegos(models.Model):
    nombre_del_juego=models.CharField(max_length=10)
    tipo_de_Juego= models.CharField(max_length=10)
    espacio_en_disco=models.IntegerField()
    fecha_lanzamiento=models.DateField()


    

    

