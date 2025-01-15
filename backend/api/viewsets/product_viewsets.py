from rest_framework import viewsets
from api.serializers.product_serializers import ProductSerializer
from product.models import ProductModel

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer