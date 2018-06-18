from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request,'inicio/index_inicio.html')

def infor(request):
	return render(request,'informacion/index_informacion.html')