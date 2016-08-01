from django import forms
from transporte.models import Vehiculo
from transporte.models import Conductor
from transporte.models import RutaVehiculo
from transporte.models import Ruta


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo

        fields = [
            'id_est',
            'placa',
            'numero_gsm',
            'codigo',
            'estado',
        ]

        labels = {
            'id_est': 'Establecimiento',
            'placa': 'Placa',
            'numero_gsm': 'Numero',
            'codigo': 'Codigo',
            'estado': 'Estado',
        }

        widgets = {
            'id_est': forms.Select(attrs={'class':'form-control'}),
            'placa': forms.TextInput(attrs={'class':'form-control'}),
            'numero_gsm': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
        }



class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor

        fields = [
            'id_vehiculo',
            'nombres',
            'apellidos',
            'edad',
            'cedula',
            'telefono',
            'correo',
        ]

        labels = {
            'id_vehiculo': 'Codigo Vehiculo',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'cedula': 'Cedula',
            'telefono': 'Telefono',
            'correo': 'Correo',
        }

        widgets = {
            'id_vehiculo': forms.Select(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        correo_base, provider = correo.split("@")
        domain, extension = provider.split('.')
        if not domain == "hotmail":
            raise forms.ValidationError("Ingrese un correo hotmail.")
        return correo

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        return cedula

    def clean_id_vehiculo(self):
        id_vehiculo = self.cleaned_data.get('id_vehiculo')
        return id_vehiculo

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        return telefono

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        return edad

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        return apellidos

    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')
        return nombres

class RutaVehiculoForm(forms.ModelForm):
    class Meta:
        model = RutaVehiculo
        fields = [
            'id_ruta',
            'id_vehiculo',
        ]

        labels = {
            'id_ruta': 'Ruta',
            'id_vehiculo': 'Vehiculo',
        }

        widgets = {
            'id_ruta': forms.Select(attrs={'class': 'form-control'}),
            'id_vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }