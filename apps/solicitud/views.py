from django.shortcuts import render
from apps.simulacion.models import Simulador, Piston
from apps.solicitud.forms import ModificacionForm
from django.http import HttpResponse
from django.shortcuts import redirect

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
	diametro_Piston = 0
	masa_Embolo = 0
	idS = 0
	velocidad_P = 0
	recorrido_Total_Piston =0
	masa_Lineal = 0
	masa_Union = 0
	presion_Embolo = 0
	dato_Piston=0
	if request.method == 'POST':		
		form = ModificacionForm(request.POST)			
		if 'btnsimular' in request.POST:
			dato_Piston = Piston.objects.all()
			idS = request.POST.get('usuario')
			datoSimulacion = Simulador.objects.all()
			for dato in datoSimulacion:
				if int(dato.id) == int(idS):
					
					numero_Cables = dato.numero_Cables
					carga_Nominal = dato.carga_Nominal
					recorrido_Cabina = dato.recorrido_Cabina
					Recorrido_Superior_Piston = dato.recorido_Superior_Piston
					cantidad_Pistones = dato.cantidad_Pistones
					cantidad_Cilindros = dato.cantidad_Cilindros
					numero_Expanciones = dato.numero_Expanciones
					velocidad_Cabina = dato.velocidad_Cabina
					diametro_Cable = dato.diametro_Cable
					peso_Ascensor = dato.peso_Ascensor
					diametro_Piston = dato.diametro_Piston
					masa_Embolo = dato.masa_Embolo
			form = ModificacionForm(request.POST)		
		if 'btnmodificar' in request.POST:
			numero_C = request.POST.get('numero_Cables')
			carga_N = request.POST.get('carga_Nominal')
			peso_Ascens = request.POST.get('peso_Ascensor')
			recorrido_Cabina =(request.POST.get('recorrido_Cabina'))
			sobre_Superior_Piston = request.POST.get('recorido_Superior_Piston')
			diametro_P = request.POST.get('diametro_Piston')
			cantidad_P = request.POST.get('cantidad_Pistones')
			masa_E = request.POST.get('masa_Embolo')
			cantidad_C = request.POST.get('cantidad_Cilindros')
			velocidad_C = request.POST.get('velocidad_Cabina')
			diametro_C = request.POST.get('diametro_Cable')


			velocidad_P = float(velocidad_C)/2

		else:
			form = ModificacionForm()	
	else:
		form = ModificacionForm()

			

#			diametro_C = request.POST.get('diametro_Cable')





	return render(request,'modificacion/index_modificacion.html',{'presion_Embolo': presion_Embolo,'velocidad_P': velocidad_P,'form':form,'masa_Embolo': masa_Embolo,'diametro_Piston': diametro_Piston,'peso_Ascensor':peso_Ascensor,'diametro_Cable': diametro_Cable,'velocidad_Cabina': velocidad_Cabina,'numero_Expanciones': numero_Expanciones,'cantidad_Cilindros' : cantidad_Cilindros,'cantidad_Pistones' : cantidad_Pistones,'Recorrido_Superior_Piston': Recorrido_Superior_Piston,'recorrido_Cabina' : recorrido_Cabina,'numero_Cables' : numero_Cables,'carga_Nominal' : carga_Nominal})


