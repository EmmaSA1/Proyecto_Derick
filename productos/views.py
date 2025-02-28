from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets #conjunto de vistas
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # me dice de donde saco el modelo y la info de la bd
    queryset = Producto.objects.all()
    #Retornar todos los productos de la base de datos 

    #Como serializar la información 
    serializer_class = ProductoSerializer

    #Como renderizar las respuestas 
    renderer_classes = [JSONRenderer]

    #Permitir filtrar los metos que se pueden usar 
    #GET, put, delete , post 
    #http_method_names = ['GET', 'POST']

    