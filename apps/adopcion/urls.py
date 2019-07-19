from django.urls import path, include
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('', index, name='index'),
    path('lista_solicitud/', SolicitudList.as_view(), name='lista_solicitud'),
    path('crear_solicitud/', SolicitudCreate.as_view(), name='crear_solicitud'),
    path('editar_solicitud/<pk>', SolicitudUpdate.as_view(), name='editar_solicitud'),
    path('eliminar_solicitud/<pk>', SolicitudDelete.as_view(), name='eliminar_solicitud'),
]
