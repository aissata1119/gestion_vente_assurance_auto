from rest_framework import viewsets
from api.serializers.subscription_serializers import SubscriptionSerializer
from subscription.models import SubscriptionModel

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionModel.objects.all()
    serializer_class = SubscriptionSerializer