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
			'usuario': 'Usuario',
		}

		# forms.select porque es una llave foranea

		widgets = {
			'numero_Cables': forms.TextInput(attrs={'class': 'form-control'}),
			'carga_Nominal': forms.TextInput(attrs={'class': 'form-control'}),
			'recorrido_Cabina': forms.TextInput(attrs={'class': 'form-control'}),
			'recorido_Superior_Piston': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_Pistones': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_Cilindros': forms.TextInput(attrs={'class': 'form-control'}),
			'numero_Expanciones': forms.TextInput(attrs={'class': 'form-control'}),
			'velocidad_Cabina': forms.TextInput(attrs={'class': 'form-control'}),
			'usuario': forms.Select(attrs={'class': 'form-control'}),
		}
