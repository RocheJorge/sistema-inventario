"""Importamos los VIEWS creados en VIEWS.PY

    from django.urls: Importamos el PATH
    from .views: Importamos los VIEWS de VIEWS.PY

"""


from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DepartamentosListView, DepartamentosCreateView, DepartamentosUpdateView, DepartamentosDeleteView, JefeDepartamentoListView,JefeDepartamentoCreateView, JefeDepartamentoUpdateView, JefeDepartamentoDeleteView, ResponsablePatrimonioListView, ResponsablePatrimonioCreateView, ResponsablePatrimonioUpdateView, ResponsablePatrimonioDeleteView, DireccionBienesListView, DireccionBienesCreateView, DireccionBienesUpdateView, DireccionBienesDeleteView, InventarioListView, InventarioCreateView, InventarioUpdateView, InventarioDeleteView, InventarioAsesoriaLegalListView, InventarioAsesoriaLegalCreateView, InventarioAsesoriaLegalUpdateView, InventarioAsesoriaLegalDeleteView, InventarioAtencionCiudadanoListView, InventarioAtencionCiudadanoCreateView, InventarioAtencionCiudadanoUpdateView, InventarioAtencionCiudadanoDeleteView, InventarioBanhaviCobranzaListView, InventarioBanhaviCobranzaCreateView, InventarioBanhaviCobranzaUpdateView, InventarioBanhaviCobranzaDeleteView, InventarioBanhaviFaoListView, InventarioBanhaviFaoCreateView, InventarioBanhaviFaoUpdateView, InventarioBanhaviFaoDeleteView, InventarioBarrioNuevoTricolorListView, InventarioBarrioNuevoTricolorCreateView, InventarioBarrioNuevoTricolorUpdateView, InventarioBarrioNuevoTricolorDeleteView, InventarioDireccionListView, InventarioDireccionCreateView, InventarioDireccionUpdateView, InventarioDireccionDeleteView, InventarioGestionHumanaListView, InventarioGestionHumanaCreateView, InventarioGestionHumanaUpdateView, InventarioGestionHumanaDeleteView, InventarioInmobiliariaNacionalListView, InventarioInmobiliariaNacionalCreateView, InventarioInmobiliarioNacionalUpdateView, InventarioInmobiliariaNacionalDeleteView, InventarioIntuListView, InventarioIntuCreateView, InventarioIntuUpdateView, InventarioIntuDeleteView, InventarioObrasListView, InventarioObrasCreateView, InventarioObrasUpdateView, InventarioObrasDeleteView, InventarioRedesPopularesListView, InventarioRedesPopularesCreateView, InventarioRedesPopularesUpdateView, InventarioRedesPopularesDeleteView, InventarioSalaSituacionalListView, InventarioSalaSituacionalCreateView, InventarioSalaSituacionalUpdateView, InventarioSalaSituacionalDeleteView, InventarioSarenListView, InventarioSarenCreateView, InventarioSarenUpdateView, InventarioSarenDeleteView, InventarioJubiladosListView, InventarioJubiladosCreateView, InventarioJubiladosUpdateView, InventarioJubiladosDeleteView, InventarioSistemasListView, InventarioSistemasCreateView, InventarioSistemasUpdateView, InventarioSistemasDeleteView, InventarioSunaviListView, InventarioSunaviCreateView, InventarioSunaviUpdateView, InventarioSunaviDeleteView, InventarioViviendaListView, InventarioViviendaCreateView, InventarioViviendaUpdateView, InventarioViviendaDeleteView, busqueda

"""Creamos las rutas de las vistas para los templates

    app_name: Nombre de la aplicacion
    path: Ruta donde crearemos la url
    <int:pk>: Asignamos el id para su actualizacion o eliminacion
"""


app_name = "app"

