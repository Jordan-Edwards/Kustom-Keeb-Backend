from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'created_by',
            'title',
            'description',
            'image',
            'slug',
            'price',
            'in_stock',
            'created',
            'updated',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]
