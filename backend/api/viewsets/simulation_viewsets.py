from rest_framework import viewsets
from api.serializers.simulation_serializers import SimulationSerializer
from simulation.models import SimulationModel

class SimulationViewSet(viewsets.ModelViewSet):
  
    queryset = SimulationModel.objects.all()
    serializer_class = SimulationSerializer