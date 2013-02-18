# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from views import (IndexView, BiographyView, ContactView, PortfolioView,
    PresentView)

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='portafolio-index'),
    url(r'^portafolio/$', PortfolioView.as_view(), name='portafolio-albumes'),
    url(r'^biografia/$', BiographyView.as_view(), name='portafolio-biografia'),
    url(r'^actualidad/$', PresentView.as_view(), name='portafolio-actualidad'),
    url(r'^contacto/$', ContactView.as_view(), name='portafolio-contacto'),
    url(r'^portafolio/(?P<codigo>\w+)/$', PortfolioView.as_view(), name='portafolio-albumes'),
)