from rest_framework import serializers
from vehiculos.models import Vehiculo, Category

class VehiculoSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Vehiculo
        fields = ("id","placa","marca","modelo","anio","color","tipo","kilometraje","nombre_propietario","telefono_propietario","estado",
                  "category_id","category_name","created_at","updated_at")
        read_only_fields = ("id","created_at","updated_at","category_name")