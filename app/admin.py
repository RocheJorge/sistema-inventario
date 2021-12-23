""" Django Admin

    from django.contrib: Administracion de Django
    from .models: Modelos de MODELS.PY
    admin.site.register: Modelos que queremos ver en Django Admin
"""


from django.contrib import admin
from .models import Departamento, ResponsablePatrimonio, JefeDepartamento, DireccionBienes, InventarioAdministracion, InventarioAsesoriaLegal, InventarioAtencionCiudadano, InventarioBanhaviCobranza, InventarioBanhaviFao, InventarioBarrioNuevoTricolor, InventarioDireccion, InventarioGestionHumana, InventarioInmobiliariaNacional, InventarioIntu, InventarioObras, InventarioRedesPopulares, InventarioSalaSituacional, InventarioSaren, InventarioJubilados, InventarioSistemas, InventarioSunavi, InventarioVivienda
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Departamento,SimpleHistoryAdmin)
admin.site.register(ResponsablePatrimonio,SimpleHistoryAdmin)
admin.site.register(JefeDepartamento,SimpleHistoryAdmin)
admin.site.register(DireccionBienes,SimpleHistoryAdmin)
admin.site.register(InventarioAdministracion,SimpleHistoryAdmin)
admin.site.register(InventarioAsesoriaLegal,SimpleHistoryAdmin)
admin.site.register(InventarioAtencionCiudadano,SimpleHistoryAdmin)
admin.site.register(InventarioBanhaviCobranza,SimpleHistoryAdmin)
admin.site.register(InventarioBanhaviFao,SimpleHistoryAdmin)
admin.site.register(InventarioBarrioNuevoTricolor,SimpleHistoryAdmin)
admin.site.register(InventarioDireccion,SimpleHistoryAdmin)
admin.site.register(InventarioGestionHumana,SimpleHistoryAdmin)
admin.site.register(InventarioInmobiliariaNacional,SimpleHistoryAdmin)
admin.site.register(InventarioIntu,SimpleHistoryAdmin)
admin.site.register(InventarioObras,SimpleHistoryAdmin)
admin.site.register(InventarioRedesPopulares,SimpleHistoryAdmin)
admin.site.register(InventarioSalaSituacional,SimpleHistoryAdmin)
admin.site.register(InventarioSaren,SimpleHistoryAdmin)
admin.site.register(InventarioJubilados,SimpleHistoryAdmin)
admin.site.register(InventarioSistemas,SimpleHistoryAdmin)
admin.site.register(InventarioSunavi,SimpleHistoryAdmin)
admin.site.register(InventarioVivienda,SimpleHistoryAdmin)