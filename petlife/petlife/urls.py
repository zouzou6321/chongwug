from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^petmicro/', include('petmicro.urls')),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,'show_indexes':False  }),
                       url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'petlife.views.home', name='home'),
    # url(r'^petlife/', include('petlife.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
