from celery import shared_task
from .models import ProcessingRequest, Product
from .utils import compress_image

@shared_task
def process_images(request_id):
    processing_request = ProcessingRequest.objects.get(request_id=request_id)
    products = Product.objects.filter(request=processing_request)
    
    for product in products:
        input_urls = product.input_image_urls.split(',')
        output_urls = []
        
        for url in input_urls:
            output_url = compress_image(url)  # Compress image and get output URL
            output_urls.append(output_url)
        
        product.output_image_urls = ','.join(output_urls)
        product.save()
    
    processing_request.status = 'completed'
    processing_request.save()
