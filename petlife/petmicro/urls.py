# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
urlpatterns = patterns(
                       '',
                       url(r'^$', 'petmicro.views.home', name='home'),
                       url(r'^login/$', 'petmicro.views.login', name='login'),
                       url(r'^pwdback/$', 'petmicro.views.pwdback', name='pwdback'),
                       )