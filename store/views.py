from django.db.models import query_utils
from django.shortcuts import get_object_or_404, render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer

from rest_framework.generics import CreateAPIView

from store import models

class all_products(APIView):
     def get(self, request):
         products = Product.objects.all()
         Serializer = ProductSerializer(products, many=True)
         return Response(Serializer.data)

class productView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class categoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

'''
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/home.html',{'product': product})
'''
class product_detail(APIView):
    
    def get(self, request, slug):
        product = Product.objects.filter(slug=slug)
        Serializer = ProductSerializer(product, many=True)
        return Response(Serializer.data)

class createProductAPIView(CreateAPIView):
    querysset = Product.objects.all()
    serializer_class = ProductSerializer
