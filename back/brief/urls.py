from django.urls import path
from .views import FileUploadView, FileDetailView

urlpatterns = [
    # Upload files and get all files
    path('files/', FileUploadView.as_view(), name='file-upload'),
    
    # Get, delete specific file
    path('files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),
]

