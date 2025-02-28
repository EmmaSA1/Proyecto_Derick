from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewSet

router = SimpleRouter()
router.register(r'productos', ProductoViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
