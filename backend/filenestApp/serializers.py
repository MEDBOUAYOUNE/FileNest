from cryptography.fernet import Fernet
from django.conf import settings
from .models import File
from rest_framework import serializers
import os

class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    
    class Meta:
        model = File
        fields = ['file']
        
    def create(self, validated_data):
        uploaded_file = validated_data['file']
        filename = uploaded_file.name
        file_content = uploaded_file.read()
        
        if not isinstance(file_content, bytes):
            file_content = file_content.encode()
        
        file_key = Fernet.generate_key()
        cipher = Fernet(file_key)
        
        encrypted_data = cipher.encrypt(file_content)
        master_key = settings.FILE_ENCRYPTION_MASTER_KEY

        if isinstance(master_key, str):
            master_key = master_key.encode()
            
        master_cipher = Fernet(master_key)
        encrypted_file_key = master_cipher.encrypt(file_key)
        
        file_instance = File.objects.create(
            file_id = uuid.uuid4(),
            file_name=filename,
            encrypted_data=encrypted_data,
            encrypted_key=encrypted_file_key,
        )
        return file_instance



