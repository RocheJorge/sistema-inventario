"""Importaciones
    
    from django.shortcuts: Render
    from django.contrib.auth: Login y Logout
    from django.http.response: HttpResponseRedirect
    from django.urls: reverse_lazy
    from django.utils.decorators: Metodo Decorador
    from django.views.decorators.cache: Never Cache
    from django.views.decorators.csrf: El csrf Token
    from django.views.generic.edit: Vista generica FormView
    from django.views.generic: Vistas genericas
    from usuario.models: Modelos de MODELS.PY
    from .forms: Formulario de FORMS.PY
    
"""


from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from usuario.models import Usuario
from .forms import FormularioLogin, FormularioUsuario

# Create your views here.

class Login(FormView):
    """Clase para el formulario de Login

    Argumentos:
        FormView (parametro): Traido de FormView de Django
        template_name: Template a usar del Login creado en TEMPLATES
        form_class: Formulario a usar de FORMS.PY
        success_url: Redireccionar cuando se logee exitosamente
        @method_decorator(csrf_protect): Decorador para proteger el ingreso con Token
        @method_decorator(never_cache): No guardar en memoria cache la contraseña
        

    Returns:
        una consulta
    """
    
    
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """Verifica el metodo de la peticion enviada por GET o POST

        Args:
            request (parametro): Peticion al servidor
            if request.user.is_authenticated: Verifica si el formulario es valido
            

        Returns:
            Usuario ingresa o no ingresa
        """
        
        
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)
        
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class PerfilUsuarioView(TemplateView):
    template_name = 'perfil.html'
    
# Usuarios

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'
    
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Usuarios'
        context["crear_url"] = reverse_lazy('usuario:registrar_usuario')
        context["lista_url"] = reverse_lazy('usuario:listar_usuarios')
        return context

class RegistrarUsuario(SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')
    success_message = "%(username)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('usuario:listar_usuarios')
        return context
    
class EditarUsuario(SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')
    success_message = "%(username)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('usuario:listar_usuarios')
        return context
    
class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuarios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('usuario:listar_usuarios')
        return context