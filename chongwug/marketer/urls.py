# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from views import manage_home_view,market_usr_attention_info_view,market_usr_attention_mod_view,market_nestofpet_info_view
from adapters import OrderListJson
from django.contrib.auth.decorators import login_required
urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       url(r'^attention/$',market_usr_attention_info_view),
                       url(r'^attention/data/$', login_required(OrderListJson.as_view()), name='order_list_json'),
                       url(r'^attention/mod/$',market_usr_attention_mod_view),
                       url(r'^nestofpet/$',market_nestofpet_info_view),
                       )