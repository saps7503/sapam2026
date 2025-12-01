from django.contrib import admin
from .models import Contrato

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombres', 'paterno', 'materno', 'estatus']
    list_filter = ['estatus']
    search_fields = ['nombres', 'paterno', 'materno']

