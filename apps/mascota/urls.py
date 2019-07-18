from django.urls import path, include
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    path('', index, name='index'),
    path('crear_mascota/', mascota_view, name='crear_mascota'),
    path('lista_mascota/', mascota_list, name='lista_mascota'),
    path('editar_mascota/<int:id_mascota>', mascota_edit, name='editar_mascota'),
    path('eliminar_mascota/<int:id_mascota>', mascota_delete, name='eliminar_mascota'),
]
