from django.contrib import admin

# Register your models here.
from apps.simulacion.models import Simulador , Piston , PistonTelescopico, CableDeSuspension, Ascensor

admin.site.register(Simulador)
admin.site.register(Piston)
admin.site.register(PistonTelescopico)
admin.site.register(CableDeSuspension)
admin.site.register(Ascensor)
