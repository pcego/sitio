from django.db import models

class Album(models.Model):
	nome = models.CharField(max_length = 200)
	data_criacao = models.DateField()

class Foto(models.Model):
	imagem = models.ImageField(upload_to='static/media/', blank=False,null=False)
	    