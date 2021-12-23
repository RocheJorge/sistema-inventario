"""Importaciones
    
    from django.views.generic: VISTAS GENERICAS
    from .models: Modelos que creamos en MODELS.PY
    from .forms: Formulario de FORMS.PY
    from django.urls: REVERSE_LAZY
    from django.contrib.messages.views: Mensajes de SUCCESS
    from django.shortcuts: Render
    from django.db.models: Q consulta de Querys
    from itertools import: Chain matches con los diferentes models
"""


from django.http.response import Http404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Departamento, InventarioInmobiliariaNacional, InventarioIntu, JefeDepartamento, ResponsablePatrimonio, DireccionBienes, InventarioAdministracion, InventarioAsesoriaLegal, InventarioAtencionCiudadano, InventarioBanhaviCobranza, InventarioBanhaviFao, InventarioBarrioNuevoTricolor, InventarioDireccion, InventarioGestionHumana, InventarioInmobiliariaNacional, InventarioIntu, InventarioObras, InventarioRedesPopulares, InventarioSalaSituacional, InventarioSaren, InventarioJubilados, InventarioSistemas, InventarioSunavi, InventarioVivienda
from .forms import RegistrarDepartamentoForm, JefeDepartamentoForm, ResponsablePatrimonioForm, DireccionBienesForm, InventarioForm, InventarioAsesoriaLegalForm, InventarioAtencionCiudadanoForm, InventarioBanhaviCobranzaForm, InventarioBanhaviFaoForm, InventarioBarrioNuevoTricolorForm, InventarioDireccionForm, InventarioGestionHumanaForm, InventarioInmobiliariaNacionalForm, InventarioIntuForm, InventarioObrasForm, InventarioRedesPopularesForm, InventarioSalaSituacionalForm, InventarioSarenForm, InventarioJubiladosForm, InventarioSistemasForm, InventarioSunaviForm, InventarioViviendaForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.db.models import Q
from itertools import chain

class Inicio(TemplateView):
    """Le indicamos que template usara para mostrar la pagina de inicio
    
    Argumentos:
        TemplateView (parametro): Vista creada para mostrar el TEMPLATE
        template_name: Template que usara para la pagina de inicio que se encuentra en TEMPLATES
        
        
    Returns:
        una consulta    
    """
    
    
    template_name = 'index.html'

'''"""""""" Busqueda en el inventario """"""""""""""'''

