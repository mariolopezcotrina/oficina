from math import fabs
from django.db import models
from .authManager import AuthManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class Banco(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'bancos'

class ClienteMarcaOficina(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    ppto = models.CharField(max_length=45, null=False)
    class Meta:
        db_table = 'clienteMarcas'

class Usuario(models.Model):
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    dni = models.CharField(max_length=25, null=False)
    rol = models.CharField(max_length=50, choices=(['ADMINISTRADOR','ADMINISTRADOR'],['USUARIO','USUARIO']))
    validado = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='creado')
    updateAt = models.DateTimeField(auto_now=True, db_column='actualizado')

    #================================================
    #TODOs LO SIGUIENTE ES NETAMENTE SI UTILIZAMOS EL PANEL ADMIN

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = AuthManager()
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre','apellidos','rol']

    class Meta:
        db_table = 'usuarios'

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipoDocumento = models.CharField(max_length=50, choices=(['DNI','DNI'],['RUC','RUC'],['CARNET_EXTRANJERIA','CARNET_EXTRANJERIA']))
    numDocumento = models.CharField(max_length=50, null=False)
    banco = models.ForeignKey(to=Banco, on_delete=models.PROTECT, related_name='contactos')
    numCuenta = models.CharField(max_length=50)

    class Meta:
        db_table = 'contactos'

class Movilidad(models.Model):
    periodo = models.CharField(max_length=45)
    fechaEmision = models.DateField()
    fechaGasto = models.DateField()
    motivo = models.CharField(max_length=200, null=False)
    destino = models.CharField(max_length=200)
    precioIda = models.CharField(max_length=25)
    precioVuelta = models.CharField(max_length=25)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, related_name='movilidades')

    class Meta:
        db_table = 'movilidades'

class Requerimiento(models.Model):
    fechaSolicitud = models.DateField()
    fechaEntrega = models.DateField()
    tipoMoneda = models.CharField(max_length=45, choices=(['DOLAR','DOLAR'],['SOLES','SOLES']))
    montoSuma = models.CharField(max_length=50, null=False)
    actividad = models.CharField(max_length=45, null=False)
    concepto = models.CharField(max_length=45, null=False)
    detalle = models.CharField(max_length=100, null=False)
    estado = models.BooleanField(default=False)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, related_name='requerimientos')
    contacto = models.ForeignKey(to=Contacto, on_delete=models.PROTECT, related_name='requerimientos')
    clienteMarca = models.ForeignKey(to=ClienteMarcaOficina, on_delete=models.PROTECT, related_name='requerimientos')

    class Meta:
        db_table = 'requerimientos'

class Liquidacion(models.Model):
    fechaLiquidacion = models.DateField()
    fechaEmisionDocumento = models.DateField()
    documento = models.CharField