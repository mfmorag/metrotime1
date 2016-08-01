from django.db import models
#from django.contrib.auth.models import User

class Establecimiento(models.Model):
	nombre = models.CharField(max_length=50, blank=False, unique=True)

	def __str__(self):
		return self.nombre

class Estado(models.Model):
	tipo = models.CharField(max_length=20, blank=False, unique=True)

	def __str__(self):
		return self.tipo

class Vehiculo(models.Model):
	id_est = models.ForeignKey(Establecimiento)
	placa = models.CharField(max_length=7, blank=False, unique=True)
	numero_gsm = models.CharField(max_length=10, blank=False, unique=True)
	codigo = models.CharField(max_length=4, blank=False, unique=True)
	estado = models.ForeignKey(Estado)

	def __unicode__(self):
		return ' %s' % (self.codigo)


class Ubicacion(models.Model):
	id_vehiculo = models.ForeignKey(Vehiculo)
	latitud = models.CharField(max_length=10, blank=False)
	longitud = models.CharField(max_length=10, blank=False)
	velocidad = models.CharField(max_length=10, blank=False)

	def __str__(self):
		return '%s %s %s' % (self.latitud, self.longitud, self.velocidad)
	def __unicode__(self):
		return '%s %s %s' % (self.latitud, self.longitud, self.velocidad)

class Conductor(models.Model):
	id_vehiculo = models.ForeignKey(Vehiculo)
	nombres = models.CharField(max_length=50, blank=False)
	apellidos = models.CharField(max_length=50, blank=False)
	edad = models.IntegerField(blank=False)
	cedula = models.CharField(max_length=10, blank=False, unique=True)
	telefono = models.CharField(max_length=10, blank=False, unique=True)
	correo = models.CharField(max_length=50, blank=False)

class Ruta(models.Model):
	id_est = models.ForeignKey(Establecimiento)
	nombre = models.CharField(max_length=50, blank=False, unique=True)

	def __str__(self):
		return self.nombre


class RLine(models.Model):
	id_ruta = models.ForeignKey(Ruta)
	latitud = models.CharField(max_length=10, blank=False)
	longitud = models.CharField(max_length=10, blank=False)

	def __str__(self):
		return '%s %s' % (self.latitud, self.longitud)


class Parada(models.Model):
	id_ruta = models.ForeignKey(Ruta)
	nombre = models.CharField(max_length=50, blank=False)
	latitud = models.CharField(max_length=10, blank=False)
	longitud = models.CharField(max_length=10, blank=False)
	order = models.IntegerField(blank=False)

	def __str__(self):
		return '%s %s %s' % (self.nombre, self.latitud, self.longitud)
	def __unicode__(self):
		return '%s %s %s' % (self.nombre, self.latitud, self.longitud)


class PLine(models.Model):
	parada = models.ForeignKey(Parada)
	latitud = models.CharField(max_length=10, blank=False)
	longitud = models.CharField(max_length=10, blank=False)

	def __str__(self):
		return '%s %s' % (self.latitud, self.longitud)
	#def __unicode__(self):
	#	return '%s %s' % (self.latitud, self.longitud)


class RutaVehiculo(models.Model):
	id_ruta = models.ForeignKey(Ruta)
	id_vehiculo = models.ForeignKey(Vehiculo)
