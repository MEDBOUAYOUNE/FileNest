# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer

class FileUploadView(APIView):
     def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            return Response({
                "message": "File uploaded successfully.",
                "file_name": file_instance.file_name,
                "file_path" : file_instance.file_path.url,
                "uploaded_at": file_instance.uploaded_at
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DownloadFileView(APIView):
    def get(self):
        pass