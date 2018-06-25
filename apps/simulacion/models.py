from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Simulador(models.Model):
	numero_Cables = models.FloatField(null=False)
	carga_Nominal = models.FloatField(null=False)
	recorrido_Cabina =  models.FloatField(null=False)
	recorido_Superior_Piston  = models.FloatField(null=False)
	cantidad_Pistones = models.IntegerField(null=False)
	cantidad_Cilindros = models.IntegerField(null=False)
	numero_Expanciones = models.IntegerField(null=False)
	velocidad_Cabina = models.FloatField(null=False)
	diametro_Cable = models.FloatField(null=False)
	peso_Ascensor = models.FloatField(null=True)
	diametro_Piston = models.FloatField(null=True)
	masa_Embolo = models.FloatField(null=True)	
	usuario = models.ForeignKey(User, null=False, blank=True, on_delete= models.CASCADE)
	
class Piston(models.Model):
	masa_Lineal_Vastago = models.FloatField(null=True)
	diametro_Exterior = models.FloatField(null=True)
	masa_Union_Vastago = models.FloatField(null=True)
	area_Resistente_Embolo = models.FloatField(null=True)
	radio_Giro_Embolo = models.FloatField(null=True)
	resistencia_Traccion_Acero = models.FloatField(null=True)
	momento_Inercia = models.FloatField(null=True)
	factor_Diametro = models.FloatField(null=True)

	
	
class PistonTelescopico(models.Model):
	masa_Embolo = models.FloatField(null=True)
	diametro_Exterior_di = models.FloatField(null=True)
	longitud_Total = models.FloatField(null=True)
	masa_Total = models.FloatField(null=True)
	diametro_Interior_Camisa = models.FloatField(null=True)
	masa_Cabezal = models.FloatField(null=True)
	resistencia_Traccion_Acero = models.FloatField(null=True)
	factor_Diametro_Tu = models.FloatField(null=True)
	

class CableDeSuspension(models.Model):
	diametro = models.FloatField(null=True)
	diametro_Efectivo = models.FloatField(null=True)
	peso_Cable = models.FloatField(null=True)
	carga_Rotura_Resestencia140 = models.FloatField(null=True)
	carga_Rotura_Resestencia160 = models.FloatField(null=True)
	carga_Rotura_Resestencia180 = models.FloatField(null=True)


class Polea(models.Model):
	diametro = models.FloatField(null=True)
	peso = models.FloatField(null=True)

class TipoPiston(models.Model):	
	area_Embolo = models.FloatField(null=True)
	longitud_Embolo = models.FloatField(null=True)
	radio_Giro = models.FloatField(null=True)
	momento_De_Inercia = models.FloatField(null=True)
	aceite = models.FloatField(null= True)

class Acero(models.Model):
	tipo_Acero = models.FloatField(null=True)
	normal = models.FloatField(null=True)
	mecanico = models.FloatField(null=True)



class Ascensor(models.Model):
	carga_Nominal = models.FloatField(null=True)
	superficie = models.FloatField(null=True)
	piston_Telescopico = models.ForeignKey(PistonTelescopico, null=True,blank=True, on_delete=models.CASCADE)
	piston = models.ForeignKey(Piston, null=True,blank=True, on_delete=models.CASCADE)
	cable = models.ForeignKey(CableDeSuspension, null=True,blank=True, on_delete=models.CASCADE)
	Polea = models.ForeignKey(Polea, null=True,blank=True, on_delete=models.CASCADE)
	acero = models.ForeignKey(Acero, null=True,blank=True, on_delete=models.CASCADE)
	tipoPiston = models.ForeignKey(TipoPiston, null=True,blank=True, on_delete=models.CASCADE)
	simulador = models.OneToOneField(Simulador, null= True, blank=True, on_delete=models.CASCADE)
	

