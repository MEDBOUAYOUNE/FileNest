from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid
import os

class File(models.Model):
    file_id = models.UUIDField(primary_key=True, editable=False)
    file_name = models.CharField(max_length=200, blank=False, editable=False)
    encrypted_data = models.BinaryField() 
    encrypted_key = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # expires_at = models.DateTimeField(null=False, blank=False, editable=False)
    # download_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.file_id
    