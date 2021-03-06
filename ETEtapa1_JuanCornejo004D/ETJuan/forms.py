from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaborador, TipoUsuario

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields =['rutColaborador', 'fotografiaColaborador', 'nombrecompletoColaborador', 'telefonoColaborador', 'direccionColaborador', 'emailColaborador', 'paisColaborador', 'constrase├▒aColaborador', 'tipousuario']
        labels ={
            'rutColaborador': 'Rut colaborador',
            'fotografiaColaborador': 'Fotografia colaborador',
            'nombrecompletoColaborador': 'Nombre completo colaborador',
            'telefonoColaborador': 'Telefono colaborador',
            'direccionColaborador': 'Direccion colaborador',
            'emailColaborador': 'Email colaborador',
            'paisColaborador': 'Pais colaborador',
            'constrase├▒aColaborador': 'Contrase├▒a colaborador',
            'tipousuario': 'Tipo usuario',
        }
        widgets={
            'rutColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut', 
                    'name': 'rut',
                    'placeholder': 'Digite rut'
                }
            ),
            'fotografiaColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'foto', 
                    'placeholder': 'Ingrese foto'

                }
            ), 
            'nombrecompletoColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre', 
                    'placeholder': 'Ingrese su nombre completo'

                }
            ),
            'telefonoColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono', 
                    'placeholder': 'Ingrese telefono'

                }
            ),
            'direccionColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion', 
                    'placeholder': 'Ingrese su direccion'

                }
            ),
            'emailColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email', 
                    'placeholder': 'Ingrese su email'

                }
            ),
            'paisColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'pais', 
                    'placeholder': 'Ingrese su pais'

                }
            ),
            'constrase├▒aColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contrase├▒a', 
                    'placeholder': 'Ingrese su contrase├▒a'

                }
            ),
            'tipousuario': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipousuario'
                }
            )
        }