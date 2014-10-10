# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from back_manager.models import manage
from manager.models import ad,tmppic_monitor
from customer.models import user,nestofpet_attention
from petfarm.models import pet_farm
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.contrib.auth.models import User
import string,re
import os,uuid,datetime
from django_datatables_view.base_datatable_view import BaseDatatableView
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

def market_attention_mod(request):
    attention = nestofpet_attention.objects.get(id=string.atoi(request.POST['data[0]']),dele=False)
    attention.user.name = request.POST['data[1]']
    attention.user.tel = request.POST['data[2]']
    attention.attention_type = request.POST['data[4]']
    if request.POST['data[6]'] == 'true':
        attention.dele = True
    attention.save()
    data = u'''{"row": {"0":"%s","1":"%s","2":"%s","3":"%s","4":"%s","5":"%s","6":"%s"}}'''\
     % (attention.id, attention.user.name, attention.user.tel, attention.nestofpet_id.farm.name + \
        attention.nestofpet_id.type, attention.attention_type, attention.time, request.POST['data[6]'])
    
    return data
class OrderListJson(BaseDatatableView):
            # The model we're going to show
            model = nestofpet_attention
            # define the columns that will be returned
            columns = ['id', 'name', 'tel', 'nestofpet_id', 'attention_type','time','dele']

            # define column names that will be used in sorting
            # order is important and should be same as order of columns
            # displayed by datatables. For non sortable columns use empty
            # value like ''
            order_columns = []

            # set max limit of records returned, this is used to protect our site if someone tries to attack our site
            # and make it return huge amount of data
            max_display_length = 100

            def render_column(self, row, column):
                # We want to render user as a custom column
                if column == 'nestofpet_id':
                    return '%s %s' % (row.nestofpet_id.farm.name, row.nestofpet_id.type)
                elif column == 'name':
                    return row.user.name
                elif column == 'tel':
                    return row.user.tel
                else:
                    return super(OrderListJson, self).render_column(row, column)
            
            def ordering(self, qs):
                return qs
            def filter_queryset(self, qs):
                # use request parameters to filter queryset
                qs = qs.filter(dele=False)
                # simple example:
                sSearch = self.request.POST.get('sSearch', None)
                if sSearch:
                    qs = qs.filter(name__istartswith=sSearch)

                # more advanced example
                filter_customer = self.request.POST.get('customer', None)

                if filter_customer:
                    customer_parts = filter_customer.split(' ')
                    qs_params = None
                    for part in customer_parts:
                        q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                        qs_params = qs_params | q if qs_params else q
                    qs = qs.filter(qs_params)
                return qs
