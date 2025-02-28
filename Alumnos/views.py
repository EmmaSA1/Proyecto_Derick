from django.shortcuts import render
from rest_framework import viewsets
from .models import Alumno  
from .serializers import AlumnoSerializer 
from .forms import AlumnoForm

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()  
    serializer_class = AlumnoSerializer  


def gestionAlumnos(request):
    alumnos = Alumno.objects.all()  # Obtén todos los alumnos
    form = AlumnoForm()  # Si tienes un formulario para agregar un alumno
    return render(request, 'Santos_Emmanuel.html', {'form': form, 'alumnos': alumnos})
