from django.db import models


class Participaciones(models.Model):
    nombre = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    organizador = models.CharField(max_length=255)
    posicion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.posicion}'
