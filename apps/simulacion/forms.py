from django import forms
from apps.simulacion.models import Simulador


class SimulacionForm(forms.ModelForm):

	class Meta:
		model = Simulador

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
			'numero_Cables': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"cables"}),
			'carga_Nominal': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"peso"}),
			'recorrido_Cabina': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"recorrido"}),
			'recorido_Superior_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"recorrido piston"}),
			'cantidad_Pistones': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Pistones"}),
			'cantidad_Cilindros': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"cilindros"}),
			'numero_Expanciones': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"expanciones"}),
			'diametro_Cable': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"diametro del cable"}),
			'velocidad_Cabina': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"velocidad"}),
			'peso_Ascensor': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"peso"}),
			'diametro_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"diametro"}),
			'masa_Embolo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"masa embolo"}),
			
		}
