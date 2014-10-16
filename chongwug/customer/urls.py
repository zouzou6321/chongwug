# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from customer.views import nav_page_view,buy_home_view,buy_main_view,buy_detail_view,buy_attention_view,knowledge_buy_view
urlpatterns = patterns(
                       '',
                       url(r'^$',nav_page_view),
                       url(r'^home/$',buy_home_view),
                       url(r'^buy/$',buy_main_view),
                       url(r'^buy/detail/$',buy_detail_view),
                       url(r'^buy/detail/attention/$',buy_attention_view),
                       url(r'^knowledge/buy/$',knowledge_buy_view),
                       )