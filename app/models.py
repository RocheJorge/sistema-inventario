"""Importaciones
    
    from django.db: Modelos traidos desde Django
    from simple_history.models: Registro del historial instalado de django-simple-history
"""


from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

# Clase Departamento
class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre
        
    class Meta:
        """Nombres que aparecen en el Admin de Django

            verbose_name: Singular
            verbose_name_plural: Plurals
        """
        
        
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamento'
        
# responsable del patrimonio
class ResponsablePatrimonio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    cedula = models.PositiveIntegerField()
    cargo = models.CharField(max_length=50, verbose_name='Cargo')
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Responsable del Patrimonio'
        verbose_name_plural = 'Responsable del Patrimonio'

# Jefe del departamento
class JefeDepartamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    cedula = models.PositiveIntegerField()
    cargo = models.CharField(max_length=50, verbose_name='Cargo')
    departamento = models.ForeignKey(Departamento, verbose_name='Jef@ del Departamento', on_delete=models.CASCADE)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Jefe del Departamento'
        verbose_name_plural = 'Jefe del Departamento'

# Direccion de Bienes
class DireccionBienes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    cedula = models.PositiveIntegerField()
    cargo = models.CharField(max_length=50, verbose_name='Cargo')
    history = HistoricalRecords()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Direccion de Bienes'
        verbose_name_plural = 'Direccion de Bienes'

# Inventario Base
class InventarioBase(models.Model):
    id = models.AutoField(primary_key= True)
    codigoDelBien = models.CharField(max_length=50, verbose_name='N° Provisional del Bien', unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    caracteristica = models.CharField(max_length=200, verbose_name='Caracteristicas')
    estado = models.CharField(max_length=50, verbose_name='Estado de Conservacion')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, verbose_name='Departamento')
    observacion = models.CharField(max_length=200, verbose_name='Observacion', null=True, blank=True)
    
    
    class Meta:
        """Meta creada para que los demas inventarios hereden sus atributos
        
            abstract: No aparecera en la base de datos pero todos heredaran sus atributos
        """

        
        abstract = True
        
# Inventario Administracion
class InventarioAdministracion(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Administracion'
        verbose_name_plural = 'Inventario Administracion'
        
# Inventario Asesoria legal
class InventarioAsesoriaLegal(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Asesoria Legal'
        verbose_name_plural = 'Inventario Asesoria Legal'
        
# Inventario Atencion al Ciudadano
class InventarioAtencionCiudadano(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Atencion Ciudadano'
        verbose_name_plural = 'Inventario Atencion Ciudadano'
        
# Inventario Banhavi Cobranza
class InventarioBanhaviCobranza(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Banhavi Cobranza'
        verbose_name_plural = 'Inventario Banhavi Cobranza'
        
# Inventario Banhavi FAO
class InventarioBanhaviFao(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Banhavi Fao'
        verbose_name_plural = 'Inventario Banhavi Fao'
        
# Inventario Barrio Nuevo Barrio Tricolor
class InventarioBarrioNuevoTricolor(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Barrio Nuevo Barrio Tricolor'
        verbose_name_plural = 'Inventario Barrio Nuevo Barrio Tricolor'
        
# Inventario Direccion
class InventarioDireccion(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Direccion'
        verbose_name_plural = 'Inventario Direccion'
        
# Inventario Gestion Humana
class InventarioGestionHumana(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Gestion Humana'
        verbose_name_plural = 'Inventario Gestion Humana'
        
# Inventario Inmobiliaria Nacional
class InventarioInmobiliariaNacional(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Inmobiliaria Nacional'
        verbose_name_plural = 'Inventario Inmobiliaria Nacional'
        
# Inventario Intu
class InventarioIntu(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Intu'
        verbose_name_plural = 'Inventario Intu'
        
# Inventario Obras
class InventarioObras(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Obras'
        verbose_name_plural = 'Inventario Obras'
        
# Inventario Redes Populares
class InventarioRedesPopulares(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Redes Populares'
        verbose_name_plural = 'Inventario Redes Populares'
        
# Inventario Sala Situacional
class InventarioSalaSituacional(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Sala Situacional'
        verbose_name_plural = 'Inventario Sala Situacional'
        
# Inventario Saren
class InventarioSaren(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Saren'
        verbose_name_plural = 'Inventario Saren'
        
# Inventario Jubilados
class InventarioJubilados(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Jubilados'
        verbose_name_plural = 'Inventario Jubilados'
        
# Inventario Sistemas
class InventarioSistemas(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Sistemas'
        verbose_name_plural = 'Inventario Sistemas'
        
# Inventario Sunavi
class InventarioSunavi(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Sunavi'
        verbose_name_plural = 'Inventario Sunavi'
        
# Inventario Vivienda
class InventarioVivienda(InventarioBase):
    history = HistoricalRecords()
    
    def __str__(self):
        return self.codigoDelBien
    
    class Meta:
        verbose_name = 'Inventario Vivienda'
        verbose_name_plural = 'Inventario Vivienda'