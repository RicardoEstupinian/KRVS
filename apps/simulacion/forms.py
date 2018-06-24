from django import forms
from apps.simulacion.models import Simulador


velocidades= (
		('1',0.15),
		('2',0.30),
		('3',0.45),
		('4',0.60),
		('5',0.75),
		('6',0.90),
		('7',1),
	)

pisos= (
		('1',1),
		('2',2),
		('3',3),
		('4',4),
		('5',5),
		('6',6),
		('7',7),
		('8',8),
		('9',9),
		('10',10),
	)
expanciones= (
		('1',1),
		('2',2),
		('3',3),		
	)


class SimulacionForm(forms.ModelForm):

	class Meta:
		model = Simulador
		INTEGER_CHOICES= (0.15,0.30,0.45,0.60,0.75,0.90,1)

		fields = [
			'numero_Cables',
			'carga_Nominal',
			'recorrido_Cabina',
			'recorido_Superior_Piston',
			'cantidad_Pistones',
			'cantidad_Cilindros',
			'numero_Expanciones',
			'velocidad_Cabina',
			'diametro_Cable',
			'peso_Ascensor',
			'diametro_Piston',
			'masa_Embolo',			
			'usuario',
		
		]

		labels = {
			'numero_Cables': 'Cantidad de cables',
			'carga_Nominal': 'Carga nominal',
			'recorrido_Cabina': 'Recorrido de la cabina',
			'recorido_Superior_Piston': 'Recorrido superior del piston',
			'cantidad_Pistones': 'Cantidad de pistones',
			'cantidad_Cilindros': 'Cantidad de cilindros',
			'numero_Expanciones': 'Cantidad de expanciones',
			'velocidad_Cabina': 'Velocidad de la cabina',
			'diametro_Cable': 'Diametro del cable',
			'peso_Ascensor': 'Peso del ascensor',
			'diametro_Piston': 'Diametro del piston',
			'masa_Embolo': 'Masa del embolo',
			'usuario': 'Usuario',	
		}

		# forms.select porque es una llave foranea

		widgets = {
			'numero_Cables': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Cables",'onkeypress':"return validar(event)",'id':"1",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'carga_Nominal': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Peso",'onkeypress':"return validar(event)",'id':"9",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'recorrido_Cabina': forms.Select(attrs={'class': 'form-control'},choices=pisos),
			'recorido_Superior_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Recorrido Piston",'onkeypress':"return validar(event)",'id':"2",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'cantidad_Pistones': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Pistones",'onkeypress':"return validar(event)",'id':"3",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'cantidad_Cilindros': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Cilindros",'onkeypress':"return validar(event)",'id':"4",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'numero_Expanciones': forms.Select(attrs={'class': 'form-control'},choices=expanciones),
			'diametro_Cable': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Diametro Del Cable",'onkeypress':"return validar(event)",'id':"5",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'velocidad_Cabina': forms.Select(attrs={'class': 'form-control'},choices= velocidades),
			'peso_Ascensor': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Peso",'onkeypress':"return validar(event)",'id':"6",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'diametro_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Diametro",'onkeypress':"return validar(event)",'id':"7",'onkeyup':"habilitar()",'onpaste':"return false"}),
			'masa_Embolo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Masa Embolo",'onkeypress':"return validar(event)",'id':"8",'onkeyup':"habilitar()",'onpaste':"return false"}),

			
		}
