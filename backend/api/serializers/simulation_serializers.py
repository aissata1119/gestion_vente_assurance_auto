from rest_framework import serializers
from simulation.models import SimulationModel

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationModel
        fields = "__all__"