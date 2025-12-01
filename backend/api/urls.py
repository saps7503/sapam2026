from django.urls import path
from .views import ContratoListCreateView

urlpatterns = [
    path('contratos/', ContratoListCreateView.as_view(), name='contratos'),
]