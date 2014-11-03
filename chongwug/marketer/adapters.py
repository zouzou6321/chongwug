# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from back_manager.models import manage
from manager.models import ad,tmppic_monitor
from customer.models import user,nestofpet_attention
from petfarm.models import pet_farm,nestofpet
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.contrib.auth.models import User
import string,re,json
import os,uuid,datetime
from django.db.models import Q
'''
管理员鉴权
'''
def manage_authentication(request):
    try:
        if (request.session['manage_id'] == ''):
            return False
    except:
        return False
    return True

def manage_login_check(request):
    name = request.REQUEST.get('username')
    passwd = request.REQUEST.get('userpassd')
    request.session['manage_id'] = ''
    try:
        _manage = manage.objects.get(name=name,passwd=passwd)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return False
    request.session['manage_id'] = _manage.id
    request.session['score'] = _manage.permission_score
    return True

def manage_home_data_get(request):
    manager = manage.objects.get(id=request.session['manage_id'])
    return {'manager':manager}

def market_nestofpet_info_get(request):
    nestpets = nestofpet.objects.filter(sale_out=False,dele=False)
    nest_pets = []
    for nest_pet in nestpets:
        nest_pets.append({'nest_pet':nest_pet,'min_price':nest_pet.pet_set.order_by('-price')[0].price,'max_price':nest_pet.pet_set.order_by('price')[0].price})
    return nest_pets

def market_nestofpet_sale_set(request):
    try:
        if request.REQUEST.get('sale') == '0' or request.REQUEST.get('sale') == '1':
            nest_pet = nestofpet.objects.get(id=string.atoi(request.REQUEST.get('id')),dele=False)
            nest_pet.sale_out = string.atoi(request.REQUEST.get('sale'))
            nest_pet.save()
            return "True"
    except:
        return "ERROR"
    return "DATA ERROR"

def market_attention_mod(request):
    attention = nestofpet_attention.objects.get(id=string.atoi(request.POST['data[0]']),dele=False)
    attention.user.nickname = request.POST['data[1]']
    attention.user.tel = request.POST['data[2]']
    attention.attention_type = request.POST['data[4]']
    if request.POST['data[6]'] == 'true':
        attention.dele = True
    attention.save()
    data = u'''{"row": {"0":"%s","1":"%s","2":"%s","3":"%s","4":"%s","5":"%s","6":"%s"}}'''\
     % (attention.id, attention.user.nickname, attention.user.tel, attention.nestofpet_id.farm.name + \
        attention.nestofpet_id.type, attention.attention_type, attention.time, request.POST['data[6]'])
    
    return data

def attention_data(request):
    filter = request.REQUEST.get('filter')
    start = request.REQUEST.get('start')
    length = request.REQUEST.get('length')
    datas = []
    if filter == 'all':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=1).order_by('id')
    elif filter == 'processed':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=2).order_by('id')
    elif filter == 'untreated':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=3).order_by('id')
    elif filter == 'fail':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=4).order_by('id')
    count = attentions.count()
    attentions = attentions[start:length]
    for attention in attentions:
        data = {}
        data['id'] = attention.id
        data['DT_RowId'] = attention.id
        data['name'] = attention.user.nickname
        data['tel'] = attention.user.tel
        data['petfarm'] = attention.nestofpet_id.farm.name
        data['pettype'] = attention.nestofpet_id.type
        data['appointtime'] = attention.appoint_time.strftime('%Y-%m-%d %H:%M:%S')
        data['location'] = attention.user.location
        data['trans'] = attention.trans
        data['accept'] = attention.attention_type
        data['time'] = attention.time.strftime('%Y-%m-%d %H:%M:%S')
        datas.append(data)
    pagedata = {'data':datas,'draw':string.atoi(request.REQUEST.get('draw')),'recordsTotal':count, 'recordsFiltered': count}
    return json.dumps(pagedata)