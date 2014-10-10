# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from views import manage_home_view,market_usr_attention_info,market_usr_attention_mod
from adapters import OrderListJson
from django.contrib.auth.decorators import login_required
urlpatterns = patterns(
                       '',
                       url(r'^$',manage_home_view),
                       url(r'^attention/$',market_usr_attention_info),
                       url(r'^attention/data/$', login_required(OrderListJson.as_view()), name='order_list_json'),
                       url(r'^attention/mod/$',market_usr_attention_mod),
                       )