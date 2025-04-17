from rest_framework import serializers
from .models import File
import uuid


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['file_path']

    def create(self, validated_data):
        uploaded_file = validated_data['file_path']
        filename = uploaded_file.name

        file_instance = File.objects.create(
            file_name=filename,
            token=uuid.uuid4().hex,
            file_path=uploaded_file
        )
        return file_instance




