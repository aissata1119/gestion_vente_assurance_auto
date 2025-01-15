from rest_framework import viewsets
from api.serializers.user_serializers import UserSerializer
from user.models import UserModel

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer