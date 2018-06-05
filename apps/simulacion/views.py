from django.shortcuts import render
# Create your views here.

def simular(request):
	return render(request,'simulacion/index_simulacion.html')