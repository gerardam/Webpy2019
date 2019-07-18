from django.urls import path, include
from apps.mascota.views import index, mascota_view

urlpatterns = [
    path('', index, name='index'),
    path('crear_mascota/', mascota_view, name='crear_mascota'),
]
