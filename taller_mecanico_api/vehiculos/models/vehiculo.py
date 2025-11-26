from django.db import models
from .category import Category

class Vehiculo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="vehiculos")
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=140)
    modelo = models.CharField(max_length=140)
    anio = models.PositiveIntegerField()    
    color = models.CharField(max_length=140)
    tipo = models.CharField(max_length=140)
    kilometraje = models.PositiveIntegerField()
    nombre_propietario = models.CharField(max_length=140)
    telefono_propietario = models.CharField(max_length=140)
    estado = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        unique_together = ("category", "placa")
        ordering = ("-created_at",)

    def __str__(self):
        return self.name