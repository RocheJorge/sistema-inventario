"""Importaciones
    
    from django.forms.models: Modelo form
    from django.forms: Input de Texto
    from .models: Modelos de MODELS.PY     
"""

from django.forms.models import ModelForm
from django.forms import TextInput
from .models import Departamento, JefeDepartamento, ResponsablePatrimonio, DireccionBienes, InventarioAdministracion, InventarioAsesoriaLegal, InventarioAtencionCiudadano, InventarioBanhaviCobranza, InventarioBanhaviFao, InventarioBarrioNuevoTricolor, InventarioDireccion, InventarioGestionHumana, InventarioInmobiliariaNacional, InventarioIntu, InventarioObras, InventarioRedesPopulares, InventarioSalaSituacional, InventarioSaren, InventarioJubilados, InventarioSistemas, InventarioSunavi, InventarioVivienda

'''""""""""""""""""" Form del Departamento """""""""""""""""""""""""""'''

class RegistrarDepartamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        """Personaliza el Formulario
        
        Argumentos:
            form.field.widget.attrs: Asigna atributos a los INPUTS 
        
        """
        
        
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        """Propiedades de los inputs
        
        Argumentos:
            model: Modelo a usar de MODELS.PY
            fields: Atributos a mostrar de MODELS.PY
            widgets: Modifica los componentes de los INPUTS
            
            
        Returns:
            una consulta
        """
        
        
        model = Departamento
        fields = '__all__'
        widgets = {
            'nombre': TextInput (
                attrs={
                    'placeholder': 'Ingrese un nombre'
                }
            )
        }
        
'''"""""""" Form de los Jefes de Departamentos """"""""""""""'''

class JefeDepartamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = JefeDepartamento
        fields = '__all__'
        widgets = {
            'nombre': TextInput (
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            ),
            'apellido': TextInput (
                attrs={
                    'placeholder': 'Ingrese apellido'
                }
            ),
            'cedula': TextInput (
                attrs={
                    'placeholder': 'Ingrese cedula'
                }
            ),
            'cargo': TextInput (
                attrs={
                    'placeholder': 'Ingrese cargo'
                }
            )
        }
    
'''"""""""" Form del Responsable del Patrimonio """"""""""""""'''

class ResponsablePatrimonioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = ResponsablePatrimonio
        fields = '__all__'
        widgets = {
            'nombre': TextInput (
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            ),
            'apellido': TextInput (
                attrs={
                    'placeholder': 'Ingrese apellido'
                }
            ),
            'cedula': TextInput (
                attrs={
                    'placeholder': 'Ingrese cedula'
                }
            ),
            'cargo': TextInput (
                attrs={
                    'placeholder': 'Ingrese cargo'
                }
            )
        }
    
'''"""""""" Form de Direccion de Bienes """"""""""""""'''

class DireccionBienesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = DireccionBienes
        fields = '__all__'
        widgets = {
            'nombre': TextInput (
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            ),
            'apellido': TextInput (
                attrs={
                    'placeholder': 'Ingrese apellido'
                }
            ),
            'cedula': TextInput (
                attrs={
                    'placeholder': 'Ingrese cedula'
                }
            ),
            'cargo': TextInput (
                attrs={
                    'placeholder': 'Ingrese cargo'
                }
            )
        }
        
'''"""""""" Form de Inventarios """"""""""""""'''

class InventarioBaseForm(ModelForm):
    """Formulario Padre

    Argumentos:
        ModelForm (parametro): FORMS de Django
    """
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['codigoDelBien'].widget.attrs['autofocus'] = True
        
    class Meta:
        fields = '__all__'
        widgets = {
            'codigoDelBien': TextInput (
                attrs={
                    'placeholder': 'INGRESE NUMERO DEL BIEN'
                }
            ),
            'nombre': TextInput (
                attrs={
                    'placeholder': 'INGRESE NOMBRE DEL BIEN'
                }
            ),
            'descripcion': TextInput (
                attrs={
                    'placeholder': 'INGRESE DESCRIPCION DEL BIEN'
                }
            ),
            'caracteristica': TextInput (
                attrs={
                    'placeholder': 'INGRESE CARACTERISTICAS DEL BIEN'
                }
            ),
            'estado': TextInput (
                attrs={
                    'placeholder': 'INGRESE ESTADO EN EL QUE SE ENCUENTRA EL ARTICULO (BUENO, MALO, REGULAR ETC..)'
                }
            ),
            'observacion': TextInput (
                attrs={
                    'placeholder': 'INGRESE OBSERVACION DEL ARTICULO'
                }
            )
        }

# Administracion

class InventarioForm(InventarioBaseForm):
    """Inventarios que heredan de InventarioBaseForm ya que todos los formularios poseen los mismos INPUTS

    Argumentos:
        InventarioBaseForm (herencia): Herencia del InventarioBaseForm
    """
    
    
    class Meta(InventarioBaseForm.Meta):
        """Esto se hace para que hereden todos los INPUTS

        Argumentos:
            InventarioBaseForm (InventarioBaseForm.Meta): Tomamos todos los INPUTS y sus estilos
            model: Modelo de MODELS.PY
        """
        
        
        model = InventarioAdministracion

# Asesoria Legal
class InventarioAsesoriaLegalForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioAsesoriaLegal
        
# Atencion al Ciudadano
class InventarioAtencionCiudadanoForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioAtencionCiudadano
        
# Banhavi Cobranza
class InventarioBanhaviCobranzaForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioBanhaviCobranza
        
# Banhavi Fao
class InventarioBanhaviFaoForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioBanhaviFao
        
# Barrio Nuevo Barrio Tricolor
class InventarioBarrioNuevoTricolorForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioBarrioNuevoTricolor
        
# Direccion
class InventarioDireccionForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioDireccion
        
# Gestion Humana
class InventarioGestionHumanaForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioGestionHumana
        
# Inmobiliaria Nacional
class InventarioInmobiliariaNacionalForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioInmobiliariaNacional
        
# Intu
class InventarioIntuForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioIntu
        
# Obras
class InventarioObrasForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioObras
        
# Redes Populares
class InventarioRedesPopularesForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioRedesPopulares
        
# Sala Situacional
class InventarioSalaSituacionalForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioSalaSituacional
        
# Saren
class InventarioSarenForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioSaren
        
# Jubilados
class InventarioJubiladosForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioJubilados
        
# Sistemas
class InventarioSistemasForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioSistemas
        
# Sunavi
class InventarioSunaviForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioSunavi
    
# Vivienda

class InventarioViviendaForm(InventarioBaseForm):
    class Meta(InventarioBaseForm.Meta):
        model = InventarioVivienda