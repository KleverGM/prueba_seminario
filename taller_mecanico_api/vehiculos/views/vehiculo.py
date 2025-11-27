from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer
from vehiculos.pagination import StandardResultsSetPagination

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.select_related("category").all()
    serializer_class = VehiculoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("placa","marca","modelo","category__name")
    ordering_fields = ("created_at","placa","marca")

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category__id=category)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            vehiculo = serializer.save()
            return Response({
                'mensaje': 'Vehículo registrado exitosamente',
                'vehiculo': VehiculoSerializer(vehiculo).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'mensaje': 'Error al registrar el vehículo',
            'errores': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            vehiculo = serializer.save()
            return Response({
                'mensaje': 'Vehículo actualizado exitosamente',
                'vehiculo': VehiculoSerializer(vehiculo).data
            })
        return Response({
            'mensaje': 'Error al actualizar el vehículo',
            'errores': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        placa = instance.placa
        self.perform_destroy(instance)
        return Response({
            'mensaje': f'Vehículo con placa {placa} eliminado exitosamente'
        })