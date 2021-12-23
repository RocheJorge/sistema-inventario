"""Importamos los VIEWS creados en VIEWS.PY

    from django.urls: Importamos el PATH
    from django.contrib.auth.decorators: Login_required
    from .views: Importamos los VIEWS de VIEWS.PY

"""


from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PerfilUsuarioView, ListadoUsuario, RegistrarUsuario, EditarUsuario, EliminarUsuario

"""Creamos las rutas de las vistas para los templates

    app_name: Nombre de la aplicacion
    path: Ruta donde crearemos la url
    <int:pk>: Asignamos el id para su actualizacion o eliminacion
"""


app_name = "usuario"

urlpatterns = [
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('listado_usuario/', login_required(ListadoUsuario.as_view()), name='listar_usuarios'),
    path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('editar_usuario/<int:pk>/', login_required(EditarUsuario.as_view()), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),
]