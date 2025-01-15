from rest_framework import serializers
from garantee.models import GaranteeModel

class GaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaranteeModel
        fields = "__all__"