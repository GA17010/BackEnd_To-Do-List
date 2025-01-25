from django.urls import path
from . import views

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import TaskListView, TaskDetailView

schema_view = get_schema_view(
   openapi.Info(
        title="API de Tareas",
        default_version="v1",
        description="Documentación de la API para la aplicación de tareas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ga17010@ues.edu.sv"),
        license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger and Redoc documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]