urlpatterns = [
    ##################### Busqueda en el Inventario ####################
    path('busqueda/lista/', login_required(busqueda), name='busqueda_inventario'),
    ##################### Departamentos ####################
    # listar
    path('departamentos/lista/', login_required(DepartamentosListView.as_view()), name='lista_departamento'),
    # Crear
    path('departamentos/crear/', login_required(DepartamentosCreateView.as_view()), name='crear_departamento'),
    # Editar
    path('departamentos/editar/<int:pk>/', login_required(DepartamentosUpdateView.as_view()), name='editar_departamento'),
    # eliminar
    path('departamentos/eliminar/<int:pk>/', login_required(DepartamentosDeleteView.as_view()), name='eliminar_departamento'),
    ##################### Jefe de los Departamentos ####################
    # listar
    path('jefe_departamento/lista/', login_required(JefeDepartamentoListView.as_view()), name='lista_jefe_departamento'),
    # Crear
    path('jefe_departamento/crear/', login_required(JefeDepartamentoCreateView.as_view()), name='crear_jefe_departamento'),
    # Editar
    path('jefe_departamento/editar/<int:pk>/', login_required(JefeDepartamentoUpdateView.as_view()), name='editar_jefe_departamento'),
    # Eliminar
    path('jefe_departamento/eliminar/<int:pk>/', login_required(JefeDepartamentoDeleteView.as_view()), name='eliminar_jefe_departamento'),
    ##################### Responsable del Patrimonio ####################
    # listar
    path('responsable_patrimonio/lista/', login_required(ResponsablePatrimonioListView.as_view()), name='lista_responsable_patrimonio'),
    # Crear
    path('responsable_patrimonio/crear/', login_required(ResponsablePatrimonioCreateView.as_view()), name='crear_responsable_patrimonio'),
    # Editar
    path('responsable_patrimonio/editar/<int:pk>/', login_required(ResponsablePatrimonioUpdateView.as_view()), name='editar_responsable_patrimonio'),
    path('responsable_patrimonio/eliminar/<int:pk>/', login_required(ResponsablePatrimonioDeleteView.as_view()), name='eliminar_responsable_patrimonio'),
    ##################### Direccion de Bienes ####################
    # listar
    path('direccion_bienes/lista/', login_required(DireccionBienesListView.as_view()), name='lista_direccion_bienes'),
    # crear
    path('direccion_bienes/crear/', login_required(DireccionBienesCreateView.as_view()), name='crear_direccion_bienes'),
    # editar
    path('direccion_bienes/editar/<int:pk>/', login_required(DireccionBienesUpdateView.as_view()), name='editar_direccion_bienes'),
    # eliminar
    path('direccion_bienes/eliminar/<int:pk>/', login_required(DireccionBienesDeleteView.as_view()), name='eliminar_direccion_bienes'),
    ##################### Inventarios #####################
    ##################### Administracion #####################
    # listar
    path('inventario/lista/', login_required(InventarioListView.as_view()), name='lista_inventario'),
    # crear
    path('inventario/crear/', login_required(InventarioCreateView.as_view()), name='crear_inventario'),
    # editar
    path('inventario/editar/<int:pk>/', login_required(InventarioUpdateView.as_view()), name='editar_inventario'),
    # eliminar
    path('inventario/eliminar/<int:pk>/', login_required(InventarioDeleteView.as_view()), name='eliminar_inventario'),
    ##################### Asesoria Legal ####################
    # listar
    path('inventario/asesoria_legal/lista/', login_required(InventarioAsesoriaLegalListView.as_view()), name='lista_inventario_asesoria_legal'),
    # crear
    path('inventario/asesoria_legal/crear/', login_required(InventarioAsesoriaLegalCreateView.as_view()), name='crear_inventario_asesoria_legal'),
    # Editar
    path('inventario/asesoria_legal/editar/<int:pk>/', login_required(InventarioAsesoriaLegalUpdateView.as_view()), name='editar_inventario_asesoria_legal'),
    # eliminar
    path('inventario/asesoria_legal/eliminar/<int:pk>/', login_required(InventarioAsesoriaLegalDeleteView.as_view()), name='eliminar_inventario_asesoria_legal'),
    ##################### Atencion Ciudadano ####################
    # listar
    path('inventario/atencion_ciudadano/lista/', login_required(InventarioAtencionCiudadanoListView.as_view()), name='lista_inventario_atencion_ciudadano'),
    # crear
    path('inventario/atencion_ciudadano/crear/', login_required(InventarioAtencionCiudadanoCreateView.as_view()), name='crear_inventario_atencion_ciudadano'),
    # Editar
    path('inventario/atencion_ciudadano/editar/<int:pk>/', login_required(InventarioAtencionCiudadanoUpdateView.as_view()), name='editar_inventario_atencion_ciudadano'),
    # Eliminar
    path('inventario/atencion_ciudadano/eliminar/<int:pk>/', login_required(InventarioAtencionCiudadanoDeleteView.as_view()), name='eliminar_inventario_atencion_ciudadano'),
    ##################### Banhavi Cobranza #####################
    # listar
    path('inventario/banhavi_cobranza/lista/', login_required(InventarioBanhaviCobranzaListView.as_view()), name='lista_inventario_banhavi_cobranza'),
    # crear
    path('inventario/banhavi_cobranza/crear/', login_required(InventarioBanhaviCobranzaCreateView.as_view()), name='crear_inventario_banhavi_cobranza'),
    # Editar
    path('inventario/banhavi_cobranza/editar/<int:pk>/', login_required(InventarioBanhaviCobranzaUpdateView.as_view()), name='editar_inventario_banhavi_cobranza'),
    # Eliminar
    path('inventario/banhavi_cobranza/eliminar/<int:pk>/', login_required(InventarioBanhaviCobranzaDeleteView.as_view()), name='eliminar_inventario_banhavi_cobranza'),
    ##################### Banhavi FAO #####################
    # listar
    path('inventario/banhavi_fao/lista/', login_required(InventarioBanhaviFaoListView.as_view()), name='lista_inventario_banhavi_fao'),
    # crear
    path('inventario/banhavi_fao/crear/', login_required(InventarioBanhaviFaoCreateView.as_view()), name='crear_inventario_banhavi_fao'),
    # Editar 
    path('inventario/banhavi_fao/editar/<int:pk>/', login_required(InventarioBanhaviFaoUpdateView.as_view()), name='editar_inventario_banhavi_fao'),
    # eliminar
    path('inventario/banhavi_fao/eliminar/<int:pk>/', login_required(InventarioBanhaviFaoDeleteView.as_view()), name='eliminar_inventario_banhavi_fao'),
    ##################### Barrio Nuevo Tricolor #####################
    # listar
    path('inventario/barrio_nuevo_tricolor/lista/', login_required(InventarioBarrioNuevoTricolorListView.as_view()), name='lista_inventario_bnbt'),
    # crear
    path('inventario/barrio_nuevo_tricolor/crear/', login_required(InventarioBarrioNuevoTricolorCreateView.as_view()), name='crear_inventario_bnbt'),
    # Editar
    path('inventario/barrio_nuevo_tricolor/editar/<int:pk>/', login_required(InventarioBarrioNuevoTricolorUpdateView.as_view()), name='editar_inventario_bnbt'),
    # Eliminar
    path('inventario/barrio_nuevo_tricolor/eliminar/<int:pk>/', login_required(InventarioBarrioNuevoTricolorDeleteView.as_view()), name='eliminar_inventario_bnbt'),
    ##################### Direccion #####################
    # listar
    path('inventario/direccion/lista/', login_required(InventarioDireccionListView.as_view()), name='lista_inventario_direccion'),
    # crear
    path('inventario/direccion/crear/', login_required(InventarioDireccionCreateView.as_view()), name='crear_inventario_direccion'),
    # Editar
    path('inventario/direccion/editar/<int:pk>/', login_required(InventarioDireccionUpdateView.as_view()), name='editar_inventario_direccion'),
    # Eliminar
    path('inventario/direccion/eliminar/<int:pk>/', login_required(InventarioDireccionDeleteView.as_view()), name='eliminar_inventario_direccion'),
    ##################### Gestion Humana #####################
    # listar
    path('inventario/gestionHumana/lista/', login_required(InventarioGestionHumanaListView.as_view()), name='lista_inventario_gestion_humana'),
    # crear
    path('inventario/gestionHumana/crear/', login_required(InventarioGestionHumanaCreateView.as_view()), name='crear_inventario_gestion_humana'),
    # Editar
    path('inventario/gestionHumana/editar/<int:pk>/', login_required(InventarioGestionHumanaUpdateView.as_view()), name='editar_inventario_gestion_humana'),
    # Eliminar
    path('inventario/gestionHumana/eliminar/<int:pk>/', login_required(InventarioGestionHumanaDeleteView.as_view()), name='eliminar_inventario_gestion_humana'),
    ##################### Inmobiliar Nacional #####################
    # listar
    path('inventario/inmobiliariaNacional/lista/', login_required(InventarioInmobiliariaNacionalListView.as_view()), name='lista_inventario_inmobiliaria_nacional'),
    # crear
    path('inventario/inmobiliariaNacional/crear/', login_required(InventarioInmobiliariaNacionalCreateView.as_view()), name='crear_inventario_inmobiliaria_nacional'),
    # Editar
    path('inventario/inmobiliariaNacional/editar/<int:pk>/', login_required(InventarioInmobiliarioNacionalUpdateView.as_view()), name='editar_inventario_inmobiliaria_nacional'),
    # Eliminar
    path('inventario/inmobiliariaNacional/eliminar/<int:pk>/', login_required(InventarioInmobiliariaNacionalDeleteView.as_view()), name='eliminar_inventario_inmobiliaria_nacional'),
    ##################### Intu #####################
    # listar
    path('inventario/intu/lista/', login_required(InventarioIntuListView.as_view()), name='lista_inventario_intu'),
    # crear
    path('inventario/intu/crear/', login_required(InventarioIntuCreateView.as_view()), name='crear_inventario_intu'),
    # Editar
    path('inventario/intu/editar/<int:pk>/', login_required(InventarioIntuUpdateView.as_view()), name='editar_inventario_intu'),
    # Eliminar
    path('inventario/intu/eliminar/<int:pk>/', login_required(InventarioIntuDeleteView.as_view()), name='eliminar_inventario_intu'),
    ##################### Obras #####################
    # listar
    path('inventario/obras/lista/', login_required(InventarioObrasListView.as_view()), name='lista_inventario_obras'),
    # crear
    path('inventario/obras/crear/', login_required(InventarioObrasCreateView.as_view()), name='crear_inventario_obras'),
    # Editar
    path('inventario/obras/editar/<int:pk>/', login_required(InventarioObrasUpdateView.as_view()), name='editar_inventario_obras'),
    # Eliminar
    path('inventario/obras/eliminar/<int:pk>/', login_required(InventarioObrasDeleteView.as_view()), name='eliminar_inventario_obras'),
    ##################### Redes Populares #####################
    # listar
    path('inventario/redes_populares/lista/', login_required(InventarioRedesPopularesListView.as_view()), name='lista_inventario_redes_populares'),
    # crear
    path('inventario/redes_populares/crear/', login_required(InventarioRedesPopularesCreateView.as_view()), name='crear_inventario_redes_populares'),
    # Editar
    path('inventario/redes_populares/editar/<int:pk>/', login_required(InventarioRedesPopularesUpdateView.as_view()), name='editar_inventario_redes_populares'),
    # Eliminar
    path('inventario/redes_populares/eliminar/<int:pk>/', login_required(InventarioRedesPopularesDeleteView.as_view()), name='eliminar_inventario_redes_populares'),
    ##################### Sala Situacional #####################
    # listar
    path('inventario/sala_situacional/lista/', login_required(InventarioSalaSituacionalListView.as_view()), name='lista_inventario_sala_situacional'),
    # crear
    path('inventario/sala_situacional/crear/', login_required(InventarioSalaSituacionalCreateView.as_view()), name='crear_inventario_sala_situacional'),
    # Editar
    path('inventario/sala_situacional/editar/<int:pk>/', login_required(InventarioSalaSituacionalUpdateView.as_view()), name='editar_inventario_sala_situacional'),
    # Eliminar
    path('inventario/sala_situacional/eliminar/<int:pk>/', login_required(InventarioSalaSituacionalDeleteView.as_view()), name='eliminar_inventario_sala_situacional'),
    ##################### Saren #####################
    # listar
    path('inventario/saren/lista/', login_required(InventarioSarenListView.as_view()), name='lista_inventario_saren'),
    # crear
    path('inventario/saren/crear/', login_required(InventarioSarenCreateView.as_view()), name='crear_inventario_saren'),
    # Editar
    path('inventario/saren/editar/<int:pk>/', login_required(InventarioSarenUpdateView.as_view()), name='editar_inventario_saren'),
    # Eliminar
    path('inventario/saren/eliminar/<int:pk>/', login_required(InventarioSarenDeleteView.as_view()), name='eliminar_inventario_saren'),
    ##################### Jubilados #####################
    # listar
    path('inventario/jubilados/lista/', login_required(InventarioJubiladosListView.as_view()), name='lista_inventario_jubilados'),
    # crear
    path('inventario/jubilados/crear/', login_required(InventarioJubiladosCreateView.as_view()), name='crear_inventario_jubilados'),
    # Editar
    path('inventario/jubilados/editar/<int:pk>/', login_required(InventarioJubiladosUpdateView.as_view()), name='editar_inventario_jubilados'),
    # Eliminar
    path('inventario/jubilados/eliminar/<int:pk>/', login_required(InventarioJubiladosDeleteView.as_view()), name='eliminar_inventario_jubilados'),
    ##################### Sistemas #####################
    # listar
    path('inventario/sistemas/lista/', login_required(InventarioSistemasListView.as_view()), name='lista_inventario_sistemas'),
    # Crear
    path('inventario/sistemas/crear/', login_required(InventarioSistemasCreateView.as_view()), name='crear_inventario_sistemas'),
    # Editar
    path('inventario/sistemas/editar/<int:pk>/', login_required(InventarioSistemasUpdateView.as_view()), name='editar_inventario_sistemas'),
    # Eliminar
    path('inventario/sistemas/eliminar/<int:pk>/', login_required(InventarioSistemasDeleteView.as_view()), name='eliminar_inventario_sistemas'),
    ##################### Sunavi #####################
    # listar
    path('inventario/sunavi/lista/', login_required(InventarioSunaviListView.as_view()), name='lista_inventario_sunavi'),
    # Crear
    path('inventario/sunavi/crear/', login_required(InventarioSunaviCreateView.as_view()), name='crear_inventario_sunavi'),
    # Editar
    path('inventario/sunavi/editar/<int:pk>/', login_required(InventarioSunaviUpdateView.as_view()), name='editar_inventario_sunavi'),
    # Eliminar
    path('inventario/sunavi/eliminar/<int:pk>/', login_required(InventarioSunaviDeleteView.as_view()), name='eliminar_inventario_sunavi'),
    ##################### Vivienda #####################
    # listar
    path('inventario/vivienda/lista/', login_required(InventarioViviendaListView.as_view()), name='lista_inventario_vivienda'),
    # Crear
    path('inventario/vivienda/crear/', login_required(InventarioViviendaCreateView.as_view()), name='crear_inventario_vivienda'),
    # Editar
    path('inventario/vivienda/editar/<int:pk>/', login_required(InventarioViviendaUpdateView.as_view()), name='editar_inventario_vivienda'),
    # Eliminar
    path('inventario/vivienda/eliminar/<int:pk>/', login_required(InventarioViviendaDeleteView.as_view()), name='eliminar_inventario_vivienda'),
]