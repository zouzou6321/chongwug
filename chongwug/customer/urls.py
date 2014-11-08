# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from customer.views import supplie_view,buy_attention_sendsms_view,knowledge_bringup_view,aboutus_view,workchance_view,contactus_view,nav_page_view,buy_home_view,buy_main_view,buy_detail_view,buy_attention_view,knowledge_buy_view
urlpatterns = patterns(
                       '',
                       url(r'^$',nav_page_view),
                       url(r'^home/$',buy_home_view),
                       url(r'^buy/$',buy_main_view),
                       url(r'^buy/detail/$',buy_detail_view),
                       url(r'^buy/detail/attention/$',buy_attention_view),
                       url(r'^buy/detail/attention/sendsms/$',buy_attention_sendsms_view),
                       url(r'^knowledge/buy/$',knowledge_buy_view),
                       url(r'^knowledge/bringup/$',knowledge_bringup_view),
                       url(r'^supplie/$',supplie_view),
                       url(r'^aboutus/$',aboutus_view),
                       url(r'^workchance/$',workchance_view),
                       url(r'^contactus/$',contactus_view),
                       )