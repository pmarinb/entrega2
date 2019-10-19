from django.db import models
from aplicaciones.productos.models import Vehiculo
from aplicaciones.usuarios.models import Usuario

# Create your models here.


class Venta(models.Model):
    usuario_fk = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)
    vehiculo_fk = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField(auto_now=True)
