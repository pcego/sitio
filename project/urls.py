from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 	
    url(r'^$', 'project.views.home', name='url_home'),    
    url(r'^fotos/piscina$', 'project.views.piscina', name = 'url_fotos_piscina'), 
    url(r'^fotos/chales$', 'project.views.chale', name = 'url_fotos_chales'), 
    url(r'^fotos/cozinha$', 'project.views.cozinha', name = 'url_fotos_cozinha'), 
    url(r'^fotos/churrasqueira$', 'project.views.churrasqueira', name = 'url_fotos_churrasqueira'), 
    url(r'^fotos/geral$', 'project.views.geral', name = 'url_fotos_geral'), 
    url(r'^fotos/esportes$', 'project.views.esporte', name = 'url_fotos_esportes'), 

]