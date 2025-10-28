from django.db import models

class Miembros(models.Model):
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    numero = models.IntegerField(null=True)
    fecha_union = models.DateField(null=True)

    def __str__(self):
        return f"({self.Nombre}{self.Apellido})"