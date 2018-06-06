from django.db import models

# Create your models here.
class Usuario(models.Model):
	idUsuario = models.CharField(max_length =10, primary_key=True)
	nombre = models.CharField(max_length=25)
	contraseña = models.CharField(max_length=10)


