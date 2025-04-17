# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileUploadSerializer
from django.conf import settings

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
            file_instance = File.objects.get(file_id=file_id)
            master_key = settings.FILE_ENCRYPTION_MASTER_KEY
            master_cipher = Fernet(master_key)
            
            file_key = master_cipher.decrypt(file_instance.encrypted_key)
        
            cipher = Fernet(file_key)
            decrypted_content = cipher.decrypt(file_instance.encrypted_data)
            
 
            response = HttpResponse(
                decrypted_content,
                content_type='application/octet-stream'  
            )
            response['Content-Disposition'] = f'attachment; filename="{file_instance.file_name}"'
            
            return response
            
        except File.DoesNotExist:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)