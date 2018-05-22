from django.db import models
from django.db.models.signals import post_save
from smart_selects.db_fields import ChainedForeignKey 
# Create your models here.


class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=40,blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion


class Proveedor(models.Model):
    proveedor_numero = models.CharField(unique=True,max_length=11)
    razon_social = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15,null=True)
    correo = models.EmailField(null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'N° Proveedor ' + self.proveedor.proveedor_numero

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveIntegerField(default=0,blank=False, null=False)
    precio_compra = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def save(self):
        total_compra = self.cantidad * self.precio_compra
        self.total = total_compra
        super(Compra, self).save()

    def __str__(self):
        return str(self.producto.precio)
