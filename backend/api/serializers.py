from rest_framework import serializers
from .models import (
    CatBancos, CatCodigos, CatColonias,  CatControlSuministro, CatDescargaDrenaje,  CatDiametros, CatLineas,CatQuejasReportes,
    CatEncuestadores, CatEstadoMedidor, CatEstados, CatEstatusPredio, CatMateriales, CatMediosCaptacion, CatMenus, CatEstatusQueja,
    CatMpiosCp, CatQuejas, CatRutas, CatServicios, CatSubmenus,  CatTipoContrato,  CatTipoEmpleado,  CatTipoMedidor, CatMeses,
    CatTipoUsuario, CatTipoVivienda, CobroServicios, CalculosProcesados, ConceptoPago, ContratoCostos, Contratos, Empleados,
    Inventarios, MaterialServicios, Municipios, Pagos, Quejas, Sistema, Suministro, UserAccess, Usuarios)

# ========== SERIALIZERS BASE ==========

class CatalogoBaseSerializer(serializers.ModelSerializer):
    """Serializer base para todos los catálogos"""
    class Meta:
        fields = "__all__"
    
    # Puedes agregar validaciones comunes aquí
    def validate_descripcion(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("La descripción debe tener al menos 3 caracteres")
        return value

# ========== CATÁLOGOS GENÉRICOS ==========
class CatBancosSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatBancos

class CatCodigosSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatCodigos

class CatColoniasSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatColonias

class CatControlSuministroSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatControlSuministro

class CatDescargaDrenajeSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatDescargaDrenaje

class CatDiametrosSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatDiametros

class CatLineasSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatLineas

class CatQuejasReportesSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatQuejasReportes

class CatEncuestadoresSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatEncuestadores

class CatEstadoMedidorSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatEstadoMedidor

class CatEstadosSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatEstados

class CatEstatusPredioSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatEstatusPredio

class CatMaterialesSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatMateriales

class CatMediosCaptacionSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatMediosCaptacion

class CatMenusSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatMenus

class CatEstatusQuejaSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatEstatusQueja

class CatMpiosCpSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatMpiosCp

class CatQuejasSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatQuejas

class CatRutasSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatRutas

class CatServiciosSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatServicios

class CatSubmenusSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatSubmenus

class CatTipoContratoSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatTipoContrato

class CatTipoEmpleadoSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatTipoEmpleado

class CatTipoMedidorSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatTipoMedidor

class CatMesesSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatMeses

class CatTipoUsuarioSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatTipoUsuario

class CatTipoViviendaSerializer(CatalogoBaseSerializer):
    class Meta(CatalogoBaseSerializer.Meta):
        model = CatTipoVivienda

# ========== MODELOS ESPECIALES ==========

class CobroServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CobroServicios
        fields = "__all__"

class CalculosProcesadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculosProcesados
        fields = "__all__"

class ConceptoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoPago
        fields = "__all__"

class ContratoCostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoCostos
        fields = "__all__"

class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratos
        fields = "__all__"

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = "__all__"

class InventariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventarios
        fields = "__all__"

class MaterialServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialServicios
        fields = "__all__"

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = "__all__"

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = "__all__"

class QuejasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quejas
        fields = "__all__"

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = "__all__"

class SuministroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suministro
        fields = "__all__"

class UserAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccess
        fields = "__all__"

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = "__all__"