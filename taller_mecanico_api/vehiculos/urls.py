from rest_framework.routers import DefaultRouter
from vehiculos.views.category import CategoryViewSet
from vehiculos.views.vehiculo import VehiculoViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')

urlpatterns = router.urls