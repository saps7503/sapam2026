from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# ========== CLASE BASE COMÚN ==========

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = None  # Se define en cada hijo
    serializer_class = None
    
    def get_queryset(self):
        # Filtro por estatus
        estatus = self.request.query_params.get('estatus')
        if estatus:
            return self.queryset.filter(estatus=estatus)
        return self.queryset.filter(estatus=1)

# ========= Catalogos =====================
CatBancosViewSet = type('CatBancosViewSet', (CatalogoViewSet,), {
    'queryset': CatBancos.objects.all(),
    'serializer_class': CatBancosSerializer
})
CatCodigosViewSet = type('CatCodigosViewSet', (CatalogoViewSet,), {
    'queryset': CatCodigos.objects.all(),
    'serializer_class': CatCodigosSerializer
})
# ========== MODELOS ESPECIALES ==========

UsuariosViewSet = type('UsuariosViewSet', (CatalogoViewSet,), {
    'queryset': Usuarios.objects.all(),
    'serializer_class': UsuariosSerializer
})

EmpleadosViewSet = type('EmpleadosViewSet', (CatalogoViewSet,), {
    'queryset': Empleados.objects.all(),
    'serializer_class': EmpleadosSerializer
})
