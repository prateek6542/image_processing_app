# image_processing_app/serializers.py
from rest_framework import serializers
from .models import ProcessingRequest, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProcessingRequestSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ProcessingRequest
        fields = '__all__'
