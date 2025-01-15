from rest_framework import serializers
from vehicleCategory.models import VehicleCategoryModel

class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategoryModel
        fields = "__all__"