def busqueda(request):
    busqueda = request.GET.get('buscar') # tomamos el valor del template
    
    if busqueda:
        """Validamos que lo que ingreso el usuario exista en la base de datos con el metodo exist() el cual devuelve un booleano y si es valido enviamos el contexto del resultado al template
        
        Argumentos:
            resultado: Toma todos los valores del query
            context: Enviamos el contexto al Template
            exists(): Metodo que valida si existe el valor ingresado
        
        
        Returns:
            consulta Base de Datos
        """
        
      
        administracion = InventarioAdministracion.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
            
        asesoriaLegal = InventarioAsesoriaLegal.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        atencionCiudadano = InventarioAtencionCiudadano.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
            
        banhaviCobranza = InventarioBanhaviCobranza.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        banhaviFao = InventarioBanhaviFao.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
            
        barrioNuevoTricolor = InventarioBarrioNuevoTricolor.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        direccion = InventarioDireccion.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
            
        gestionHumana = InventarioGestionHumana.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        inmobiliariaNacional = InventarioInmobiliariaNacional.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
            
        obras = InventarioObras.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        redesPopulares = InventarioRedesPopulares.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        salaSituacional = InventarioSalaSituacional.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        saren = InventarioSaren.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        jubilados = InventarioJubilados.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        sistemas = InventarioSistemas.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        sunavi = InventarioSunavi.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        vivienda = InventarioVivienda.objects.filter(
            Q(codigoDelBien__icontains=busqueda) |
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(caracteristica__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )
        
        resultado = list(chain(administracion, asesoriaLegal, atencionCiudadano, banhaviCobranza, banhaviFao, barrioNuevoTricolor, direccion, gestionHumana, inmobiliariaNacional, obras, redesPopulares, salaSituacional, saren, jubilados, sistemas, sunavi, vivienda))
            
        context= {
            'resultado': resultado
        }

        return render(request, 'busquedaInventario.html', context)
    
    else:
        
        return render(request, 'busquedaInventario.html')

'''""""""""""""""""" Departamentos """""""""""""""""""""""'''

class DepartamentosListView(ListView):
    """Contiene la Logica para listar los departamentos y mostrarlos por pantalla
    
    Argumentos:
        ListView (parametro): Vista creada para LISTAR
        model: Modelo a utilizarse creado en MODELS.PY
        template_name: 'Template que se usara para la clase ListView que se encuentra en TEMPLATES'


    Returns:
        una consulta
    """
    
    
    model = Departamento
    template_name = "departamentos/lista.html"
    
    def get_context_data(self, **kwargs):
        """Esta funcion contiene el contexto a enviar al template
        Aqui definimos todas las variables que necesitamos enviar a nuestro template definido en TEMPLATE_NAME, se agregan a un diccionario general para poder ser enviados

        
        Returns:
            el contexto al template que se esta usando
        """
        
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Departamentos'
        context['crear_url'] = reverse_lazy('app:crear_departamento')
        context['lista_url'] = reverse_lazy('app:lista_departamento')
        return context

class DepartamentosCreateView(SuccessMessageMixin, CreateView):
    """Contiene la logica para crear los departamentos y ser enviados al template

    Argumentos:
        SuccessMessageMixin (parametro): Enviamos el mensaje que queremos mostrar por pantalla indicandole al usuario que el departamento fue creado exitosamente
        CreateView (parametro): Vista creada para la creacion
        model: Modelo a utilizarse creado desde MODELS.PY
        form_class: Formulario de django referente al modelo creado en FORMS.PY
        template_name: Template que se usara para la clase CreateView que se encuentra en TEMPLATES
        succes_url: Url a la redirecciona al haber sido CREADO exitosamente
        success_message: Mensaje de que se CREO exitosamente


    Returns:
        succes_url: Url a redireccionar
        success_message: Mensaje a mostrar por pantalla
    """
    
    
    model = Departamento
    form_class = RegistrarDepartamentoForm
    template_name = 'departamentos/crear.html'
    success_url = reverse_lazy('app:lista_departamento')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_departamento')
        return context

class DepartamentosUpdateView(SuccessMessageMixin, UpdateView):
    """Contiene la logica para actualizar los departamentos y ser enviados al template

    Argumentos:
        SuccessMessageMixin (parametro): Enviamos el mensaje que queremos mostrar por pantalla indicandole al usuario que el departamento fue actualizado exitosamente
        UpdateView (parametro): Vista creada para la actualizacion
        model: Modelo a utilizarse creado desde MODELS.PY
        form_class: Formulario de django referente al modelo creado en FORMS.PY
        template_name: Template que se usara para la clase UpdateView que se encuentra en TEMPLATES
        succes_url: Url a la redirecciona al haber sido ACTUALIZADO exitosamente
        success_message: Mensaje de que se ACTUALIZADO exitosamente


    Returns:
        succes_url: Url a redireccionar
        success_message: Mensaje a mostrar por pantalla
    """
    
    
    model = Departamento
    form_class = RegistrarDepartamentoForm
    template_name = 'departamentos/crear.html'
    success_url = reverse_lazy('app:lista_departamento')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_departamento')
        return context

class DepartamentosDeleteView(DeleteView):
    """Contiene la logica para Eliminar los departamentos y ser enviados al template

    Argumentos:
        DeleteView (parametro): Vista creada para la ELIMINACION
        model: Modelo a utilizarse creado desde MODELS.PY
        template_name: Template que se usara para la clase DeleteView que se encuentra en TEMPLATES
        succes_url: Url a la redirecciona al haber sido ELIMINADO exitosamente


    Returns:
        succes_url: Url a redireccionar
    """
    
    
    model = Departamento
    template_name = 'departamentos/eliminar.html'
    success_url = reverse_lazy('app:lista_departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_departamento')
        return context

'''"""""""" Jefes de Departamentos Departamentos """"""""""""""'''

class JefeDepartamentoListView(ListView):
    model = JefeDepartamento
    template_name = "jefe_departamento/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Jefe Departamento'
        context['crear_url'] = reverse_lazy('app:crear_jefe_departamento')
        context['lista_url'] = reverse_lazy('app:lista_jefe_departamento')
        return context

class JefeDepartamentoCreateView(SuccessMessageMixin, CreateView):
    model = JefeDepartamento
    form_class = JefeDepartamentoForm
    template_name = 'jefe_departamento/crear.html'
    success_url = reverse_lazy('app:lista_jefe_departamento')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_jefe_departamento')
        return context

class JefeDepartamentoUpdateView(SuccessMessageMixin,UpdateView):
    model = JefeDepartamento
    form_class = JefeDepartamentoForm
    template_name = 'jefe_departamento/crear.html'
    success_url = reverse_lazy('app:lista_jefe_departamento')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_jefe_departamento')
        return context

class JefeDepartamentoDeleteView(DeleteView):
    model = JefeDepartamento
    template_name = 'jefe_departamento/eliminar.html'
    success_url = reverse_lazy('app:lista_jefe_departamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_jefe_departamento')
        return context
    
'''"""""""" Responsable del Patrimonio """"""""""""""'''

class ResponsablePatrimonioListView(ListView):
    model = ResponsablePatrimonio
    template_name = "responsable_patrimonio/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Responsable Patrimonio'
        context['crear_url'] = reverse_lazy('app:crear_responsable_patrimonio')
        context['lista_url'] = reverse_lazy('app:lista_responsable_patrimonio')
        return context

class ResponsablePatrimonioCreateView(SuccessMessageMixin, CreateView):
    model = ResponsablePatrimonio
    form_class = ResponsablePatrimonioForm
    template_name = 'responsable_patrimonio/crear.html'
    success_url = reverse_lazy('app:lista_responsable_patrimonio')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_responsable_patrimonio')
        return context

class ResponsablePatrimonioUpdateView(SuccessMessageMixin,UpdateView):
    model = ResponsablePatrimonio
    form_class = ResponsablePatrimonioForm
    template_name = 'responsable_patrimonio/crear.html'
    success_url = reverse_lazy('app:lista_responsable_patrimonio')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_responsable_patrimonio')
        return context

class ResponsablePatrimonioDeleteView(DeleteView):
    model = ResponsablePatrimonio
    template_name = 'responsable_patrimonio/eliminar.html'
    success_url = reverse_lazy('app:lista_responsable_patrimonio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_responsable_patrimonio')
        return context
    
'''""""""""  Direccion de Bienes """"""""""""""'''

class DireccionBienesListView(ListView):
    model = DireccionBienes
    template_name = "direccion_bienes/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Direccion Bienes'
        context['crear_url'] = reverse_lazy('app:crear_direccion_bienes')
        context['lista_url'] = reverse_lazy('app:lista_direccion_bienes')
        return context

class DireccionBienesCreateView(SuccessMessageMixin, CreateView):
    model = DireccionBienes
    form_class = DireccionBienesForm
    template_name = 'direccion_bienes/crear.html'
    success_url = reverse_lazy('app:lista_direccion_bienes')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_direccion_bienes')
        return context

class DireccionBienesUpdateView(SuccessMessageMixin,UpdateView):
    model = DireccionBienes
    form_class = DireccionBienesForm
    template_name = 'direccion_bienes/crear.html'
    success_url = reverse_lazy('app:lista_direccion_bienes')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_direccion_bienes')
        return context

class DireccionBienesDeleteView(DeleteView):
    model = DireccionBienes
    template_name = 'direccion_bienes/eliminar.html'
    success_url = reverse_lazy('app:lista_direccion_bienes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_direccion_bienes')
        return context
    
'''""""""""""" Views de Inventarios """"""""""""""""'''

'''""""""""""" Administracion """"""""""""""""'''

class InventarioListView(ListView):
    model = InventarioAdministracion
    template_name = "inventario/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administracion'
        context['crear_url'] = reverse_lazy('app:crear_inventario')
        context['lista_url'] = reverse_lazy('app:lista_inventario')
        return context
    
class InventarioCreateView(SuccessMessageMixin, CreateView):
    model = InventarioAdministracion
    form_class = InventarioForm
    template_name = 'inventario/crear.html'
    success_url = reverse_lazy('app:lista_inventario')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario')
        return context
    
class InventarioUpdateView(SuccessMessageMixin,UpdateView):
    model = InventarioAdministracion
    form_class = InventarioForm
    template_name = 'inventario/crear.html'
    success_url = reverse_lazy('app:lista_inventario')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario')
        return context

class InventarioDeleteView(DeleteView):
    model = InventarioAdministracion
    template_name = 'inventario/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_inventario')
        return context
    
