import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProcessingRequest, Product
from .serializers import ProcessingRequestSerializer
from .tasks import process_images
from .utils import parse_csv

class UploadAPIView(APIView):
    def post(self, request):
        csv_file = request.FILES['file']
        request_id = str(uuid.uuid4())
        
        # Parse CSV
        products_data = parse_csv(csv_file)

        # Create ProcessingRequest and Product entries
        processing_request = ProcessingRequest.objects.create(request_id=request_id)
        for product_data in products_data:
            Product.objects.create(
                request=processing_request,
                serial_number=product_data['serial_number'],
                product_name=product_data['product_name'],
                input_image_urls=product_data['input_image_urls']
            )
        
        # Trigger asynchronous processing
        process_images.delay(request_id)

        return Response({'request_id': request_id}, status=status.HTTP_202_ACCEPTED)

class StatusAPIView(APIView):
    def get(self, request, request_id):
        try:
            processing_request = ProcessingRequest.objects.get(request_id=request_id)
        except ProcessingRequest.DoesNotExist:
            return Response({'error': 'Request ID not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProcessingRequestSerializer(processing_request)
        return Response(serializer.data)
