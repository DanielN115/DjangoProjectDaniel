from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=255)
    mapa = models.ImageField(upload_to='region_maps/', null=True, blank=True)
    pueblo_inicial = models.CharField(max_length=255)
    lider_liga = models.ForeignKey('Entrenador', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre

class Pokemon(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    altura = models.FloatField()
    peso = models.FloatField()
    habilidad = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='pokemones')

    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='entrenador_images/', null=True, blank=True)

    def __str__(self):
        return self.nombre

