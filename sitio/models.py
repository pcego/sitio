from django.db import models

class Album(models.Model):
	nome = models.CharField(max_length = 200, blank = True, null = True)	
	data_criacao = models.DateField()

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name_plural = 'albuns'


class Foto(models.Model):
	imagem = models.ImageField(blank=False)	
	album = models.ForeignKey(Album)

	def __str__(self):
		return self.album.nome

	class Meta:
		verbose_name = 'Foto'

class Thumbnail(models.Model):
	album = models.ForeignKey(Album)
	thumbnail = models.ImageField(upload_to = 'thumbnails/')

	def __str__(self):
		return self.album.nome 


	    