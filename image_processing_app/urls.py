from django.urls import path
from .views import UploadAPIView, StatusAPIView

urlpatterns = [
    path('upload/', UploadAPIView.as_view(), name='upload'),
    path('status/<str:request_id>/', StatusAPIView.as_view(), name='status'),
]
