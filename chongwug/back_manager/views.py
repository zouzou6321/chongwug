# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import adapters
MANAGE_ROOT='/back_manage/'
def manage_login(request):
    return render_to_response('manage/tpl/manage_login.html')
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
    return render_to_response('manage/tpl/manage_home.html',data)

def manage_pet_farm_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'POST':
        if adapters.manage_pet_farm_add(request) == False:
            return HttpResponse("data error occur!!!")
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet_farm_add.html',data,context_instance=RequestContext(request))
def manage_pet_farm_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet_farm.html',data)
def manage_pet_farm_picadd_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    page_data = adapters.manage_pet_farm_picadd(request)
    data = adapters.manage_home_data_get(request)
    page_data['manager'] = data['manager']
    return render_to_response('manage/tpl/manage_pet_farm_picadd.html',page_data,context_instance=RequestContext(request))

def manage_nestofpet_picadd_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    page_data = adapters.manage_nestofpet_picadd(request)
    data = adapters.manage_home_data_get(request)
    page_data['manager'] = data['manager']
    return render_to_response('manage/tpl/manage_pet_picadd.html',page_data,context_instance=RequestContext(request))

@csrf_exempt
def manage_nestofpet_pic_upload_view(request):
    photo = request.FILES.get('Filedata',None)
    imgw = 200
    imgh = 160
    if request.REQUEST.get('usefor') == 'narmol':
        imgw = 600
        imgh = 400
    elif request.REQUEST.get('usefor') == 'buy_main':
        imgw = 200
        imgh = 160
    return HttpResponse(adapters.manage_picupload(photo,imgw,imgh))

@csrf_exempt
def manage_pet_farm_pic_upload_view(request):
    photo = request.FILES.get('Filedata',None)
    return HttpResponse(adapters.manage_picupload(photo,200,160))

def manage_pet_farm_picpre_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponse('false')
    return HttpResponse(adapters.manage_pet_farm_picpreupload(request))

def manage_nestofpet_picpre_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponse('false')
    return HttpResponse(adapters.manage_nestofpet_picpreupload(request))

def manage_nestofpet_farmselect_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponse('false')
    return HttpResponse(adapters.manage_nestofpet_farmselect(request))

def manage_pet_farm_picmod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet_farm.html',data)

def manage_pet_farm_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet_farm.html',data)

def manage_ad_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_ad.html',data)

def manage_pet_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet.html',data)

def manage_nestofpet_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_pet.html',data)

def manage_nestofpet_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'POST':
        if adapters.manage_nestofpet_add(request) == False:
            return HttpResponse("data error occur!!!")
    page_data = adapters.pet_farm_all()
    data = adapters.manage_home_data_get(request)
    page_data['manager'] = data['manager']
    return render_to_response('manage/tpl/manage_pet_add.html',page_data,context_instance=RequestContext(request))

def manage_ad_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_ad_picadd.html',data,context_instance=RequestContext(request))

@csrf_exempt
def manage_ad_pic_upload_view(request):
    photo = request.FILES.get('Filedata',None)
    return HttpResponse(adapters.manage_picupload(photo))
def manage_ad_picpre_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponse('false')
    return HttpResponse(adapters.manage_ad_picpreupload(request,1170,500))

def manage_ad_mod_view(request):
    return True

def manage_manager_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_manager.html',data,context_instance=RequestContext(request))
