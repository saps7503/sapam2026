from django.db import models

class Contrato(models.Model):
      ESTATUS_CHOICES = [
        (1, 'Activo'),
        (2, 'Inactivo'),
        (3, 'Cancelado'),
      ]
      id  = models.BigAutoField(primary_key=True)
      nombres = models.CharField(max_length=25, null=True, blank=True)
      paterno = models.CharField(max_length=15, null=True, blank=True)
      materno = models.CharField(max_length=15, null=True, blank=True)
      estatus = models.IntegerField(choices=ESTATUS_CHOICES, default=1)

      class Meta:
          db_table = 'contratos'
          managed = False

      def __str__(self):
        return f"{self.id} {self.nombres} {self.paterno} {self.materno} {self.estatus}"