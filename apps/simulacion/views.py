from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm
from apps.simulacion.models import CableDeSuspension , Piston
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


	if request.method == 'POST':
		if 'btnsimular' in request.POST:

			form = SimulacionForm(request.POST)
			datoCable = CableDeSuspension.objects.all()
			dato_Piston = Piston.objects.all()

			numero_C = request.POST.get('numero_Cables')
			carga_N = request.POST.get('carga_Nominal')
			peso_Ascens = request.POST.get('peso_Ascensor')
			recorrido_Cabina = request.POST.get('recorrido_Cabina')
			sobre_Superior_Piston = request.POST.get('recorido_Superior_Piston')
			diametro_P = request.POST.get('diametro_Piston')
			cantidad_P = request.POST.get('cantidad_Pistones')

			recorrido_Total_Piston = float(recorrido_Cabina) + float(sobre_Superior_Piston )

			for cable in datoCable:
				if cable.diametro == 10:
					cargaRotura = cable.carga_Rotura_Resestencia160

			for piston in dato_Piston:
				if piston.diametro_Exterior == 	float(diametro_P):
					masa_Lineal = piston.masa_Lineal_Vastago	
					masa_Union = piston.masa_Union_Vastago

	

			coeficiente_Seg = (cargaRotura * float(numero_C))/(float(carga_N) + float(peso_Ascens))
			masa_Vastago = ((recorrido_Total_Piston/100)* masa_Lineal) + masa_Union*(2)
			presion_Embolo = ((float(carga_N)+ float(peso_Ascens))+ (float(cantidad_P)*masa_Vastago))/(((float(cantidad_P)*3.1416)*(float(diametro_P)*float(diametro_P)))/4)

			form = SimulacionForm(request.POST)
			if form.is_valid():
				form.save()
	else:
		form = SimulacionForm()


	return render(request, 'simulacion/index_simulacion.html' , {'form':form, 'coeficiente':coeficiente_Seg,'pis':presion_Embolo})
