from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm
from apps.simulacion.models import CableDeSuspension , Piston , Polea , Acero, TipoPiston
from django.shortcuts import redirect



def simular(request):
	return render(request,'simulacion/index_simulacion.html')

def simulador_view(request):	
	coeficiente_Seg = 0
	cargaRotura = 0
	peso_Ascens = 0 
	recorrido_Total_Piston = 0
	recorrido_Cabina = 0
	sobre_Superior_Piston = 0
	masa_Lineal = 0
	masa_Union = 0 
	diametro_P = 0
	masa_Vastago = 0
	presion_Embolo = 0
	carga_Piston = 0
	masa_E = 0
	cantidad_C = 0
	velocidad_C = 0
	velocidad_P = 0
	caudal_Bomba = 0
	peso_Polea = 0
	diametro_Polea = 0
	diametro_C = 0
	maxima_Carga = 0
	esbeltez = 0
	longitud_Embolo = 0
	radio_Giro = 0
	longitud_Embolo = 0
	carga_Maxima = 0
	traccion = 0
	momento_Incercia = 0
	aceite_Circulacion = 0


	if request.method == 'POST':
		if 'btnsimular' in request.POST:
			
			form = SimulacionForm(request.POST)
			
			datoCable = CableDeSuspension.objects.all()
			dato_Piston = Piston.objects.all()
			dato_Polea = Polea.objects.all()
			dato_Acero = Acero.objects.all()
			dato_Tipo = TipoPiston.objects.all()

			numero_C = request.POST.get('numero_Cables')
			carga_N = request.POST.get('carga_Nominal')
			peso_Ascens = request.POST.get('peso_Ascensor')
			recorrido_Cabina = request.POST.get('recorrido_Cabina')
			sobre_Superior_Piston = request.POST.get('recorido_Superior_Piston')
			diametro_P = request.POST.get('diametro_Piston')
			cantidad_P = request.POST.get('cantidad_Pistones')
			masa_E = request.POST.get('masa_Embolo')
			cantidad_C = request.POST.get('cantidad_Cilindros')
			velocidad_C = request.POST.get('velocidad_Cabina')
			diametro_C = request.POST.get('diametro_Cable')


			velocidad_P = float(velocidad_C)/2
			diametro_Polea = 40*(float(diametro_C))

			recorrido_Total_Piston = float(recorrido_Cabina) + float(sobre_Superior_Piston )

			
			

			for polea in dato_Polea:
				if polea.diametro == diametro_Polea:
					peso_Polea = polea.peso

			for cable in datoCable:
				if coeficiente_Seg	< 12:
					cargaRotura = cable.carga_Rotura_Resestencia160
					coeficiente_Seg = (cargaRotura * float(numero_C))/(float(carga_N) + float(peso_Ascens))
					break

			for piston in dato_Piston:
				if piston.diametro_Exterior == 	float(diametro_P):
					masa_Lineal = piston.masa_Lineal_Vastago	
					masa_Union = piston.masa_Union_Vastago

			for dato in dato_Acero:
				traccion = dato.normal

			coeficiente_Seg = (cargaRotura * float(numero_C))/(float(carga_N) + float(peso_Ascens))
			masa_Vastago = ((recorrido_Total_Piston/100)* masa_Lineal) + masa_Union*(3)
			presion_Embolo = (((float(carga_N)+ float(peso_Ascens))+ (float(cantidad_P)*masa_Vastago)) / (float(cantidad_P)*3.1416*((float(diametro_P)*float(diametro_P)/100)/4)))*9.8
			carga_Piston =1.4*9.8*(((float(carga_N)+float(peso_Ascens))/float(cantidad_C)) + 0.64*float(masa_E))
			caudal_Bomba = float(velocidad_C)*(((5*6*3.1416)*((float(diametro_P)/100)*(float(diametro_P)/100)))/4)
			j=0
			for lamda in dato_Tipo:				
				longitud_Embolo = float(lamda.longitud_Embolo)/float(lamda.radio_Giro)	
				carga_Maxima = ((3.1416*3.1416)*(210000)*lamda.momento_De_Inercia)/(2*(longitud_Embolo*longitud_Embolo))
				if carga_Maxima	>= carga_Piston	:
					aceite_Circulacion	= lamda.aceite * recorrido_Total_Piston
					break

			form = SimulacionForm(request.POST)

			if form.is_valid():
				form.save()

	else:
		form = SimulacionForm()


	return render(request, 'simulacion/index_simulacion.html' , {'aceite': round(aceite_Circulacion,2)	,'carga':round(carga_Maxima,2),'peso_Polea': round(peso_Polea,2) ,'caudal_Bomba':round(caudal_Bomba,2),'form':form, 'coeficiente':round(coeficiente_Seg,2),'pis':round(presion_Embolo,2),'carga_Piston':round(carga_Piston,2), 'velocidad_P': round(velocidad_P,2), 'diametro_Polea':round(diametro_Polea,2)})
