# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from back_manager.views import manage_home_view,manage_pet_farm_view,manage_pet_farm_add_view,manage_pet_farm_mod_view,manage_pet_farm_picadd_view,manage_pet_farm_picmod_view,manage_pet_farm_pic_upload_view,manage_pet_farm_picpre_view,manage_ad_view,manage_ad_add_view,manage_ad_mod_view,manage_ad_pic_upload_view,manage_ad_picpre_view,manage_manager_view,manage_nestofpet_add_view
from back_manager.views import manage_nestofpet_picadd_view,manage_nestofpet_farmselect_view,manage_nestofpet_pic_upload_view,manage_nestofpet_picpre_view,manage_nestofpet_view
urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       url(r'^ad/$',manage_ad_view),
                       url(r'^ad/add/$',manage_ad_add_view),
                       url(r'^ad/mod/$',manage_ad_mod_view),
                       url(r'^ad/picadd/upload/$',manage_ad_pic_upload_view),
                       url(r'^ad/picadd/preupload/$',manage_ad_picpre_view),
                       url(r'^manager/$',manage_manager_view),
                       url(r'^nestofpet/$',manage_nestofpet_view),
                       url(r'^nestofpet/add/$',manage_nestofpet_add_view),
                       url(r'^nestofpet/picadd/$',manage_nestofpet_picadd_view),
                       url(r'^nestofpet/picadd/upload/$',manage_nestofpet_pic_upload_view),
                       url(r'^nestofpet/picadd/preupload/$',manage_nestofpet_picpre_view),
                       url(r'^nestofpet/picadd/farmselect/$',manage_nestofpet_farmselect_view),
                       url(r'^petfarm/$',manage_pet_farm_view),
                       url(r'^petfarm/add/$',manage_pet_farm_add_view),
                       url(r'^petfarm/mod/$',manage_pet_farm_mod_view),
                       url(r'^petfarm/picadd/$',manage_pet_farm_picadd_view),
                       url(r'^petfarm/picmod/$',manage_pet_farm_picmod_view),
                       url(r'^petfarm/picadd/upload/$',manage_pet_farm_pic_upload_view),
                       url(r'^petfarm/picadd/preupload/$',manage_pet_farm_picpre_view),
                       )