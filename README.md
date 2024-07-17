# Image Processing System

## Overview

This project is a Django-based system designed to process image data from CSV files. The system validates the CSV data, compresses the images by 50% of their original quality, stores the processed images along with their product information, and provides APIs to upload CSV files and check the processing status.

## Features

- **Upload API**: Accepts CSV files, validates the formatting, and returns a unique request ID.
- **Status API**: Allows users to query processing status using the request ID.
- **Image Processing**: Asynchronously compresses images to 50% of their original quality.
- **Webhook Handling**: Triggers a webhook endpoint after processing all images.
- **Database Storage**: Stores processed image data and associated product information.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Asynchronous Task Queue**: Celery
- **Message Broker**: Redis
- **Database**: SQLite (can be switched to any other SQL database)

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Celery
- Redis
- Pillow (for image processing)
- pandas (for CSV handling)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd image_processing_project
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Redis**:
    - Download and install Redis from [Redis.io](https://redis.io/download).
    - Start the Redis server.

5. **Configure Celery**:
    Ensure that the `CELERY_BROKER_URL` in `settings.py` is set to `redis://localhost:6379/0`.

6. **Run database migrations**:
    ```sh
    python manage.py migrate
    ```

## Usage

### Running the Server

1. **Start the Django server**:
    ```sh
    python manage.py runserver
    ```

2. **Start the Celery worker**:
    ```sh
    celery -A image_processing_project worker --loglevel=info
    ```

### Testing the APIs with Postman

1. **Upload API**:
    - URL: `http://127.0.0.1:8000/api/upload-csv/`
    - Method: `POST`
    - Body: Form-data
        - Key: `file`
        - Value: (Select your CSV file)

2. **Status API**:
    - URL: `http://127.0.0.1:8000/api/check-status/<request_id>/`
    - Method: `GET`

### Sample CSV Format

```csv
S. No.,Product Name,Input Image Urls
1,SKU1,https://www.public-image-url1.jpg,https://www.public-image-url2.jpg,https://www.public-image-url3.jpg
2,SKU2,https://www.public-image-url4.jpg,https://www.public-image-url5.jpg,https://www.public-image-url6.jpg
