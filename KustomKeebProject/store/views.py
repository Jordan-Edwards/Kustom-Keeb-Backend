from django.http import Http404
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductByCategoryList(APIView):

    def filter_by_id(self, category_id):
        try:
            return Product.objects.filter(category_id=category_id)
        except category_id.DoesNotExist:
            raise Http404

    def get(self, request, category_id):
        category_id = self.filter_by_id(category_id)
        serializer = ProductSerializer(category_id, many=True)
        return Response(serializer.data)


class ProductList(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):

    def get(self, request, pk):
        print(pk)
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404
