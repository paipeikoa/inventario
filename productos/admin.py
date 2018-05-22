from django.contrib import admin
from productos.models import Compra, DetalleCompra, Producto

# Register your models here.


class DetalleCompraAdmin(admin.TabularInline):
    model = DetalleCompra

class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraAdmin]

admin.site.register(Compra, CompraAdmin)
admin.site.register(DetalleCompra)
admin.site.register(Producto)
