from django.shortcuts import render
from .models import Product
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer
# Create your views here.


class ProductAPI(APIView):

    def get(self, request):
        products = Product.objects.prefetch_related('categories').all()
        
        return Response(ProductSerializer(products, many=True).data)
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, pk=None):

        product = Product.objects.prefetch_related('comments').filter(pk=pk).first()
        print(product.comments.all())
        return Response(ProductSerializer(product).data)