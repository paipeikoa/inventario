from django.contrib import admin
from .models import (
	Pais,Provincia,Departamento,Localidad,
	Direccion)
# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Departamento)
admin.site.register(Localidad)
admin.site.register(Direccion)