'''""""""""""" Asesoria Legal """"""""""""""""'''

class InventarioAsesoriaLegalListView(ListView):
    model = InventarioAsesoriaLegal
    template_name = "inventario/asesoriaLegal/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Asesoria Legal'
        context['crear_url'] = reverse_lazy('app:crear_inventario_asesoria_legal')
        context['lista_url'] = reverse_lazy('app:lista_inventario_asesoria_legal')
        return context

class InventarioAsesoriaLegalCreateView(SuccessMessageMixin, CreateView):
    model = InventarioAsesoriaLegal
    form_class = InventarioAsesoriaLegalForm
    template_name = 'inventario/asesoriaLegal/crear.html'
    success_url = reverse_lazy('app:lista_inventario_asesoria_legal')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_asesoria_legal')
        return context

class InventarioAsesoriaLegalUpdateView(SuccessMessageMixin,UpdateView):
    model = InventarioAsesoriaLegal
    form_class = InventarioAsesoriaLegalForm
    template_name = 'inventario/asesoriaLegal/crear.html'
    success_url = reverse_lazy('app:lista_inventario_asesoria_legal')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_asesoria_legal')
        return context

class InventarioAsesoriaLegalDeleteView(DeleteView):
    model = InventarioAsesoriaLegal
    template_name = 'inventario/asesoriaLegal/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_asesoria_legal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_asesoria_legal')
        return context
    
