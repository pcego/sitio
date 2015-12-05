from django.contrib import admin
from sitio.models import Album, Foto, Thumbnail

class AlbumAdmin(admin.ModelAdmin):
	vebose_name = 'Album Fotos'
	

class FotoAdmin(admin.ModelAdmin):
	vebose_name = 'Fotos'	

class ThumbnailAdmin(admin.ModelAdmin):
	verbose_name = 'Miniaturas'

admin.site.register(Album, AlbumAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)