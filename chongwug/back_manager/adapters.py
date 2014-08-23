# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from models import manage,pet_farm
import string

def manage_authentication(request):
    try:
        if (request.session['manage_id'] == ''):
            return False
    except NameError:
        return False
    return True

def manage_login_check(request):
    name = request.REQUEST.get('username')
    passwd = request.REQUEST.get('userpassd')
    request.session['manage_id'] = ''
    try:
        manage_id = manage.objects.get(name=name,passwd=passwd).id
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return False
    request.session['manage_id'] = manage_id
    return True

def manage_home_data_get(request):
    manager = manage.objects.get(id=request.session['manage_id'])
    return {'manager':manager}

def manage_pet_farm_add(request):
    try:
        if request.POST['province'] == '':
            province = '四川'
        else:
            province = request.POST['province']
        if request.POST['city'] == '':
            city = '成都'
        else:
            city = request.POST['city']
        if request.POST['manage_score'] == '':
            manage_score = 1.0
        else:
            manage_score = string.atof(request.POST['manage_score'])
        new_pet_farm = pet_farm(name = request.POST['name'],
                                desc = request.POST['desc'],
                                province = province,
                                city = city,
                                district = request.POST['district'],
                                direct = request.POST['direct'],
                                min_prince = request.POST['min_prince'],
                                manage_score = manage_score)
        new_pet_farm.save()
    except NameError:
        return False
    return True