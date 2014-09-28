# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from manager.views import manage_home_view,manage_pet_farm_add_view,manage_ad_add_view,manage_ad_mod_view,manage_ad_pic_upload_view,manage_ad_picpre_view
urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       
                       url(r'^ad/add/$',manage_ad_add_view),
                       url(r'^ad/mod/$',manage_ad_mod_view),
                       url(r'^ad/picadd/upload/$',manage_ad_pic_upload_view),
                       url(r'^ad/picadd/preupload/$',manage_ad_picpre_view),
                       url(r'^petfarm/add/$',manage_pet_farm_add_view),
                       )