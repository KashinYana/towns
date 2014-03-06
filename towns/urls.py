from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import search, suggest

import settings

urlpatterns = patterns('',
    url(r'^$', search),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^suggest/$', suggest),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
                 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_ROOT}),              
)
