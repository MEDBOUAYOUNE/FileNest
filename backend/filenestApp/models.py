from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=100, blank=False, null=False)
    token = models.CharField(max_length=64, unique=True)
    uploaded_to = models.FileField(upload_to=) #overide a func upload_to to genrate uuid/file_name
    uploaded_at = models.DateTimeField(auto_now_add=True)

