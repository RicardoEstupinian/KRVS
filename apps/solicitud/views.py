from django.shortcuts import render
from apps.simulacion.models import Simulador, Piston, CableDeSuspension	, Polea	,Acero, TipoPiston	
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
	presion_Embolo = 0
	idS = 0
	velocidad_P = 0
	recorrido_Total_Piston =0
	masa_Lineal = 0
	masa_Union = 0
	presion_Embolo = 0
	dato_Piston=0
	coeficiente_Seg	= 0
	carga_Piston = 0
	carga_Maxima = 0
	peso_Polea=0
	diametro_Polea = 0
	caudal_Bomba = 0
	aceite_Circulacion = 0
	cantidad_P = 0

	if request.method == 'POST':		
		form = ModificacionForm(request.POST)			
		if 'btnsimular' in request.POST:			
			idS = request.POST.get('usuario')
			datoSimulacion = Simulador.objects.all()
			datoCable = CableDeSuspension.objects.all()
			dato_Piston = Piston.objects.all()
			dato_Polea = Polea.objects.all()
			dato_Acero = Acero.objects.all()
			dato_Tipo = TipoPiston.objects.all()
			

			for dato in datoSimulacion:
				if int(dato.id) == int(idS):				
					velocidad_C = request.POST.get('velocidad_Cabina')	
					numero_Cables = request.POST.get('numero_Cables')
					carga_Nominal = request.POST.get('carga_Nominal')	
					recorrido_Cabina = dato.recorrido_Cabina
					Recorrido_Superior_Piston = dato.recorido_Superior_Piston
					cantidad_P = dato.cantidad_Pistones
					cantidad_Cilindros = dato.cantidad_Cilindros
					numero_Expanciones = dato.numero_Expanciones
					velocidad_Cabina = dato.velocidad_Cabina
					diametro_Cable = dato.diametro_Cable
					peso_Ascensor = dato.peso_Ascensor
					diametro_Piston = dato.diametro_Piston
					masa_Embolo = dato.masa_Embolo

					recorrido_Total_Piston = float(recorrido_Cabina)*2.5 + float(Recorrido_Superior_Piston)	

					for piston in dato_Piston:
						if piston.diametro_Exterior == 	float(diametro_Piston):
							masa_Lineal = piston.masa_Lineal_Vastago	
							masa_Union = piston.masa_Union_Vastago

					masa_Vastago = ((recorrido_Total_Piston/100)* masa_Lineal) + masa_Union*(3)		

					presion_Embolo = (((float(carga_Nominal)+ float(peso_Ascensor))+ (float(cantidad_P)*masa_Vastago)) / (float(cantidad_P)*3.1416*((float(diametro_Piston)*float(diametro_Piston)/100)/4)))*9.8	
					for cable in datoCable:
						if coeficiente_Seg	< 12:
							cargaRotura = cable.carga_Rotura_Resestencia160
							coeficiente_Seg = (cargaRotura * float(numero_Cables))/(float(carga_Nominal) + float(peso_Ascensor))
							break
					
					velocidad_P = float(velocidad_C)/2
					carga_Piston =1.4*9.8*(((float(carga_Nominal)+float(peso_Ascensor))/float(cantidad_Cilindros)) + 0.64*float(masa_Embolo))

					diametro_Polea = 40*(float(diametro_Cable))
					for polea in dato_Polea:
						if polea.diametro == diametro_Polea:
							peso_Polea = polea.peso

					for lamda in dato_Tipo:				
						longitud_Embolo = float(lamda.longitud_Embolo)/float(lamda.radio_Giro)	
						carga_Maxima = ((3.1416*3.1416)*(210000)*lamda.momento_De_Inercia)/(2*(longitud_Embolo*longitud_Embolo))
						if carga_Maxima	>= carga_Piston	:
							aceite_Circulacion	= lamda.aceite * recorrido_Total_Piston
							break
					caudal_Bomba = float(velocidad_C)*(((5*6*3.1416)*((float(diametro_Piston)/100)*(float(diametro_Piston)/100)))/4)		
		

			form = ModificacionForm(request.POST)		
		

		if 'btnmodificar' in request.POST:
			
			modific = Simulador.objects.get(id='135')			
			if request.method == 'GET':
				form = ModificacionForm(instance= modific)
			else:
					
				
				if form.is_valid():
					form.save()
				else:
					form = ModificacionForm()


		
	else:
		form = ModificacionForm()

			






	return render(request,'modificacion/index_modificacion.html',{'peso_Polea':round(peso_Polea,2),'diametro_Polea':round(diametro_Polea,2),'caudal_Bomba':round(caudal_Bomba),'aceite_Circulacion': round(aceite_Circulacion,2),'carga_Maxima':round(carga_Maxima,2),'carga_Piston':round(carga_Piston,2),'presion_Embolo':round(presion_Embolo,2),'coeficiente_Seg':round(coeficiente_Seg,2),'presion_Embolo': round(presion_Embolo,2),'velocidad_P': velocidad_P,'form':form,'masa_Embolo': masa_Embolo,'diametro_Piston': diametro_Piston,'peso_Ascensor':peso_Ascensor,'diametro_Cable': diametro_Cable,'velocidad_Cabina': velocidad_Cabina,'numero_Expanciones': numero_Expanciones,'cantidad_Cilindros' : cantidad_Cilindros,'cantidad_Pistones' : cantidad_P,'Recorrido_Superior_Piston': Recorrido_Superior_Piston,'recorrido_Cabina' : recorrido_Cabina,'numero_Cables' : numero_Cables,'carga_Nominal' : carga_Nominal})


