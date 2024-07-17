import csv
import requests
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def parse_csv(file):
    products = []
    csv_reader = csv.DictReader(file.read().decode('utf-8').splitlines())
    for row in csv_reader:
        products.append({
            'serial_number': row['S. No.'],
            'product_name': row['Product Name'],
            'input_image_urls': row['Input Image Urls']
        })
    return products

def compress_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    output = BytesIO()
    img.save(output, format='JPEG', quality=50)
    output.seek(0)
    
    file_name = f"compressed_images/{url.split('/')[-1]}"
    saved_file_name = default_storage.save(file_name, ContentFile(output.read()))
    
    return default_storage.url(saved_file_name)
