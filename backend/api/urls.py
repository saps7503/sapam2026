from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

catalogos = [
    (CatBancosViewSet, 'cat-bancos'),
    (CatCodigosViewSet, 'cat-codigos'),
    # ... todos los catalogos
]
for viewset, basename in catalogos:
    router.register(basename, viewset, basename=basename)

# Modelos especiales poner todos los demas
router.register('usuarios', UsuariosViewSet)
router.register('empleados', EmpleadosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]