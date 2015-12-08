from django.http import HttpResponse
from django.shortcuts import render
from sitio.models import Album, Foto


def home(request):
	return render(request, 'index.html')

def piscina(request):
	data = {}
	fotos = Foto.objects.all	
	data['foto'] = fotos	
	
	return render(request, 'gallery.html', data)

def chale(request):
	return HttpResponse('teste chales')

def cozinha(request):
	return HttpResponse('teste cozinha')

def geral(request):
	return HttpResponse('teste geral')

def churrasqueira(request):
	return HttpResponse('teste churrasqueira')

def esporte(request):
	return HttpResponse('teste esportes')