# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
import adapters
MANAGE_ROOT='/back_manage/'
def manage_login(request):
    return render_to_response('tpl/manage_login.html')
#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'GET' and 'username' in request.GET and 'userpassd'  in request.GET:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'GET' and 'logout' in request.GET:
        request.session['manage_id'] = ''
        return HttpResponseRedirect(MANAGE_ROOT)
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_home.html',data)

def manage_pet_farm_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'POST':
        if adapters.manage_pet_farm_add(request) == False:
            return HttpResponse("data error occur!!!")
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_pet_farm_add.html',data,context_instance=RequestContext(request))
def manage_pet_farm_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_pet_farm.html',data)
def manage_pet_farm_picadd_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_pet_farm.html',data)
def manage_pet_farm_picmod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_pet_farm.html',data)
def manage_pet_farm_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('tpl/manage_pet_farm.html',data)