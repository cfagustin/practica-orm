from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre + '' + str(self.edad)


class Vehiculo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='vehiculo_persona')
    marca = models.CharField(max_length=25)
    modelo = models.PositiveIntegerField()

    def __str__(self):
        return self.marca + '' +str(self.modelo)


class Servicio (models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='servicio_vehiculo')
    nombre_servicio = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()


    def __str__(self):
        return self.nombre_servicio + '' + str(self.precio)


