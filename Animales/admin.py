from django.contrib import admin
from .models import Animal, Localidad, Convenio, Familia, Genero, Especie

admin.site.register(Localidad)
admin.site.register(Animal)
admin.site.register(Convenio)
admin.site.register(Familia)
admin.site.register(Genero)
admin.site.register(Especie)