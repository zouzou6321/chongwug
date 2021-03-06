# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from views import market_usr_unpayclose_info_view,market_usr_unpay_info_view,market_usr_attention_mod_select_view,market_attention_data_view,manage_home_view,market_usr_attention_info_view,market_usr_attention_mod_view,market_nestofpet_info_view,market_usr_processed_info_view,market_usr_untreated_info_view,market_usr_fail_info_view,market_usr_success_info_view

urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       url(r'^attention/$',market_usr_attention_info_view),
                       url(r'^processed/$',market_usr_processed_info_view),
                       url(r'^untreated/$',market_usr_untreated_info_view),
                       url(r'^fail/$',market_usr_fail_info_view),
                       url(r'^success/$',market_usr_success_info_view),
                       url(r'^unpay/$',market_usr_unpay_info_view),
                       url(r'^unpayclose/$',market_usr_unpayclose_info_view),
                       url(r'^attention/data/$', market_attention_data_view),
                       url(r'^attention/mod/$',market_usr_attention_mod_view),
                       url(r'^attention/mod/select/$',market_usr_attention_mod_select_view),
                       url(r'^nestofpet/$',market_nestofpet_info_view),
                       )