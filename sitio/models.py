from django.db import models

class Album(models.Model):
	nome = models.CharField(max_length = 200, blank = False, null = True)	
	data_criacao = models.DateField()	

	def __str__(self):
		return self.nome
		
	class Meta:
		verbose_name_plural = 'albuns' 

class Foto(models.Model):
	imagem = models.ImageField(blank=False)
	thumbnail = models.ImageField(upload_to = 'thumbnails/', blank = False, null = True)
	album = models.ForeignKey(Album, blank = False, null = True)

	def __str__(self):
		return 'imagem'
		
	class Meta:
		verbose_name = 'Foto' 