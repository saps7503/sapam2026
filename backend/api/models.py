from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CalculosProcesados(models.Model):
      ESTATUS_CHOICES =  [
      (1, 'Activo'),
      (2, 'Inactivo'),
      ]
      id     = models.AutoField(primary_key=True) 
      anio   = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
      mes    = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
      id_ruta = models.IntegerField()
      fecha_calculo = models.DateField()
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
          db_table = 'calculos_procesados'
          managed = False
      def __str__(self):
       return f"{self.id} - {self.id_ruta} ({self.anio}/{self.mes:02d})" 

class CatBancos(models.Model): 
      ESTATUS_CHOICES =  [
      (1, 'Activo'),
      (2, 'Inactivo'),
      ]
      id  = models.AutoField(primary_key=True) 
      descripcion = models.CharField(max_length=60)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
          db_table = 'cat_bancos'
          managed = False
            
      def __str__(self):
       return f"{self.id} - {self.descripcion}"
        
class CatCodigos(models.Model):
        id = models.AutoField(primary_key=True) 
        IdLocalidad = models.IntegerField()
        IdZona = models.IntegerField()
        IdAsentamiento = models.IntegerField()
        DescColonia = models.CharField(max_length=150)
        class Meta:
          db_table = 'cat_codigos'
          managed = False
          
        def __str__(self):
         return f"{self.id} - {self.DescColonia}"
        
class CatColonias(models.Model):
        id = models.AutoField(primary_key=True)   
        idEstado = models.IntegerField()
        idMunicipio = models.IntegerField()
        descripcion = models.CharField(max_length=160)
        codigo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
        class Meta:
          db_table = 'cat_colonias'
          managed = False
              
        def __str__(self):
          return f"{self.id} - {self.descripcion}"
        
