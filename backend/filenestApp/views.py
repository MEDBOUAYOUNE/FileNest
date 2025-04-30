# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileUploadSerializer
from django.conf import settings
from cryptography.fernet import Fernet
import uuid
from django.http import HttpResponse

class FileUploadView(APIView):
     def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            return Response({
                "message": "File uploaded successfully.",
                "file_id": file_instance.file_id,
                # "file_path" : file_instance.file_path.url,
                # "uploaded_at": file_instance.uploaded_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DownloadFileView(APIView):
    def get(self, request, file_id):
        try:
            # print(type(file_id))
            # if not isinstance(file_id, uuid.UUID):
            # file_id = uuid.UUID(file_id)
                # file_id = uuid.UUID(file_id)
            if File.objects.filter(file_id=file_id).exists():
                file_instance = File.objects.get(file_id=file_id)
                master_key = settings.FILE_ENCRYPTION_MASTER_KEY
                master_cipher = Fernet(master_key)
                
                file_key = master_cipher.decrypt(bytes(file_instance.encrypted_key))
            
                cipher = Fernet(file_key)
                decrypted_content = cipher.decrypt(bytes(file_instance.encrypted_data))
                
    
                response = HttpResponse(
                    # {"hhzy": "yeh"}
                    decrypted_content,
                    # content_type=file_instance.content_type,  
                )
                response['Content-Disposition'] = f'attachment; filename="{file_instance.file_name}"'
                
                return response
            
        except File.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)