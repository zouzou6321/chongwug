# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from chongwug import config
import adapters,json
from chongwug.commom import __errorcode__
PETFARM_ROOT='/petfarm/'

def manage_login(request,error=''):
    return render_to_response('petfarm/tpl/manage_login.html',{'error':error},context_instance=RequestContext(request))

def manage_regist_view(request):
    if request.method == 'POST':
        data = adapters.petfarm_regist(request)
        return HttpResponse(data)
    if 'tel' in request.GET:
        if request.session['validate'].upper() != request.REQUEST.get('verify').upper():
            return HttpResponse(__errorcode__(30))
        data = adapters.petfarm_regist_sendcheck(request)
        return HttpResponse(data)
    data = adapters.addressHandle(request)
    data['petfarmtypes'] = config.__petfarmtypes
    return render_to_response('petfarm/tpl/manage_regist.html',data,context_instance=RequestContext(request))

@csrf_exempt
def manage_regist_picadd_view(request):
    photo = request.FILES.get('Filedata',None)
    imgw,imgh = 500,500
    return HttpResponse(adapters.manage_picupload(photo,imgw,imgh))

from chongwug.validatecode import create_validate_code
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
def manage_validate_view(request):
    mstream = StringIO.StringIO()
    
    validate_code = create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")
    
    request.session['validate'] = validate_code[1]
    
    return HttpResponse(mstream.getvalue(), "image/gif")

def manage_pwdforgot_view(request):
    if 'email' in request.POST:
        return HttpResponse(adapters.manage_pwdforgot(request))
    return render_to_response('petfarm/tpl/manage_pwdforgot.html',{},context_instance=RequestContext(request))

#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'POST' and 'username' in request.POST and 'userpassd'  in request.POST:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(PETFARM_ROOT)
        else:
            return manage_login(request,u'账号或密码错误')
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    if request.method == 'GET' and 'logout' in request.GET:
        adapters.manage_logout(request)
        return HttpResponseRedirect(PETFARM_ROOT)
    data = adapters.manage_home_data_get(request)
    return render_to_response('petfarm/tpl/manage_home.html',data)

def address_handle_view(request):
    data = adapters.addressHandle(request);
    return HttpResponse(json.dumps(data))

def manage_pet_farm_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(PETFARM_ROOT)
    if request.method == 'POST':
        return HttpResponse(adapters.manage_pet_farm_mod(request))
    data = adapters.addressHandle(request)
    data['manager'] = adapters.manage_home_data_get(request)['manager']
    data['types'] = adapters.get_farmpic_types()['types']
    data['farmimgs'] = adapters.get_farmpics(data['manager'])
    form = adapters.descform()
    medialist = str(form.media).split('\n')
    media = '%s\n%s' % (medialist[-2],medialist[-1])
    data['form'] = form
    data['media'] = media
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
    pagedata['types'] = adapters.get_petpic_types()['types']
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
    data['petages'] = adapters.get_pet_ages()['petages']
    return render_to_response('petfarm/tpl/manage_pet_add.html',data,context_instance=RequestContext(request))