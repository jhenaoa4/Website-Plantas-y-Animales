from django.db import models

class Animal(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    nombre = models.CharField(max_length=40)
    localidad = models.ForeignKey('Localidad', on_delete=models.CASCADE)
    repositorio = models.CharField(max_length=40)
    convenio = models.ManyToManyField('Convenio')
    fecha_colecta = models.DateField(auto_now_add=False)
    familia = models.ForeignKey('Animales.Familia', on_delete=models.CASCADE)
    genero = models.ForeignKey('Animales.Genero', on_delete=models.CASCADE)
    especie = models.ForeignKey('Animales.Especie', on_delete=models.CASCADE)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField(default=0)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    id_alt = models.CharField(max_length=10)
    comentario = models.TextField(max_length=180, blank=True, null=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        db_table = 'animales'

    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    latitud = models.DecimalField(max_digits=6, decimal_places=4)
    longitud = models.DecimalField(max_digits=6, decimal_places=4)
    polaridad = models.CharField(max_length=10)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    comentario = models.TextField(max_length=180, blank=True, null=True)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'localidades'

    def __str__(self):
        return self.nombre

class Convenio(models.Model):
    id = models.CharField(default='0', max_length=10, primary_key=True, auto_created=False)
    nombre = models.CharField(max_length=40)
    fecha_inicio = models.DateField(auto_now_add=False)
    fecha_fin = models.DateField(auto_now_add=False)
    comentario = models.TextField(max_length=180, blank=True, null=True)

    class Meta:
        verbose_name = 'Convenio'
        verbose_name_plural = 'Convenios'
        db_table = 'convenio'

    def __str__(self):
        return self.nombre

class Familia(models.Model):
	nombre = models.CharField(max_length=40)

	class Meta:
		verbose_name='Familia Animal'
		verbose_name_plural='Familias Animales'
		db_table='familias animales'

	def __str__(self):
		return self.nombre

class Genero(models.Model):
	nombre = models.CharField(max_length=40)
	familia = models.ForeignKey('Animales.Familia', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Genero Animal'
		verbose_name_plural='Generos Animales'
		db_table='generos animales'

	def __str__(self):
		return self.nombre

class Especie(models.Model):
	nombre = models.CharField(max_length=40)
	genero = models.ForeignKey('Animales.Genero', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name='Especie Animal'
		verbose_name_plural='Especies Animales'
		db_table='especies animales'
	
	def __str__(self):
		return self.nombre
