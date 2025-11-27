from django.urls import path
from reparaciones.views.reparacion import calcular_costo_total

urlpatterns = [
    path('costo-total/', calcular_costo_total, name='calcular_costo_total'),
]