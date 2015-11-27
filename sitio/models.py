from django.db import models

class Album(models.Model):
	nome = models.CharField(max_length = 200, blank = True, null = True)
	data_criacao = models.DateField()


class Foto(models.Model):
	imagem = models.ImageField(blank=False)
	legenda = models.CharField(max_length = 100, blank = True, null = True)
	album = models.ForeignKey(Album)
	
	    