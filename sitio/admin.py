from django.contrib import admin
from sitio.models import Album, Foto

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('nome', 'data_criacao')
	verbose_name_plural = 'Albuns'

class FotoAdmin(admin.ModelAdmin):
	verbose_name_plural = 'Fotos'


admin.site.register(Album, AlbumAdmin)
admin.site.register(Foto, FotoAdmin)




