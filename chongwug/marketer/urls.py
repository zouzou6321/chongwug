# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from views import market_attention_data_view,manage_home_view,market_usr_attention_info_view,market_usr_attention_mod_view,market_nestofpet_info_view

urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       url(r'^attention/$',market_usr_attention_info_view),
                       url(r'^attention/data/$', market_attention_data_view),
                       url(r'^attention/mod/$',market_usr_attention_mod_view),
                       url(r'^nestofpet/$',market_nestofpet_info_view),
                       )