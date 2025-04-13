from django.urls import path, re_path, include
from .views import FileUploadView, DownloadFileView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="FileNest API",
        default_version='v1',
        description="A file-sharing system that allows users to anonymously share files quickly and securely, with time-based expiration",
        contact=openapi.Contact(email="mbouayou@student.1337.ma"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('api/upload', FileUploadView.as_view()),
    path('api/<str:token>', DownloadFileView.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]