'''""""""""""" Atencion al ciudadano """"""""""""""""'''

class InventarioAtencionCiudadanoListView(ListView):
    model = InventarioAtencionCiudadano
    template_name = "inventario/atencionCiudadano/lista.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atencion Ciudadano'
        context['crear_url'] = reverse_lazy('app:crear_inventario_atencion_ciudadano')
        context['lista_url'] = reverse_lazy('app:lista_inventario_atencion_ciudadano')
        return context

class InventarioAtencionCiudadanoCreateView(SuccessMessageMixin, CreateView):
    model = InventarioAtencionCiudadano
    form_class = InventarioAtencionCiudadanoForm
    template_name = 'inventario/atencionCiudadano/crear.html'
    success_url = reverse_lazy('app:lista_inventario_atencion_ciudadano')
    success_message = "%(nombre)s Fue Agregado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_atencion_ciudadano')
        return context
    
class InventarioAtencionCiudadanoUpdateView(SuccessMessageMixin,UpdateView):
    model = InventarioAtencionCiudadano
    form_class = InventarioAtencionCiudadanoForm
    template_name = 'inventario/atencionCiudadano/crear.html'
    success_url = reverse_lazy('app:lista_inventario_atencion_ciudadano')
    success_message = "%(nombre)s Fue Actualizado Correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_atencion_ciudadano')
        return context
    
class InventarioAtencionCiudadanoDeleteView(DeleteView):
    model = InventarioAtencionCiudadano
    template_name = 'inventario/atencionCiudadano/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_atencion_ciudadano')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_atencion_ciudadano')
        return context
    
'''""""""""""" Banhavi Cobranza """"""""""""""""'''

class InventarioBanhaviCobranzaListView(ListView):
    model = InventarioBanhaviCobranza
    template_name = 'inventario/banhaviCobranza/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Banhavi Cobranza'
        context['crear_url'] = reverse_lazy('app:crear_inventario_banhavi_cobranza')
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_cobranza')
        return context
    
class InventarioBanhaviCobranzaCreateView(SuccessMessageMixin, CreateView):
    model = InventarioBanhaviCobranza
    form_class = InventarioBanhaviCobranzaForm
    template_name = 'inventario/banhaviCobranza/crear.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_cobranza')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_cobranza')
        return context
    
class InventarioBanhaviCobranzaUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioBanhaviCobranza
    form_class = InventarioBanhaviCobranzaForm
    template_name = 'inventario/banhaviCobranza/crear.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_cobranza')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_cobranza')
        return context
    
class InventarioBanhaviCobranzaDeleteView(DeleteView):
    model = InventarioBanhaviCobranza
    template_name = 'inventario/banhaviCobranza/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_cobranza')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar'
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_cobranza')
        return context
    
'''""""""""""" Banhavi FAO """"""""""""""""'''

class InventarioBanhaviFaoListView(ListView):
    model = InventarioBanhaviFao
    template_name = 'inventario/banhaviFao/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Banhavi FAO'
        context['crear_url'] = reverse_lazy('app:crear_inventario_banhavi_fao')
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_fao')
        return context
    
class InventarioBanhaviFaoCreateView(SuccessMessageMixin, CreateView):
    model = InventarioBanhaviFao
    form_class = InventarioBanhaviFaoForm
    template_name = 'inventario/banhaviFao/crear.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_fao')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_fao')
        return context
    
class InventarioBanhaviFaoUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioBanhaviFao
    form_class = InventarioBanhaviFaoForm
    template_name = 'inventario/banhaviFao/crear.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_fao')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_fao')
        return context
    
class InventarioBanhaviFaoDeleteView(DeleteView):
    model = InventarioBanhaviFao
    template_name = 'inventario/banhaviFao/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_banhavi_fao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_banhavi_fao')
        return context
    
'''""""""""""" Barrio Nuevo Barrio Tricolor """"""""""""""""'''

class InventarioBarrioNuevoTricolorListView(ListView):
    model = InventarioBarrioNuevoTricolor
    template_name = 'inventario/barrioNuevoTricolor/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Barrio Nuevo Barrio Tricolor'
        context['crear_url'] = reverse_lazy('app:crear_inventario_bnbt')
        context['lista_url'] = reverse_lazy('app:lista_inventario_bnbt')
        return context

class InventarioBarrioNuevoTricolorCreateView(SuccessMessageMixin, CreateView):
    model = InventarioBarrioNuevoTricolor
    form_class = InventarioBarrioNuevoTricolorForm
    template_name = 'inventario/barrioNuevoTricolor/crear.html'
    success_url = reverse_lazy('app:lista_inventario_bnbt')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_bnbt')
        return context

class InventarioBarrioNuevoTricolorUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioBarrioNuevoTricolor
    form_class = InventarioBarrioNuevoTricolorForm
    template_name = 'inventario/barrioNuevoTricolor/crear.html'
    success_url = reverse_lazy('app:lista_inventario_bnbt')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_bnbt')
        return context

class InventarioBarrioNuevoTricolorDeleteView(DeleteView):
    model = InventarioBarrioNuevoTricolor
    template_name = 'inventario/barrioNuevoTricolor/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_bnbt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_bnbt')
        return context
    
'''""""""""""" Direccion """"""""""""""""'''

class InventarioDireccionListView(ListView):
    model = InventarioDireccion
    template_name = 'inventario/direccion/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Dirección'
        context['crear_url'] = reverse_lazy('app:crear_inventario_direccion')
        context['lista_url'] = reverse_lazy('app:lista_inventario_direccion')
        return context

class InventarioDireccionCreateView(SuccessMessageMixin, CreateView):
    model = InventarioDireccion
    form_class = InventarioDireccionForm
    template_name = 'inventario/direccion/crear.html'
    success_url = reverse_lazy('app:lista_inventario_direccion')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_direccion')
        return context
    
class InventarioDireccionUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioDireccion
    form_class = InventarioDireccionForm
    template_name = 'inventario/direccion/crear.html'
    success_url = reverse_lazy('app:lista_inventario_direccion')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_direccion')
        return context
    
class InventarioDireccionDeleteView(DeleteView):
    model = InventarioDireccion
    template_name = 'inventario/direccion/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_direccion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_direccion')
        return context
    
'''""""""""""" Gestion Humana """"""""""""""""'''

class InventarioGestionHumanaListView(ListView):
    model = InventarioGestionHumana
    template_name = 'inventario/gestionHumana/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion Humana'
        context['crear_url'] = reverse_lazy('app:crear_inventario_gestion_humana')
        context['lista_url'] = reverse_lazy('app:lista_inventario_gestion_humana')
        return context
    
