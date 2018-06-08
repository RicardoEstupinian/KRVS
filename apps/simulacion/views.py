from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from apps.simulacion.forms import SimulacionForm


def simular(request):
	return render(request,'simulacion/index_simulacion.html')

def simulador_view(request):	
	if request.method == 'POST':
		form = SimulacionForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = SimulacionForm()

	return render(request, 'simulacion/index_simulacion.html' , {'form':form})
