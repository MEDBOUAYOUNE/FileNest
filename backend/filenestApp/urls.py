from django.urls import path
from .views import UploadFile, DownloadFile

urlpatterns = [

    path('/upload', UploadFile.as_view),
    path('/<uid>', DownloadFile.as_view),
]