class InventarioGestionHumanaCreateView(SuccessMessageMixin, CreateView):
    model = InventarioGestionHumana
    form_class = InventarioGestionHumanaForm
    template_name = 'inventario/gestionHumana/crear.html'
    success_url = reverse_lazy('app:lista_inventario_gestion_humana')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Agregar'
        context['titulo_accion'] = 'Guardar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_gestion_humana')
        return context
    
class InventarioGestionHumanaUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioGestionHumana
    form_class = InventarioGestionHumanaForm
    template_name = 'inventario/gestionHumana/crear.html'
    success_url = reverse_lazy('app:lista_inventario_gestion_humana')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar'
        context['titulo_accion'] = 'Actualizar Registro'
        context['lista_url'] = reverse_lazy('app:lista_inventario_gestion_humana')
        return context
    
class InventarioGestionHumanaDeleteView(DeleteView):
    model = InventarioGestionHumana
    template_name = 'inventario/gestionHumana/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_gestion_humana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Eliminar '
        context['lista_url'] = reverse_lazy('app:lista_inventario_gestion_humana')
        return context
    
'''""""""""""" Inmobiliaria Nacional """"""""""""""""'''

class InventarioInmobiliariaNacionalListView(ListView):
    model = InventarioInmobiliariaNacional
    template_name = 'inventario/inmobiliariaNacional/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Inmobiliaria Nacional'
        context["crear_url"] = reverse_lazy('app:crear_inventario_inmobiliaria_nacional')
        context["lista_url"] = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
        return context

class InventarioInmobiliariaNacionalCreateView(SuccessMessageMixin, CreateView):
    model = InventarioInmobiliariaNacional
    form_class = InventarioInmobiliariaNacionalForm
    template_name = 'inventario/inmobiliariaNacional/crear.html'
    success_url = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
        return context
    
class InventarioInmobiliarioNacionalUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioInmobiliariaNacional
    form_class = InventarioInmobiliariaNacionalForm
    template_name = 'inventario/inmobiliariaNacional/crear.html'
    success_url = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
        return context
    
class InventarioInmobiliariaNacionalDeleteView(DeleteView):
    model = InventarioInmobiliariaNacional
    template_name = 'inventario/inmobiliariaNacional/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_inmobiliaria_nacional')
        return context
    
'''""""""""""" Intu """"""""""""""""'''

class InventarioIntuListView(ListView):
    model = InventarioIntu
    template_name = 'inventario/intu/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Intu'
        context["crear_url"] = reverse_lazy('app:crear_inventario_intu')
        context["lista_url"] = reverse_lazy('app:lista_inventario_intu')
        return context
    
class InventarioIntuCreateView(SuccessMessageMixin, CreateView):
    model = InventarioIntu
    form_class = InventarioIntuForm
    template_name = 'inventario/intu/crear.html'
    success_url = reverse_lazy('app:lista_inventario_intu')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_intu')
        return context
    
class InventarioIntuUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioIntu
    form_class = InventarioIntuForm
    template_name = 'inventario/intu/crear.html'
    success_url = reverse_lazy('app:lista_inventario_intu')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_intu')
        return context
    
class InventarioIntuDeleteView(DeleteView):
    model = InventarioIntu
    template_name = 'inventario/intu/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_intu')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_intu')
        return context
    
'''""""""""""" Obras """"""""""""""""'''

class InventarioObrasListView(ListView):
    model = InventarioObras
    template_name = 'inventario/obras/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Obras'
        context["crear_url"] = reverse_lazy('app:crear_inventario_obras')
        context["lista_url"] = reverse_lazy('app:lista_inventario_obras')
        return context
    
class InventarioObrasCreateView(SuccessMessageMixin, CreateView):
    model = InventarioObras
    form_class = InventarioObrasForm
    template_name = 'inventario/obras/crear.html'
    success_url = reverse_lazy('app:lista_inventario_obras')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_obras')
        return context
    
class InventarioObrasUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioObras
    form_class = InventarioObrasForm
    template_name = 'inventario/obras/crear.html'
    success_url = reverse_lazy('app:lista_inventario_obras')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_obras')
        return context
    
