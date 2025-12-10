from django.contrib import admin
from .models import (
    CatBancos, CatCodigos, CatColonias,  CatControlSuministro, CatDescargaDrenaje,  CatDiametros, CatLineas,CatQuejasReportes,
    CatEncuestadores, CatEstadoMedidor, CatEstados, CatEstatusPredio, CatMateriales, CatMediosCaptacion, CatMenus, CatEstatusQueja,
    CatMpiosCp, CatQuejas, CatRutas, CatServicios, CatSubmenus,  CatTipoContrato,  CatTipoEmpleado,  CatTipoMedidor, CatMeses,
    CatTipoUsuario, CatTipoVivienda, CobroServicios, CalculosProcesados, ConceptoPago, ContratoCostos, Contratos, Empleados,
    Inventarios, MaterialServicios, Municipios, Pagos, Quejas, Sistema, Suministro, UserAccess, Usuarios)

class CatalogoBaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'estatus']
    list_display_links = ['id', 'descripcion']  # Hacer click en ID o descripción
    list_filter = ['estatus']
    search_fields = ['descripcion']
    ordering = ['descripcion']  # Orden alfabético por defecto
    list_per_page = 20
    
    # Acciones comunes
    actions = ['activar_registros', 'desactivar_registros']
    
    def activar_registros(self, request, queryset):
        queryset.update(estatus=1)
    activar_registros.short_description = "Activar registros seleccionados"
    
    def desactivar_registros(self, request, queryset):
        queryset.update(estatus=0)
    desactivar_registros.short_description = "Desactivar registros seleccionados"

@admin.register(CatBancos)
class CatBancosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatCodigos)
class CatCodigosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatColonias)
class CatColoniasAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatBancos)
class CatBancosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatControlSuministro)
class CatControlSuministroAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatDescargaDrenaje)
class CatDescargaDrenajeAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatDiametros)
class CatDiametrosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatLineas)
class CatLineasAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatQuejasReportes)
class CatQuejasReportesAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatEncuestadores)
class CatEncuestadoresAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatEstadoMedidor)
class CatEstadoMedidorAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatEstados)
class CatEstadosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatEstatusPredio)
class CatEstatusPredioAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatMateriales)
class CatMaterialesAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatMediosCaptacion)
class CatMediosCaptacionAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatMenus)
class CatMenusAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatEstatusQueja)
class CatEstatusQuejaAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatMpiosCp)
class CatMpiosCpAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatQuejas)
class CatQuejasAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatRutas)
class CatRutasAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatServicios)
class CatServiciosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatSubmenus)
class CatSubmenusAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatTipoEmpleado)
class CatTipoEmpleadoAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatTipoContrato)
class CatTipoContratoAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatTipoMedidor)
class CatTipoMedidorAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatMeses)
class CatMesesAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatTipoUsuario)
class CatTipoUsuarioAdmin(CatalogoBaseAdmin):
    pass
@admin.register(CatTipoVivienda)
class CatTipoViviendaAdmin(CatalogoBaseAdmin):
    pass
""" Comienza tablas principales """
@admin.register(CobroServicios)
class CobroServiciosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(ConceptoPago)
class ConceptoPagoAdmin(CatalogoBaseAdmin):
    pass
@admin.register(ContratoCostos)
class ContratoCostosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Contratos)
class ContratosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Empleados)
class EmpleadosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Inventarios)
class CInventariosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(MaterialServicios)
class MaterialServiciosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Municipios)
class MunicipiosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Pagos)
class PagosAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Quejas)
class QuejasAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Sistema)
class SistemaAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Suministro)
class SuministroAdmin(CatalogoBaseAdmin):
    pass
@admin.register(UserAccess)
class UserAccessAdmin(CatalogoBaseAdmin):
    pass
@admin.register(Usuarios)
class UsuariosAdmin(CatalogoBaseAdmin):
    pass


@admin.register(CalculosProcesados)
class CalculosProcesadosAdmin(admin.ModelAdmin):
    list_display = ['id', 'anio', 'mes', 'id_ruta', 'fecha_calculo','estatus']
    list_filter = ['anio', 'mes', 'id_ruta', 'fecha_calculo','estatus']
    search_fields = ['anio', 'mes', 'id_ruta', 'fecha_calculo','estatus']

