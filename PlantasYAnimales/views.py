from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render


def home(request):
	bienvenida = '¡Bienvenido a la página de inicio!'

	# index_tmplt = get_template('index.html')
	index_tmplt = get_template('home.html')

	context = {'bienvenida': bienvenida}
	document = index_tmplt.render(context)

	return HttpResponse(document)