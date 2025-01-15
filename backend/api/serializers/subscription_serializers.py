from rest_framework import serializers
from subscription.models import SubscriptionModel

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionModel
        fields = "__all__"