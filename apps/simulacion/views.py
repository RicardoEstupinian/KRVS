from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm
from apps.simulacion.models import CableDeSuspension
from django.shortcuts import redirect



def simular(request):
	return render(request,'simulacion/index_simulacion.html')

def simulador_view(request):	
	coeficiente_Seg = 10
	cargaRotura = 0
	if request.method == 'POST':
		if 'btnsimular' in request.POST:

			form = SimulacionForm(request.POST)
			datoCable = CableDeSuspension.objects.all()

			numero_C = request.POST.get('numero_Cables')
			carga_N = request.POST.get('carga_Nominal')

			for cable in datoCable:
				if cable.diametro == 10:
					cargaRotura = cable.carga_Rotura_Resestencia160


	

			coeficiente_Seg = (cargaRotura * float(numero_C))/float(carga_N)


			form = SimulacionForm(request.POST)
			if form.is_valid():
				form.save()
	else:
		form = SimulacionForm()


	return render(request, 'simulacion/index_simulacion.html' , {'form':form, 'coeficiente':coeficiente_Seg})
