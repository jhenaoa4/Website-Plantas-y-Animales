from django.db import models

# Este proyecto alberga información descriptiva de muestras de plantas recolectadas. 

class Planta(models.Model):
	tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE)
	locacion = models.ForeignKey('Locacion', on_delete=models.CASCADE)
	fecha_coleccion = models.DateTimeField(auto_now_add=False)
	importancia = models.CharField(max_length=40)
	medidas = models.CharField(max_length=40)
	unidades_medida = models.ForeignKey('UnidadesMedida', on_delete=models.CASCADE)
	familia = models.ForeignKey('Plantas.Familia', on_delete=models.CASCADE)
	genero = models.ForeignKey('Plantas.Genero', on_delete=models.CASCADE)
	especie = models.ForeignKey('Plantas.Especie', on_delete=models.CASCADE)
	foto = models.ManyToManyField('Foto', blank=True)
	
	class Meta:
		verbose_name='Planta'
		verbose_name_plural='Plantas'
		db_table='plantas'
	
	def __str__(self):
		return self.especie.nombre

class Tipo(models.Model):
	id = models.AutoField(primary_key=True)
	tipo = models.CharField(max_length=40)
	
	class Meta:
		verbose_name='Tipo'
		verbose_name_plural='Tipos'
		db_table='tipos'
	
	def __str__(self):
		return self.tipo

class Locacion(models.Model):
	latitud = models.DecimalField(max_digits=6, decimal_places=4)
	longitud = models.DecimalField(max_digits=7, decimal_places=4)
	nombre = models.CharField(max_length=40)
	pais = models.CharField(max_length=40)

	class Meta:
		verbose_name='Locacion'
		verbose_name_plural='Locaciones'
		db_table='locaciones'

	def __str__(self):      
		return self.nombre

class UnidadesMedida(models.Model):
	unidad = models.CharField(max_length=40)

	class Meta:
		verbose_name='Unidad de Medida'
		verbose_name_plural='Unidades de Medida'
		db_table='unidades_medida'

	def __str__(self):
		return self.unidad

class Familia(models.Model):
	nombre = models.CharField(max_length=40)

	class Meta:
		verbose_name='Familia Planta'
		verbose_name_plural='Familias Plantas'
		db_table='familias plantas'

	def __str__(self):
		return self.nombre

class Genero(models.Model):
	nombre = models.CharField(max_length=40)
	familia = models.ForeignKey('Plantas.Familia', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Genero Planta'
		verbose_name_plural='Generos Plantas'
		db_table='generos plantas'

	def __str__(self):
		return self.nombre

class Especie(models.Model):
	nombre = models.CharField(max_length=40)
	genero = models.ForeignKey('Plantas.Genero', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Especie Planta'
		verbose_name_plural='Especies Plantas'
		db_table='especies plantas'
	
	def __str__(self):
		return self.nombre

class Foto(models.Model):
	id = models.CharField(max_length=40, primary_key=True)
	foto = models.ImageField(upload_to='plantas', null=True, blank=True)
	# planta = models.ForeignKey('Plantas.Foto.foto', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Foto'
		verbose_name_plural='Fotos'
		db_table='fotos'

	def __str__(self):
		return self.id