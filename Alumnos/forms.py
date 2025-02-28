from django import forms
from .models import Alumno  # Asegúrate de importar el modelo correspondiente

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_edad'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_matricula'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_correo'}),
        }
