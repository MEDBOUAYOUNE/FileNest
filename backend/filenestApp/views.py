# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

class FileUploadView(APIView):
    def post(self, request):
        pass



class DownloadFileView(APIView):
    def get(self):
        pass