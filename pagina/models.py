from django.db import models

# Create your models here.
class Auto (models.Model):
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    color = models.CharField(max_length = 20)
    kilometros = models.IntegerField()
    
    def __str__(self) :
        return f"{self.marca.capitalize()}  {self.modelo.capitalize()} color {self.color} con {self.kilometros}KM"
