from django.urls import path
from . import views

urlpatterns = [
    path('revision/', views.revision_cambio_aceite, name='revision_cambio_aceite'),
]