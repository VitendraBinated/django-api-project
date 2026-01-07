from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

from django.db.models import Sum
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer




@api_view(['GET'])
def external_posts(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return Response(response.json()[:5])



@api_view(['GET'])
def product_summary_report(request):
    data = {
        "total_products": Product.objects.count(),
        "total_quantity": Product.objects.aggregate(
            total=Sum('quantity')
        )['total'] or 0,
        "total_inventory_value": Product.objects.aggregate(
            total=Sum('price')
        )['total'] or 0
    }
    return Response(data)