class CatControlSuministro(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
          db_table= 'cat_controlsuministro'
          managed = False
          
      def __str__(self):
        return f"{self.id} - {self.descripcion}"
        
class CatDescargaDrenaje(models.Model):
      ESTATUS_CHOICES =  [
              (1, 'Activo'),
              (2, 'Inactivo'),
      ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
          db_table = 'cat_descargadrenaje'
          managed = False
        
      def __str__(self):
        return f"{self.id} - {sel.decripcion}"

class CatDiametros(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table= 'cat_diametros'
        managed = False
            
      def __str__(self):
       return f"{self.id} - {self.decripcion}"

class CatEncuestadores(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      fechaContrato = models.DateField()
      paterno = models.CharField(max_length=20)
      materno = models.CharField(max_length=20)
      nombre = models.CharField(max_length=20)
      domicilio = models.CharField(max_length=60)
      numero = models.CharField(max_length=5)
      colonia = models.CharField(max_length=20)
      telFijo = models.CharField(max_length=20)
      telCelular = models.CharField(max_length=20)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_encuestadores'
        mandaged = False
        
      def __str__(self):
        return f"{self.id} - ({self.paterno} {self.materno} {self.nombre})"
	
class CatEstadoMedidor(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_estadomedidor'
        managed = False
      
      def __str__(self):
        return f"{self.id} - {self.descripcion}"
	
class CatEstados(models.Model):
      idEstado = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=40)
      DescCURPEntidad = models.CharField(max_length=2)
      class Meta:
        db_Table = 'cat_estados'
        managed = False
              
      def __str__(self):
        return f"{self.id} - {self.descripcion}"
        
class CatEstatusPredio(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_estatuspredio'
        managed = False
            
      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class CatMateriales(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_materiales'
        managed = False
        
      def __str__(self):  
        return f"{self.id} - {self.descripcion}"

class CatMediosCaptacion(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_medioscaptacion'
        managed = False
      
      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class CatMenus(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_menus'
        managed= False

      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class CatMpiosCp (models.Model):
        id = models.AutoField(primary_key=True)
        idEstado = models.IntegerField()
        claveMunicipio = models.IntegerField()
        nombreMunicipio = models.CharField(max_length=150)
        siglas = models.CharField(max_length=11)
        class Meta:
          db_table = 'cat_mpios_cp'
          managed = False
 
        def __str_(self):
          return f"{self.id} - {self.nombreMunicipio}"

class CatQuejas(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_quejas'
        managed = False
      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class CatRutas(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=30)
      colonias = models.TextField()
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_rutas'
        managed = False
      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class CatServicios(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      descripcion = models.CharField(max_length=65)
      detalles = models.CharField(max_length=250)
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      fechUltimaMoficicacion = models.DateField(null=True, blank=True)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_servicios'
        nabaged = False
      def __str__(self):  
        return f"{self.id}  {self.descriçion}"
	  
class CatSubmenus(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)   
      idMenu = models.IntegerField()
      descripcion = models.CharField(max_length=65)
      nombre_frm = models.CharField(max_length=35)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_submenus'
        nabaged = False
      def __str__(self):  
        return f"{self.id} {self.descriçion}"
          
class CatTipoContrato(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key=True)
      idTipoContrato = models.IntegerField()
      descripcion = models.CharField(max_length=30)
      caracteristicas = models.CharField(max_length=150)
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      anio = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
      class Meta:
        db_tabe = 'cat_tipocontrato'
        managed = False
      
      def __str__(self):
        return f"{self.id}  {self.descriçion}"
	
class CatTipoEmpleado(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      descripcion = models.models.CharField(nax_length=20)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_tipoempleado'
        managed = False
      
      def __str__(self):
        return f"{self.id} {self.descriçion}"

class CatTipoMedidor(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      descripcion = models.models.CharField(nax_length=20)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_tipomedidor'
        managed = False
      
      def __str__(self):
        return f"{self.id} {self.descriçion}"

class CatTipoUsuario(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      descripcion = models.models.CharField(nax_length=20)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_tipousuario'
        managed = False
      
      def __str__(self):
       return f"{self.id}  {self.descriçion}"
	
class CatTipoVivienda(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      descripcion = models.models.CharField(nax_length=20)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_tipovivienda'
        managed = False
      
      def __str__(self):
        return f"{self.id} {self.descriçion}"
	
class CobroServicios(models.Model):
      id = models.UUIDField(primary_key=True, editable=False)
      idEmpleado = models.IntegerField()
      idServicio = models.IntegerField()
      estatus = models.IntegerField()
      forma_pago = models.models.IntegerField()
      idbanco = models.models.IntegerField()
      fechaCobro = models.DateField()
      folio = models.CharField(max_length=15)
      contratosistema = models.CharField(max_length=22)
      idContrato = models.CharField(max_length=38)
      horaCobro = models.CharField(max_length=15)
      descripcion = models.CharField(max_length=65)
      contribuyente = models.CharField(max_length=85)
      observaciones = models.CharField(max_length=125)
      num_tarjeta = models.CharField(max_length=16)
      voucher = models.CharField(max_length=20)
      deuda_total = models.DecimalField(max_digits=12, decimal_places=2)
      imp_pago_real = models.DecimalField(max_digits=12, decimal_places=2)
      porc_desc = models.IntegerField()
      importe_desc = models.DecimalField(max_digits=12, decimal_places=2)
      importe_cobrado = models.DecimalField(max_digits=12, decimal_places=2)
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      cambio = models.DecimalField(max_digits=12, decimal_places=2)
      saldo = models.DecimalField(max_digits=12, decimal_places=2)
      class Meta:
        db_table = 'cobros_servicios'
        managed = False
      def __str__(self):
        return f"{self.id} {self.fechaCobro}"

class ConceptoPago(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      clave =models.CharField(max_length=3)
      descripcion = models.CharField(max_length=80)
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'conceptos_pago'
        managed = False
      def __str__(self):  
        return f"{self.id}  {self.descripcion}"

class ContratoCostos(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      idContrato = models.IntegerField()
      idTipoContrato = models.IntegerField()
      idServicio = models.IntegerField()
      fechaContrato = models.DateField()
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'contrato_costos'
        managed = False
      def __str__(self):
        return f"{self.id} {self.importe}"
	
class Contratos(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.UUIDField(primary_key=True,editable=False)
      idEstado = models.IntegerField()
      idMunicipio = models.IntegerField()
      idTipoVivienda = models.IntegerField()
      idColonia = models.IntegerField()
      idTipoContrato = models.IntegerField()
      idControlSuministro = models.IntegerField()
      idEstadoMedidor = models.IntegerField()
      idDiametro = models.IntegerField()
      idMaterialBanqueta = models.IntegerField()	
      idMaterialCalle = models.IntegerField()
      idMediosCaptacion = models.IntegerField()	
      idDescargaDrenaje = models.IntegerField()	
      idEstatusPredio = models.IntegerField()
      idEmpleado = models.IntegerField()
      fechaEncuesta = models.DateField()
      fechaContrato = models.DateField()
      folio = models.CharField(max_length=10)
      idRuta = models.IntegerField()
      manzana = models.CharField(max_length=3)
      predio = models.CharField(max_length=6)
      latitud = models.CharField(max_length=25)
      longitud = models.CharField(max_length=25)
      otraViv = models.CharField(max_length=60)
      nombreContrato = models.CharField(max_length=65)
      paterno = models.CharField(max_length=25)
      materno = models.CharField(max_length=25)
      nombres = models.CharField(max_length=25)
      domicilio = models.CharField(max_length=60)
      numero = models.CharField(max_length=5)
      cp = models.IntegerField()
      telFijo = models.CharField(max_length=15)
      telCelular = models.CharField(max_length=15)
      referenciaDomicilio = models.CharField(max_length=250)
      numHabitantes = models.IntegerField()
      aguaPotable = models.CharField(max_length=1)
      alcantarillado = models.CharField(max_length=1)
      luzElectrica = models.CharField(max_length=1)
      otroServicio = models.CharField(max_length=65)
      comoAbasteceAgua = models.CharField(max_length=160)
      contrato = models.CharField(max_length=1)
      numeroContrato =   models.CharField(max_length=10)
      numMedidor = models.IntegerField()
      marcaMedidor = models.CharField(max_length=15)
      idtipoMedidor = models.IntegerField()
      numTomas = models.IntegerField()
      capacidadCaptacion = models.CharField(max_length=1)
      jardin = models.CharField(max_length=1)
      alberca = models.CharField(max_length=1)
      numRecamaras = models.IntegerField()
      numSanitarios = models.IntegerField()
      observaciones = models.CharField(max_length=350)
      contratosistema = models.CharField(max_length=22)
      anio_contrato = models.IntegerField()
      mes_contrato = models.IntegerField()
      estatus =  models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'contratos'
        managed = False  
           
      def __str__(self):
        return f"{self.id}  {self.nombreContrato}"

class Empleados(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.AutoField(primary_key = True)
      idPuesto = models.IntegerField()
      fechaIngreso =  models.DateField()
      paterno = models.CharField(max_length=25)
      materno = models.CharField(max_length=25)
      nombres = models.CharField(max_length=25)
      sexo = models.CharField(max_length=1)
      fechaNacimiento = models.DateField()
      domicilio = models.CharField(max_length=20)
      numero = models.CharField(max_length=6)
      cp = models.IntegerField()
      idColonia = models.BigIntegerField()
      colonia = models.CharField(max_length=65)
      idEstado = models.IntegerField()
      idMunicipio= models.IntegerField()
      telCasa = models.CharField(max_length=15)
      telMovil = models.CharField(max_length=15)
      email = models.EmailField(unique=True)
      fechaBaja = models.DateField()
      fechaUpd = models.DateField()
      idUsuario = models.IntegerField()
      foto =  models.ImageField(upload_to='imagenes/', null=True, blank=True)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
            db_table = 'empleados'
            managed = False
      def  __str__(self):
        return f"{self.id} {self.nombres}"
      
class CatEstados(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
	    ]
      id = models.UUIDField(primary_key=True,editable=False)
      descripcion = models.CharField(max_lengthdigits=80)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_estados'
        managed = False
      def __str__(self):
        return f"{self.id} {self.descripcion}"

class CatEstatusQueja(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.AutoField(primary_key = True)
      descripcion = models.CharField(max_lengthdigits=80)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_estatus_queja'
        managed = False
      def __str__(self):
        return f"{self.id} {self.descripcion}"

class Inventarios(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.UUIDField(primary_key=True,editable=False)
      idEmpleado = models.IntegerField()
      idAlmacen = models.IntegerField()
      idLinea = models.IntegerField()
      idUMedida = models.IntegerField()
      medida = models.IntegerField()
      descripcion = models.CharField(max_length=150)
      imagenRuta = models.CharField(max_length=255)
      marca = models.CharField(max_length=15)
      modelo = models.CharField(max_length=15)
      color = models.CharField(max_length=15)
      num_serie = models.CharField(max_length=25)
      contNeto = models.DecimalField(max_digits=12, decimal_places=2)
      lote = models.IntegerField()
      caduca  = models.CharField(max_length=1)
      fechaCaduca = models.DateField()
      fechaRegistro = models.DateField()
      fechaUltimaUpd = models.DateField()
      stockActual = models.IntegerField()
      stockMinimo = models.IntegerField()
      precioCompra = models.DecimalField(max_digits=12, decimal_places=2)
      precioVenta = models.DecimalField(max_digits=12, decimal_places=2)
      observaciones  = models.CharField(max_length=125)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'invetarios'
        managed =  False
      def __str__(self):
        return f"{self.id}  {self.descripcion}"

class CatLineas(models.Model):        
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.AutoField(primary_key = True)
      descipcion = models.CharField(max_length = 45)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_lineas'
        managed =  False
      def __str__(self):
        return f"{self.id}  {self.descripcion}"

class MaterialServicios(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id =  models.AutoField(primary_key = True)
      idServicio = models.IntegerField()
      material = models.CharField(max_length= 60)
      importe = models.DecimalField(max_digits=12, decimal_places=2)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'material_servicios'
        managed = False
      def __str__(self):
        return f"{self.id} - {self.material}"

class CatMeses(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 12)
    class Meta:
      db_table = 'cat_meses'
      managed = False
    def __str__(self):
      return f"{self.id} - {id.descripcion}"

class Municipios(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.UUIDField(primary_key=True,editable=False)
      idEstado = models.UUIDField()
      descripcion = models.CharField(max_length = 150)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
         db_table = 'municipios'
         managed = False
      def __str__(self):
         return f"{self.id} - {self.descripcion}"

class Pagos(models.Model):
         id = models.UUIDField(primary_key=True,editable=False)
         idContrato = models.UUIDField(max_length= 38)
         anio = models.IntegerField()
         idRuta  = models.IntegerField()
         idEmpleado  = models.IntegerField()
         fechaEmision = models.DateField()
         P01 = models.CharField(max_length=1)
         M01 = models.DecimalField(max_digits=12, decimal_places=2)
         A01 = models.DecimalField(max_digits=12, decimal_places=2)
         B01 = models.DecimalField(max_digits=12, decimal_places=2)
         C01 = models.DecimalField(max_digits=12, decimal_places=2)
         N01 = models.CharField(max_length = 120)
         P02 = models.CharField(max_length=1)
         M02 = models.DecimalField(max_digits=12, decimal_places=2)
         A02 = models.DecimalField(max_digits=12, decimal_places=2)
         B02 = models.DecimalField(max_digits=12, decimal_places=2)
         C02 = models.DecimalField(max_digits=12, decimal_places=2)
         N02 = models.CharField(max_length = 120)
         P03 = models.CharField(max_length=1)
         M03 = models.DecimalField(max_digits=12, decimal_places=2)
         A03 = models.DecimalField(max_digits=12, decimal_places=2)
         B03 = models.DecimalField(max_digits=12, decimal_places=2)
         C03 = models.DecimalField(max_digits=12, decimal_places=2)
         N03 = models.CharField(max_length = 120)
         P04 = models.CharField(max_length=1)
         M04 = models.DecimalField(max_digits=12, decimal_places=2)
         A04 = models.DecimalField(max_digits=12, decimal_places=2)
         B04 = models.DecimalField(max_digits=12, decimal_places=2)
         C04 = models.DecimalField(max_digits=12, decimal_places=2)
         N04 = models.CharField(max_length = 120)
         P05 = models.CharField(max_length=1)
         M05 = models.DecimalField(max_digits=12, decimal_places=2)
         A05 = models.DecimalField(max_digits=12, decimal_places=2)
         B05 = models.DecimalField(max_digits=12, decimal_places=2)
         C05 = models.DecimalField(max_digits=12, decimal_places=2)
         N05 = models.CharField(max_length = 120)
         P06 = models.CharField(max_length=1)
         M06 = models.DecimalField(max_digits=12, decimal_places=2)
         A06 = models.DecimalField(max_digits=12, decimal_places=2)
         B06 = models.DecimalField(max_digits=12, decimal_places=2)
         C06 = models.DecimalField(max_digits=12, decimal_places=2)
         N06 = models.CharField(max_length = 120)
         P07 = models.CharField(max_length=1)
         M07 = models.DecimalField(max_digits=12, decimal_places=2)
         A07 = models.DecimalField(max_digits=12, decimal_places=2)
         B07 = models.DecimalField(max_digits=12, decimal_places=2)
         C07 = models.DecimalField(max_digits=12, decimal_places=2)
         N07 = models.CharField(max_length = 120)
         P08 = models.CharField(max_length=1)
         M08 = models.DecimalField(max_digits=12, decimal_places=2)
         A08 = models.DecimalField(max_digits=12, decimal_places=2)
         B08 = models.DecimalField(max_digits=12, decimal_places=2)
         C08 = models.DecimalField(max_digits=12, decimal_places=2)
         N08 = models.CharField(max_length = 120)
         P09 = models.CharField(max_length=1)
         M09 = models.DecimalField(max_digits=12, decimal_places=2)
         A09 = models.DecimalField(max_digits=12, decimal_places=2)
         B09 = models.DecimalField(max_digits=12, decimal_places=2)
         C09 = models.DecimalField(max_digits=12, decimal_places=2)
         N09 = models.CharField(max_length = 120)
         P10 = models.CharField(max_length=1)
         M10 = models.DecimalField(max_digits=12, decimal_places=2)
         A10 = models.DecimalField(max_digits=12, decimal_places=2)
         B10 = models.DecimalField(max_digits=12, decimal_places=2)
         C10 = models.DecimalField(max_digits=12, decimal_places=2)
         N10 = models.CharField(max_length = 120)
         P11 = models.CharField(max_length=1)
         M11 = models.DecimalField(max_digits=12, decimal_places=2)
         A11 = models.DecimalField(max_digits=12, decimal_places=2)
         B11 = models.DecimalField(max_digits=12, decimal_places=2)
         C11 = models.DecimalField(max_digits=12, decimal_places=2)
         N11 = models.CharField(max_length = 120)
         P12 = models.CharField(max_length=1)
         M12 = models.DecimalField(max_digits=12, decimal_places=2)
         A12 = models.DecimalField(max_digits=12, decimal_places=2)
         B12 = models.DecimalField(max_digits=12, decimal_places=2)
         C12 = models.DecimalField(max_digits=12, decimal_places=2)
         N12 = models.CharField(max_length = 120)
         contratosistema = models.CharField(max_length=22)
         importe = models.DecimalField(max_digits=12, decimal_places=2)
         contrato = models.CharField(max_length=25)
         idtipocontrato = models.IntegerField()
         class Meta:
            db_table = 'pagos'
            managed = False
         def __str__(self):
           return f"{self.id} - {self.idContrato}"

class Quejas(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
        ]
      id = models.UUIDField(primary_key=True,editable=False)
      idquejareporte = models.IntegerField()
      idEmpleado = models.IntegerField()
      idestatusqueja = models.IntegerField()
      fecha_reporte = models.DateField()
      fecha_termino = models.DateField()
      idContrato = models.UUIDField(mac_length = 38)
      comentarios = models.CharField(max_length =  500)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)      
      class Meta:
          db_table = 'queja'
          managed = False
      def __str__(self):
           return f"{self.id} - {self.fecha_reporte}"
           
class CatQuejasReportes(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.AutoField(primary_key = True)
      descripcion = models.CahrField(max_length = 200)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
      class Meta:
        db_table = 'cat_quejas_reportes'
        managed = False
      def __str__(self):
        return f"{self.id} - {self.descripcion}"

class Sistema(models.Model):
      ESTATUS_CHOICES =  [
      	 (1, 'Activo'),
      	 (2, 'Inactivo'),
       ]
      id = models.AutoField(primary_key = True)
      idEstado = models.IntegerField()
      idMunicipio = models.IntegerField()
      estatus = models.IntegerField()
      fechaRegistro = models.DateField()
      fechaVence = models.DateField()
      razonSocial = models.CharField(max_length = 125)
      rfc = models.CharField(max_length = 15)
      domicilio = models.CharField(max_length = 65)
      numero = models.CharField(max_length = 10)
      colonia = models.CharField(max_length = 45)
      telefono = models.CharField(max_length = 15)
      director = models.CharField(max_length = 65)
      subdirector = models.CharField(max_length = 65)
      presidente = models.CharField(max_length = 65)
      latitud = models.CharField(max_length = 25)
      longitud = models.CharField(max_length = 25)
      vigencia = models.IntegerField()
      periodo = models.CharField(max_length = 9)
      slogan= models.CharField(max_length = 65)
      tesoreria = models.CharField(max_length = 65)
      recaudacion = models.CharField(max_length = 65)
      ruta_logo = models.CharField(max_length = 200)
      ruta_sapam = models.CharField(max_length = 200)
      delanio = models.IntegerField()
      alanio = models.IntegerField()
      class Meta:
        db_table = 'sistema'
        managed = False
      
      def __Str__(self):
        return f"{self.id} - {self.idMunicipio}"

class Suministro(models.Model):
      id = models.AutoField(primary_key= True)
      anio = models.IntegerField()
      mes = models.IntegerField()
      idcolonia = models.BigIntegerField()
      fecha_registro = models.DateField()
      d01 = models.CharField(max_length=1)
      d02 = models.CharField(max_length=1)
      d03 = models.CharField(max_length=1)
      d04 = models.CharField(max_length=1)
      d05 = models.CharField(max_length=1)
      d06 = models.CharField(max_length=1)
      d07 = models.CharField(max_length=1)
      d08 = models.CharField(max_length=1)
      d09 = models.CharField(max_length=1)
      d10 = models.CharField(max_length=1)
      d11 = models.CharField(max_length=1)
      d12 = models.CharField(max_length=1)
      d13 = models.CharField(max_length=1)
      d14 = models.CharField(max_length=1)
      d15 = models.CharField(max_length=1)
      d16 = models.CharField(max_length=1)
      d17 = models.CharField(max_length=1)
      d18 = models.CharField(max_length=1)
      d19 = models.CharField(max_length=1)
      d20 = models.CharField(max_length=1)
      d21 = models.CharField(max_length=1)
      d22 = models.CharField(max_length=1)
      d23 = models.CharField(max_length=1)
      d24 = models.CharField(max_length=1)
      d25 = models.CharField(max_length=1)                   
      d26 = models.CharField(max_length=1)
      d27 = models.CharField(max_length=1)
      d28 = models.CharField(max_length=1)
      d29 = models.CharField(max_length=1)
      d30 = models.CharField(max_length=1)
      d31 = models.CharField(max_length=1)
      observacion = models.TextField()
      class Meta:
        db_table = 'suministro'
        managed = False
      
      def __str__(self):
        return f"{self.id} {self.fecha_registro}"

class UserAccess(models.Model):
    ESTATUS_CHOICES = [
	    (1 , 'Activo')
	    (2 , 'Inactivo')
    ]
    id = models.AutoField(primary_key = True)
    idUsuario = models.IntegerField()
    idMenu = models.IntegerField()
    idSubmenu = models.IntegerField()
    estatus = models.IntegerField(choices= ESTATUS_CHOICES, default=1)
    class Meta:
      db_able = 'user_access'
      managed = False
    def __str__(self):
      return f"{self.id} - {self.descripcion}"

class Usuarios(models.Model):
    ESTATUS_CHOICES = [
	    (1 , 'Activo')
	    (2 , 'Inactivo')
    ]
    id = models.AutoField(primary_key = True)
    idTipoUsuario = models.IntegerField()
    idEmpleado = models.IntegerField()
    usuario = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
    fechaCreacion = models.DateField()
    fechaBaja = models.DateField()
    estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)
    class Meta:
      db_table = 'usuarios'
      managed = False
    def __str__(self):  
      return f"{self.id} - {self.usuario}"