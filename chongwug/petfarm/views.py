# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
import adapters
from chongwug.commom import __errorcode__
PETFARM_ROOT='/petfarm/'

def manage_login(request):
    return render_to_response('petfarm/tpl/manage_login.html',{},context_instance=RequestContext(request))

#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'POST' and 'username' in request.POST and 'userpassd'  in request.POST:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(PETFARM_ROOT)
    if request.method == 'GET' and 'logout' in request.GET:
        auth.logout(request)
        return HttpResponseRedirect(PETFARM_ROOT)
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    data = adapters.manage_home_data_get(request)
    return render_to_response('petfarm/tpl/manage_home.html',data)

def address_handle_view(request):
    data = adapters.addressHandle(request);
    return HttpResponse(data.__str__())

def manage_pet_farm_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(PETFARM_ROOT)
    if request.method == 'POST':
        return HttpResponse(adapters.manage_pet_farm_mod(request))
    data = adapters.addressHandle(request)
    data['manager'] = adapters.manage_home_data_get(request)['manager']
    data['types'] = adapters.get_farmpic_types()['types']
    data['farmimgs'] = adapters.get_farmpics(data['manager'])
    return render_to_response('petfarm/tpl/manage_pet_farm_mod.html',data,context_instance=RequestContext(request))

@csrf_exempt
def manage_nestofpet_pic_upload_view(request):
    photo = request.FILES.get('Filedata',None)
    imgw,imgh = adapters.petpic_upload_pre(request)
    return HttpResponse(adapters.manage_picupload(photo,imgw,imgh))

@csrf_exempt
def manage_pet_farm_pic_upload_view(request):
    photo = request.FILES.get('Filedata',None)
    imgw,imgh = adapters.farmpic_upload_pre(request)
    return HttpResponse(adapters.manage_picupload(photo,imgw,imgh))

def manage_nestofpet_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(PETFARM_ROOT)
    
    data = adapters.manage_home_data_get(request)
    if request.method == 'POST':
        return HttpResponse(adapters.manage_nestofpet_mod(request))
    else:
        if "id" in request.GET:
            if 'del' in request.GET:
                return HttpResponse(adapters.manage_del_pet(request))
            data = adapters.manage_nestofpet_mod_info(request)
            data['types'] = adapters.get_petpic_types()['types']
            return render_to_response('petfarm/tpl/manage_nestofpet_mod_ajax.html',data)
    pagedata = adapters.manage_nestofpet_mod_info(request)
    data['types'] = adapters.get_petpic_types()['types']
    pagedata['manager'] = data['manager']
    return render_to_response('petfarm/tpl/manage_nestofpet_mod.html',pagedata,context_instance=RequestContext(request))

def manage_nestofpet_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(PETFARM_ROOT)
    
    if request.method == 'POST':
        return HttpResponse(adapters.manage_nestofpet_add(request))
    
    data = adapters.manage_home_data_get(request)
    data['types'] = adapters.get_petpic_types()['types']
    data['pettypes'] = adapters.get_pet_types()['pettypes']
    data['petcolors'] = adapters.get_pet_colors()['petcolors']
    data['petages'] = adapters.get_pet_ages()['petages']
    return render_to_response('petfarm/tpl/manage_pet_add.html',data,context_instance=RequestContext(request))