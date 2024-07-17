# image_processing_app/models.py
from django.db import models

class ProcessingRequest(models.Model):
    request_id = models.CharField(max_length=36, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

class Product(models.Model):
    request = models.ForeignKey(ProcessingRequest, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    product_name = models.CharField(max_length=255)
    input_image_urls = models.TextField()  # Comma-separated URLs
    output_image_urls = models.TextField(blank=True, null=True)  # Comma-separated URLs
