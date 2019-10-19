from django.db import models

# Create your models here.

marcas = [
    ('Nissan', 'Nissan'),
    ('Toyota', 'Toyota'),
    ('Subaru', 'Subaru'),
    ('Mazda', 'Mazda'),
    ('Honda', 'Honda'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Datsun', 'Datsun'),
]


class Vehiculo(models.Model):
    marca = models.CharField(max_length=20,choices=marcas)
    year = models.IntegerField()
    modelo = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    precio= models.IntegerField()
    vendido= models.BooleanField()
    imgFront= models.ImageField()
    imgSide= models.ImageField()
    imgBack= models.ImageField()
    imgInside= models.ImageField()

