# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
                       'customer.views',
                       url(r'^$','nav_page_view'),
                       url(r'^home/$','buy_home_view'),
                       url(r'^buy/$','buy_main_view'),
                       url(r'^buy/(?P<direct>[^/]+)/(?P<type>[^/]+)/(?P<prince>\d+)/(?P<age>\d+)/(?P<epidemic>[^/]+)/(?P<key>[^/]+)/(?P<curpage>\d+)/$','buy_main_view'),
                       url(r'^buy/detail/$','buy_detail_view'),
                       url(r'^buy/detail/(?P<petid>\d+)/$','buy_detail_view'),
                       url(r'^buy/detail/attention/$','buy_attention_view'),
                       url(r'^buy/detail/attention/sendsms/$','buy_attention_sendsms_view'),
                       url(r'^knowledge/buy/$','knowledge_buy_view'),
                       url(r'^knowledge/bringup/$','knowledge_bringup_view'),
                       url(r'^supplie/$','supplie_view'),
                       url(r'^aboutus/$','aboutus_view'),
                       url(r'^workchance/$','workchance_view'),
                       url(r'^contactus/$','contactus_view'),
                       )