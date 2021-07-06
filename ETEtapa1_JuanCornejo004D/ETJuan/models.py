from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True, verbose_name='Id tipo de usuario')
    nombreTipoUsuario = models.CharField(max_length=50, verbose_name='Nombre tipo de usuario')

    def __str__(self):
        return self.nombreTipoUsuario


class Colaborador(models.Model):
    rutColaborador = models.CharField(max_length=9,primary_key=True, verbose_name='rut de colaborador')
    fotografiaColaborador = models.CharField(max_length=20, verbose_name='Fotografía colaborador')
    nombrecompletoColaborador = models.CharField(max_length=40, verbose_name='Nombre completo de colaborador')
    telefonoColaborador = models.IntegerField(verbose_name='Teléfono de colaborador')
    direccionColaborador = models.CharField(max_length=30, verbose_name='Dirección de colaborador')
    emailColaborador = models.CharField(max_length=20, verbose_name='Email de colaborador')
    paisColaborador = models.CharField(max_length=15, verbose_name='País de colaborador')
    constraseñaColaborador = models.CharField(max_length=8, verbose_name='Contraseña de colaborador')
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rutColaborador

