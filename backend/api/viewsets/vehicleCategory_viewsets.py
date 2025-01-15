from rest_framework import viewsets
from api.serializers.vehicleCategory_serializers import VehicleCategorySerializer
from vehicleCategory.models import VehicleCategoryModel

class VehicleCategoryViewSet(viewsets.ModelViewSet):
    queryset = VehicleCategoryModel.objects.all()
    serializer_class = VehicleCategorySerializer