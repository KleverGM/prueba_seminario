from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vehiculos.urls')),
    path('reparaciones/', include('reparaciones.urls')),
    path('cambio-aceite/', include('cambio_aceite.urls')),
]