from django.http import HttpResponse
from django.shortcuts import render
from sitio.models import Album, Foto


def home(request):	
	return render(request, 'index.html')

def piscina(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Piscina')	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)

def chale(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Chales')	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)

def cozinha(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Cozinha')	
	data['foto'] = fotos

	return render(request, 'gallery.html', data)

def geral(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Geral')	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)

def churrasqueira(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Churrasqueira')	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)

def esporte(request):
	data = {}
	fotos = Foto.objects.filter(album__nome = 'Esportes')	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)