class InventarioObrasDeleteView(DeleteView):
    model = InventarioObras
    template_name = 'inventario/obras/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_obras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_obras')
        return context
    
'''""""""""""" Redes Populares """"""""""""""""'''

class InventarioRedesPopularesListView(ListView):
    model = InventarioRedesPopulares
    template_name = 'inventario/redesPopulares/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Redes Populares'
        context["crear_url"] = reverse_lazy('app:crear_inventario_redes_populares')
        context["lista_url"] = reverse_lazy('app:lista_inventario_redes_populares')
        return context

class InventarioRedesPopularesCreateView(SuccessMessageMixin, CreateView):
    model = InventarioRedesPopulares
    form_class = InventarioRedesPopularesForm
    template_name = 'inventario/redesPopulares/crear.html'
    success_url = reverse_lazy('app:lista_inventario_redes_populares')
    success_message = "%(nombre)s Fue Agregado Corectamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Creacion Inventario'
        context["lista_url"] = reverse_lazy('app:lista_inventario_redes_populares')
        return context
    
class InventarioRedesPopularesUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioRedesPopulares
    form_class = InventarioRedesPopularesForm
    template_name = 'inventario/redesPopulares/crear.html'
    success_url = reverse_lazy('app:lista_inventario_redes_populares')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_redes_populares')
        return context
    
class InventarioRedesPopularesDeleteView(DeleteView):
    model = InventarioRedesPopulares
    template_name = 'inventario/redesPopulares/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_redes_populares')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_redes_populares')
        return context
    
'''""""""""""" Sala Situacional """"""""""""""""'''

class InventarioSalaSituacionalListView(ListView):
    model = InventarioSalaSituacional
    template_name = 'inventario/salaSituacional/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Sala Situacional'
        context["crear_url"] = reverse_lazy('app:crear_inventario_sala_situacional')
        context["lista_url"] = reverse_lazy('app:lista_inventario_sala_situacional')
        return context

class InventarioSalaSituacionalCreateView(SuccessMessageMixin, CreateView):
    model = InventarioSalaSituacional
    form_class = InventarioSalaSituacionalForm
    template_name = 'inventario/salaSituacional/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sala_situacional')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sala_situacional')
        return context
    
class InventarioSalaSituacionalUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioSalaSituacional
    form_class = InventarioSalaSituacionalForm
    template_name = 'inventario/salaSituacional/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sala_situacional')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sala_situacional')
        return context
    
class InventarioSalaSituacionalDeleteView(DeleteView):
    model = InventarioSalaSituacional
    template_name = 'inventario/salaSituacional/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_sala_situacional')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sala_situacional')
        return context
    
'''""""""""""" Saren """"""""""""""""'''

class InventarioSarenListView(ListView):
    model = InventarioSaren
    template_name = 'inventario/saren/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Saren'
        context["crear_url"] = reverse_lazy('app:crear_inventario_saren')
        context["lista_url"] = reverse_lazy('app:lista_inventario_saren')
        return context
    
class InventarioSarenCreateView(SuccessMessageMixin, CreateView):
    model = InventarioSaren
    form_class = InventarioSarenForm
    template_name = 'inventario/saren/crear.html'
    success_url = reverse_lazy('app:lista_inventario_saren')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_saren')
        return context
    
class InventarioSarenUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioSaren
    form_class = InventarioSarenForm
    template_name = 'inventario/saren/crear.html'
    success_url = reverse_lazy('app:lista_inventario_saren')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_saren')
        return context
    
class InventarioSarenDeleteView(DeleteView):
    model = InventarioSaren
    template_name = 'inventario/saren/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_saren')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_saren')
        return context
    
'''""""""""""" Jubilados """"""""""""""""'''

class InventarioJubiladosListView(ListView):
    model = InventarioJubilados
    template_name = 'inventario/jubilados/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Jubilados'
        context["crear_url"] = reverse_lazy('app:crear_inventario_jubilados')
        context["lista_url"] = reverse_lazy('app:lista_inventario_jubilados')
        return context
    
class InventarioJubiladosCreateView(SuccessMessageMixin, CreateView):
    model = InventarioJubilados
    form_class = InventarioJubiladosForm
    template_name = 'inventario/jubilados/crear.html'
    success_url = reverse_lazy('app:lista_inventario_jubilados')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_jubilados')
        return context
    
class InventarioJubiladosUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioJubilados
    form_class = InventarioJubiladosForm
    template_name = 'inventario/jubilados/crear.html'
    success_url = reverse_lazy('app:lista_inventario_jubilados')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_jubilados')
        return context
    
class InventarioJubiladosDeleteView(DeleteView):
    model = InventarioJubilados
    template_name = 'inventario/jubilados/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_jubilados')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_jubilados')
        return context
    
'''""""""""""" Sistemas """"""""""""""""'''

class InventarioSistemasListView(ListView):
    model = InventarioSistemas
    template_name = 'inventario/sistemas/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Sistemas'
        context["crear_url"] = reverse_lazy('app:crear_inventario_sistemas')
        context["lista_url"] = reverse_lazy('app:lista_inventario_sistemas')
        return context
    
class InventarioSistemasCreateView(SuccessMessageMixin, CreateView):
    model = InventarioSistemas
    form_class = InventarioSistemasForm
    template_name = 'inventario/sistemas/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sistemas')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sistemas')
        return context

class InventarioSistemasUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioSistemas
    form_class = InventarioSistemasForm
    template_name = 'inventario/sistemas/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sistemas')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sistemas')
        return context

class InventarioSistemasDeleteView(DeleteView):
    model = InventarioSistemas
    template_name = 'inventario/sistemas/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_sistemas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sistemas')
        return context

'''""""""""""" Sunavi """"""""""""""""'''

class InventarioSunaviListView(ListView):
    model = InventarioSunavi
    template_name = 'inventario/sunavi/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Sunavi'
        context["crear_url"] = reverse_lazy('app:crear_inventario_sunavi')
        context["lista_url"] = reverse_lazy('app:lista_inventario_sunavi')
        return context
    
class InventarioSunaviCreateView(SuccessMessageMixin, CreateView):
    model = InventarioSunavi
    form_class = InventarioSunaviForm
    template_name = 'inventario/sunavi/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sunavi')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sunavi')
        return context
    
class InventarioSunaviUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioSunavi
    form_class = InventarioSunaviForm
    template_name = 'inventario/sunavi/crear.html'
    success_url = reverse_lazy('app:lista_inventario_sunavi')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sunavi')
        return context
    
class InventarioSunaviDeleteView(DeleteView):
    model = InventarioSunavi
    template_name = 'inventario/sunavi/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_sunavi')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_sunavi')
        return context
    
'''""""""""""" Vivienda """"""""""""""""'''

class InventarioViviendaListView(ListView):
    model = InventarioVivienda
    template_name = 'inventario/vivienda/lista.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Vivienda'
        context["crear_url"] = reverse_lazy('app:crear_inventario_vivienda')
        context["lista_url"] = reverse_lazy('app:lista_inventario_vivienda')    
        return context
    
class InventarioViviendaCreateView(SuccessMessageMixin, CreateView):
    model = InventarioVivienda
    form_class = InventarioViviendaForm
    template_name = 'inventario/vivienda/crear.html'
    success_url = reverse_lazy('app:lista_inventario_vivienda')
    success_message = "%(nombre)s Fue Agregado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Agregar'
        context["titulo_accion"] = 'Guardar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_vivienda')
        return context
    
class InventarioViviendaUpdateView(SuccessMessageMixin, UpdateView):
    model = InventarioVivienda
    form_class = InventarioViviendaForm
    template_name = 'inventario/vivienda/crear.html'
    success_url = reverse_lazy('app:lista_inventario_vivienda')
    success_message = "%(nombre)s Fue Actualizado Correctamente"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Editar'
        context["titulo_accion"] = 'Actualizar Registro'
        context["lista_url"] = reverse_lazy('app:lista_inventario_vivienda')
        return context
    
class InventarioViviendaDeleteView(DeleteView):
    model = InventarioVivienda
    template_name = 'inventario/vivienda/eliminar.html'
    success_url = reverse_lazy('app:lista_inventario_vivienda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_form"] = 'Eliminar'
        context["lista_url"] = reverse_lazy('app:lista_inventario_vivienda')
        return context
    