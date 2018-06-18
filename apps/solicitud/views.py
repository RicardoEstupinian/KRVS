from django.shortcuts import render
from apps.simulacion.models import Simulador


def modificacion(request):
	numero_Cables = 0
	carga_Nominal = 0
	recorrido_Cabina = 0
	Recorrido_Superior_Piston = 0
	cantidad_Pistones = 0
	cantidad_Cilindros = 0
	numero_Expanciones = 0
	velocidad_Cabina = 0
	diametro_Cable = 0
	peso_Ascensor = 0
	diamtro_Piston = 0
	masa_Embolo = 0
	if request.method == 'POST':					
		



		form = ModificacionForm(request.POST)
		datoSimulacion = Simulador.objects.all()
		for dato in datoSimulacion:
			if dato.id == 5:
				numero_Cables = dato.numero_Cables
				carga_Nominal = dato.carga_Nominal
				recorrido_Cabina = dato.recorrido_Cabina
				Recorrido_Superior_Piston = dato.Recorido_Superior_Piston
				cantidad_Pistones = dato.cantidad_Pistones
				cantidad_Cilindros = dato.cantidad_Cilindros
				numero_Expanciones = dato.numero_Expanciones
				velocidad_Cabina = dato.velocidad_Cabina
				diametro_Cable = dato.diametro_Cable
				peso_Ascensor = dato.peso_Ascensor
				diametro_Piston = dato.diamtro_Piston
				masa_Embolo = dato.masa_Embolo

		
		diccionario = {
			
			
			'recorrido_Cabina' : recorrido_Cabina,
			'Recorrido_Superior_Piston': Recorrido_Superior_Piston,
			'cantidad_Pistones' : cantidad_Pistones,
			'cantidad_Cilindros' : cantidad_Cilindros,
			'numero_Expanciones': numero_Expanciones,
			'velocidad_Cabina': velocidad_Cabina,
			'diametro_Cable': diametro_Cable,
			'peso_Ascensor':peso_Ascensor,
			'diamtro_Piston': diamtro_Piston,
			'masa_Embolo': masa_Embolo,
		}

			
			


			

#			diametro_C = request.POST.get('diametro_Cable')





	return render(request,'modificacion/index_modificacion.html',{'numero_Cables' : numero_Cables,'carga_Nominal' : carga_Nominal})


