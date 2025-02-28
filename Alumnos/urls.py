from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewSet, gestionAlumnos

router = SimpleRouter()
router.register(r'api', AlumnoViewSet) 

urlpatterns = [
    path('', include(router.urls)),  
    path('registrar/', gestionAlumnos, name='gestionar_alumnos'),  # Página para gestionar los alumnos
]
