from django.urls import path, include
from apps.usuario.views import RegistroUsuario

urlpatterns = [
    path('registrar_usuario/', RegistroUsuario.as_view(), name='registrar_usuario'),
]