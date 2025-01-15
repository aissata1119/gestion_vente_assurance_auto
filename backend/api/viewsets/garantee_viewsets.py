from rest_framework import viewsets
from api.serializers.garantee_serializers import GaranteeSerializer
from garantee.models import GaranteeModel

class GaranteeViewSet(viewsets.ModelViewSet):
  
    queryset = GaranteeModel.objects.all()
    serializer_class = GaranteeSerializer