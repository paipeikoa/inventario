from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
                Categoria, on_delete=models.CASCADE,
                null=True, verbose_name='Categoria')
    KILOS = 1
    METROS = 2
    LITROS = 3
    TIPO_DE_PRODUCTO = (
        (KILOS, 'Kilogramos'),
        (METROS, 'Metros'),
        (LITROS, 'Litros'),
    )
    nombre = models.CharField(max_length=50,null=True)
    marca = models.CharField(max_length=50)
    tipo_producto = models.PositiveSmallIntegerField(
                    choices=TIPO_DE_PRODUCTO, blank=True,
                    null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    #total2 = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    imagenes = models.ImageField(upload_to='images/', null=True, default='images/caballero.png')

#    def save(self):
#        prueba_total = self.cantidad * self.precio
#        self.total2 = prueba_total
#        super(Producto, self).save()

    def __str__(self):
        return self.nombre
