from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario

# creamos la clase del formulario
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['username'].widget.attrs['autofocus'] = True
        
# Formulario de creacion usuario

class FormularioUsuario(forms.ModelForm):
    """Formulario de Registro de un Usuario en la base de datos

    Variables:
        password1: contraseña
        password2: verificacion de contraseña
    """
    
    
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))
    
    password2 = forms.CharField(label = 'Contraseña de confirmacion', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Nuevamente su Contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))
    
    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Correo Electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus Apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre de Usuario',
                }
            ),
        }

    def clean_password2(self):
        """Validacion de Contraseña
        
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas y guardadas en la base de datos, Retornar la contraseña validada.
        
        Excepciones:
            ValidationError: Cuando las contraseñas no son iguales muestra un mensaje de error
            
        cleaned_data: Envia la informacion que ya esta limpia a la base de datos
        """
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseña no coincide')
        return password2
    
    # Aqui es donde se encripta la contraseña con set_password
    def save(self,commit=True): # commit indica que proceda con el registro
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user