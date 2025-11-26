from rest_framework import viewsets, filters
from vehiculos.models import Category
from vehiculos.serializers import CategorySerializer # type: ignore

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)
    ordering_fields = ("name","created_at")