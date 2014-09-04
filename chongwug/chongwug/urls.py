from django.conf.urls import patterns, include, url
from customer.views import nav_page_view,buy_home_view
from back_manager.views import manage_home_view,manage_pet_farm_view,manage_pet_farm_add_view,manage_pet_farm_mod_view,manage_pet_farm_picadd_view,manage_pet_farm_picmod_view,manage_pet_farm_pic_upload_view,manage_pet_farm_picpre_view,manage_ad_view,manage_ad_add_view,manage_ad_mod_view,manage_ad_pic_upload_view,manage_ad_picpre_view
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',nav_page_view),
                       url(r'^home/$',buy_home_view),
                       url(r'^back_manage/$',manage_home_view),
                       url(r'^back_manage/ad/$',manage_ad_view),
                       url(r'^back_manage/ad/add/$',manage_ad_add_view),
                       url(r'^back_manage/ad/mod/$',manage_ad_mod_view),
                       url(r'^back_manage/ad/picadd/upload/$',manage_ad_pic_upload_view),
                       url(r'^back_manage/ad/picadd/preupload/$',manage_ad_picpre_view),
                       url(r'^back_manage/petfarm/$',manage_pet_farm_view),
                       url(r'^back_manage/petfarm/add/$',manage_pet_farm_add_view),
                       url(r'^back_manage/petfarm/mod/$',manage_pet_farm_mod_view),
                       url(r'^back_manage/petfarm/picadd/$',manage_pet_farm_picadd_view),
                       url(r'^back_manage/petfarm/picmod/$',manage_pet_farm_picmod_view),
                       url(r'^back_manage/petfarm/picadd/upload/$',manage_pet_farm_pic_upload_view),
                       url(r'^back_manage/petfarm/picadd/preupload/$',manage_pet_farm_picpre_view),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,'show_indexes':True  }),
    # Examples:
    # url(r'^$', 'chongwug.views.home', name='home'),
    # url(r'^chongwug/', include('chongwug.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
