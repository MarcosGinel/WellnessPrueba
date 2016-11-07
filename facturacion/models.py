# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model

class PrecioDiario(Model):
    fecha = models.DateField(blank=False)
    precio = models.DecimalField(blank=False, max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.fecha)

class ConsumoDiario(Model):
    fecha = models.ForeignKey(PrecioDiario, unique=True)
    usuario = models.ForeignKey(User)
    cantidad = models.DecimalField(blank=False, max_digits=5, decimal_places=2)

