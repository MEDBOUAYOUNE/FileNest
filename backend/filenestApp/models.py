from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid
import os

def get_upload_path(instance, filename):
    """Generate a unique file path with UUID to prevent filename collisions"""
    unique_filename = f"{instance.token}{filename}"
    return os.path.join('uploads', unique_filename)

class File(models.Model):
    file_name = models.CharField(max_length=200, blank=False, null=False, editable=False)
    token = models.CharField(max_length=64, unique=True, editable=False)
    file_path = models.FileField(upload_to=get_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # expires_at = models.DateTimeField(null=False, blank=False, editable=False)
    # download_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.file_name
    