from django.db import models

# Create your models here.
class Pais(models.Model):
	"""Datos de paises"""
	id_pais = models.AutoField(primary_key=True)
	nombre  = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = 'Países'

class Provincia(models.Model):
	"""Datos de todas las provincias de Argentina"""
	id_provincia = models.AutoField(primary_key=True)
	nombre 		 = models.CharField(max_length=100, null=False, blank=False)
	pais 	 	 = models.ForeignKey(Pais, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']

class Departamento(models.Model):
	"""Datos de todos los dptos de c/u de las provincias"""
	id_departamento = models.AutoField(primary_key=True)
	nombre 		 	= models.CharField(max_length=100, null=False, blank=False)
	provincia 	    = models.ForeignKey(Provincia, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre'] 

class Localidad(models.Model):
	"""Datos de todos las localidades de c/u de los dpts"""
	id_localidad 	= models.AutoField(primary_key=True)
	nombre 		 	= models.CharField(max_length=100, null=False, blank=False)
	departamento    = models.ForeignKey(Departamento, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']
		verbose_name_plural = 'Localidades' 

class Direccion(models.Model):
	"""Datos relacionado con la direccion de las personas"""
	id_direccion = models.AutoField(primary_key=True)
	calle 		 = models.CharField(max_length=100, null=False, blank=False)
	numero 		 = models.PositiveSmallIntegerField(blank=False, null=False)
	localidad    = models.ForeignKey(Localidad, on_delete=models.CASCADE)

	def __str__(self):
		return self.calle + " " + self.numero

	class Meta:
		ordering = ['calle']
		verbose_name_plural = 'Direcciones' 
