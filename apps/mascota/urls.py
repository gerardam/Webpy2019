from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    path('crear_mascota/', login_required(MascotaCreate.as_view()), name='crear_mascota'),
    path('lista_mascota/', login_required(MascotaList.as_view()), name='lista_mascota'),
    path('editar_mascota/<pk>', login_required(MascotaUpdate.as_view()), name='editar_mascota'),
    path('eliminar_mascota/<pk>', login_required(MascotaDelete.as_view()), name='eliminar_mascota'),
]
