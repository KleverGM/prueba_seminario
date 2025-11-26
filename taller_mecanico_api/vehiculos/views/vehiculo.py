from rest_framework import viewsets, filters
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer
from vehiculos.pagination import StandardResultsSetPagination

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.select_related("category").all()
    serializer_class = VehiculoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name","category__name")
    ordering_fields = ("created_at","name")

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category__id=category)
        return qs