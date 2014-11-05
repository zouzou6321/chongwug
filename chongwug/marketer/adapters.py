# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from back_manager.models import manage
from customer.models import nestofpet_attention
from petfarm.models import pet_farm,nestofpet
from chongwug.config import __addresses,__appointtime,__appointdays
from chongwug.commom import __errorcode__
import string,json
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
    name = request.POST['username']
    passwd = request.POST['userpassd']
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
    filter = request.REQUEST.get('filter')
    attention = False
    if filter == 'appoint':
        attention = nestofpet_attention.objects.get(id=string.atoi(request.POST['id']), dele=False,attention_type=1)
        if request.POST['data[accept]'] == '2':
            attention.attention_type = 2
        elif request.POST['data[accept]'] == '3':
            attention.attention_type = 3
    elif filter == 'processed':
        attention = nestofpet_attention.objects.get(id=string.atoi(request.POST['id']), dele=False,attention_type=2)
        if request.POST['data[accept]'] == '5':
            attention.attention_type = 5
        elif request.POST['data[accept]'] == '3':
            attention.attention_type = 3
        elif request.POST['data[name]'] == '4':
            attention.attention_type = 4
    elif filter == 'untreated':
        attention = nestofpet_attention.objects.get(id=string.atoi(request.POST['id']), dele=False,attention_type=3)
        if request.POST['data[accept]'] == '4':
            attention.attention_type = 4
        elif request.POST['data[accept]'] == '2':
            attention.attention_type = 2
            
    if not attention:
        fieldErrors = [{'name':'filter','status':'can not find this'}]
        return json.dumps({'fieldErrors': fieldErrors})
    attention.save()
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
    
    return json.dumps({'row': data})

def attention_data(request):
    filter = request.REQUEST.get('filter')
    start = request.REQUEST.get('start')
    length = request.REQUEST.get('length')
    datas = []
    if filter == 'appoint':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=1).order_by('id')
    elif filter == 'processed':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=2).order_by('id')
    elif filter == 'untreated':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=3).order_by('id')
    elif filter == 'fail':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=4).order_by('id')
    elif filter == 'success':
        attentions = nestofpet_attention.objects.filter(dele=False,attention_type=5).order_by('id')
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

def market_untreated_info(request):
    petfarms = pet_farm.objects.filter(dele=False)
    return {'petfarms':petfarms,'appointtime':__appointtime,'appointdays':__appointdays,'addresses':__addresses}

def select_change(request):
    if 'petfarm' in request.GET:
        petfarm = pet_farm.objects.get(id=request.REQUEST.get('petfarm'),dele=False)
        pettypes = petfarm.nestofpet_set.filter(dele=False).values('type').distinct()
        return json.dumps([ i['type'] for i in pettypes ])
    elif 'range' in request.GET:
        addresses = __addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]
        if 'city' in request.GET:
            addresses = addresses['sublist'][string.atoi(request.REQUEST.get('city'))]
        if 'district' in request.GET:
            addresses = addresses['sublist'][string.atoi(request.REQUEST.get('district'))]
        arr = []
        for address in addresses['sublist']:
            arr.append({'id': address['index'], 'name': address['name']})
        return {'locations': arr}
    return __errorcode__(1)