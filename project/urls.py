# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    #ADMINISTRACION
    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    #PUBLICO
    (r'^', include('home.urls')),
)

from django.views.static import serve
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),    
)

handler500 = 'home.views.internal_error_view'