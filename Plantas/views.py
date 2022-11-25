from django.shortcuts import render, redirect
from .models import Planta, Especie, Genero, Familia, Locacion, UnidadesMedida, Tipo

def home(request):
	plantas = Planta.objects.all()

	return render(request, "gestion_plantas.html", {'plantas': plantas})

def crear_planta(request):
	especie = request.POST['txtEspecie']
	familia = request.POST['txtFamilia']
	genero = request.POST['txtGenero']
	localidad = request.POST['txtLocalidad']
	latitud = request.POST['txtLatitud']
	longitud = request.POST['txtLongitud']
	unidades = request.POST['txtUnidades']
	medidas = request.POST['txtMedidas']
	pais = request.POST['txtPais']
	importancia = request.POST['txtImportancia']
	fecha = request.POST['txtFecha']
	tipo = request.POST['txtTipo']

	tipo = Tipo.objects.create(tipo=tipo)
	familia = Familia.objects.create(nombre=familia)
	genero = Genero.objects.create(nombre=genero, familia=familia)
	especie = Especie.objects.create(nombre=especie, genero=genero)
	unidades = UnidadesMedida.objects.create(unidad=unidades)
	localidad = Locacion.objects.create(nombre=localidad, latitud=latitud, longitud=longitud, pais=pais)
	planta = Planta.objects.create(tipo=tipo, especie=especie, familia=familia, genero=genero, locacion=localidad, medidas=medidas, importancia=importancia, fecha_coleccion=fecha, unidades_medida=unidades)

	return redirect('/investigadores/')
