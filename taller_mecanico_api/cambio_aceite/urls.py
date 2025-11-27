from django.urls import path
from cambio_aceite.views.cambio_aceite import revision_cambio_aceite

urlpatterns = [
    path('revision/', revision_cambio_aceite, name='revision_cambio_aceite'),
]