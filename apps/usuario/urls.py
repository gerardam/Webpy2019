from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.usuario.views import index, RegistroUsuario, UserAPI

urlpatterns = [
    path('', login_required(index), name='index'),
    path('registrar_usuario/', RegistroUsuario.as_view(), name='registrar_usuario'),
    path('api', UserAPI.as_view(), name='api'),
]
