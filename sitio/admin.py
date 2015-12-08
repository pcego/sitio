from django.contrib import admin
from sitio.models import Album, Foto

class AlbumAdmin(admin.ModelAdmin):
	vebose_name = 'Album Fotos'
	

class FotoAdmin(admin.ModelAdmin):
	vebose_name = 'Fotos'	


admin.site.register(Album, AlbumAdmin)
admin.site.register(Foto, FotoAdmin)