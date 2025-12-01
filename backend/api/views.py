from django.shortcuts import render
from rest_framework import generics
from .models import Contrato
from .serializers import ContratoSerializer

class ContratoListCreateView(generics.ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
# Create your views here.
