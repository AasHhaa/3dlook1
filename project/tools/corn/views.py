from . import models, serializers
from rest_framework import generics
from .pagination import StandardResultsSetPagination


# This endpoint provides the ability to create Product or get them all
class ProductView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return models.Product.objects.all()


# This endpoint provides the ability to get\put\patch\delete Product by id
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = StandardResultsSetPagination