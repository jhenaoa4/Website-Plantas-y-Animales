from django.shortcuts import render

from .models import Animal

def home(request):
	piezas = Animal.objects.all()

	return render(request, "gestion_piezas.html", {'piezas': piezas})
