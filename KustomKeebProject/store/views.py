from django.http import Http404
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryList(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):

    def filter_by_id(self, category_id):
        try:
            return Product.objects.filter(category_id=category_id)
        except category_id.DoesNotExist:
            raise Http404

    def get(self, request, collection_id):
        collection_id = self.filter_by_id(collection_id)
        serializer = ProductSerializer(collection_id, many=True)
        return Response(serializer.data)


class CreateFlashcard(APIView):

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetails(APIView):

    def get(self, request, pk):
        print(pk)
        try:
            flashcard = Flashcard.objects.get(pk=pk)
            newthing = FlashcardSerializer(flashcard)
            return Response(newthing.data)
        except Flashcard.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        flashcard_id = Flashcard.objects.get(pk=pk)
        updateFlashcard = FlashcardSerializer(flashcard_id, data=request.data, partial=True)
        if updateFlashcard.is_valid():
            updateFlashcard.save()
            return Response(updateFlashcard.data, status=status.HTTP_202_ACCEPTED)
        return Response(updateFlashcard.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        flashcard_id = self.get_by_id(pk)
        deleteFlashcard = FlashcardSerializer(flashcard_id)
        flashcard_id.delete()
        return Response(deleteFlashcard.data, status=status.HTTP_200_OK)
