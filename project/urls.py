from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'project.views.home', name='url_home'),
    url(r'^admin/', include(admin.site.urls)),    
]