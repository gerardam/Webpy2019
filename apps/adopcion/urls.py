from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('', index, name='index'),
    path('lista_solicitud/', login_required(SolicitudList.as_view()), name='lista_solicitud'),
    path('crear_solicitud/', login_required(SolicitudCreate.as_view()), name='crear_solicitud'),
    path('editar_solicitud/<pk>', login_required(SolicitudUpdate.as_view()), name='editar_solicitud'),
    path('eliminar_solicitud/<pk>', login_required(SolicitudDelete.as_view()), name='eliminar_solicitud'),
]
