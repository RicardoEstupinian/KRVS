from django.shortcuts import render
from django.contrib import authenticate,login

# Create your views here.
def vistalogin(request):
	return render(request,'login/login_index.html')

	

