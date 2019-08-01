from django.urls import path, include
from apps.usuario.views import RegistroUsuario, UserAPI

urlpatterns = [
    path('registrar_usuario/', RegistroUsuario.as_view(), name='registrar_usuario'),
    path('api', UserAPI.as_view(), name='api'),
]
