from django.conf.urls import patterns, include, url
from customer.views import nav_page_view,buy_home_view,buy_main_view,buy_detail_view,buy_attention_view
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',nav_page_view),
                       url(r'^home/$',buy_home_view),
                       url(r'^buy/$',buy_main_view),
                       url(r'^buy/detail/$',buy_detail_view),
                       url(r'^buy/detail/attention/$',buy_attention_view),
                       url(r'^back_manage/', include('back_manager.urls')),
                       url(r'^petfarm/', include('petfarm.urls')),
                       url(r'^manage/', include('manager.urls')),
                       url(r'^market/', include('marketer.urls')),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes':True  }),
    # Examples:
    # url(r'^$', 'chongwug.views.home', name='home'),
    # url(r'^chongwug/', include('chongwug.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
