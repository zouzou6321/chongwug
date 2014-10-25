from django.conf.urls import patterns, include, url
import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('customer.urls')),
                       url(r'^back_manage/', include('back_manager.urls')),
                       url(r'^petfarm/', include('petfarm.urls')),
                       url(r'^manage/', include('manager.urls')),
                       url(r'^market/', include('marketer.urls')),
                       url(r'^crossdomain.xml$',direct_to_template,{'template': 'crossdomain.xml', 'mimetype': 'text/xml'}),
    # Examples:
    # url(r'^$', 'chongwug.views.home', name='home'),
    # url(r'^chongwug/', include('chongwug.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.STATIC_PATH_URL:
    urlpatterns.append(settings.STATIC_PATH_URL)