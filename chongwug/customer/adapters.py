# -*- coding: UTF-8 -*-
'''
文件功能：针对购宠用户涉及的页面，根据展示的数据需要，整理出格式化的数据返回
'''
from manager.models import ad
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img,pet
from customer.models import attention_user,nestofpet_attention
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import simplejson

import datetime,string,re
'''
函数功能：首页数据适配器
作者：胡怀勇
时间：2014-9-22
'''
def buy_home_adapter(request):
    #前期只有一个城市：成都
    contry = "china"
    province = "四川"
    city = "成都"
    enum_farms = []
    
    #获取首页需要展示的广告信息
    ads = ad.objects.filter(Q(type__exact = 'nav_m'),Q(dele__exact = False),Q(start_time__lte = datetime.datetime.now),Q(end_time__gte = datetime.datetime.now)).order_by('-prince')
    
    #目前是3个广告，需要考虑数据库中找不全可用广告的场景
    ads0 = False
    ads1 = False
    ads2 = False
    ads_count = ads.count()
    if ads_count > 0:
        ads0 = ads[0]
    if ads_count > 1:
        ads1 = ads[1]
    if ads_count > 2:
        ads2 = ads[2]
    data = {'ads': ads}

    #获取养殖场信息，同时考虑信息获取不完整的情况，确保页面不崩溃
    city_farms = pet_farm.objects.filter(contry=contry,province=province,city=city)
    for city_farm in city_farms:
        try:
            pet = nestofpet.objects.filter(farm=city_farm,dele=False,sale_out=False).order_by('-min_price')[0]
            city_farm.min_prince = pet.min_price
            city_farm.save()
        except:
            None
    enum_farms.append({'direct':'东','name':'east_farm','picname':'east_farm_img'})
    enum_farms.append({'direct':'西','name':'west_farm','picname':'west_farm_img'})
    enum_farms.append({'direct':'南','name':'south_farm','picname':'south_farm_img'})
    enum_farms.append({'direct':'北','name':'north_farm','picname':'north_farm_img'})
    enum_farms.append({'direct':'中','name':'center_farm','picname':'center_farm_img'})
    for farm in enum_farms:
        tmp_farm = city_farms.filter(direct=farm['direct'],dele=False).order_by('manage_score')
        if tmp_farm.count() > 0:
            tmp_farm = tmp_farm[0]
            tmp_farm_img = pet_farm_img.objects.filter(pet_farm_id=tmp_farm,img_usefor='buy_home',dele=False)
            if tmp_farm_img.count() > 0:
                tmp_farm_img = tmp_farm_img[0]
            else:
                tmp_farm_img = None
        else:
            tmp_farm = None
            tmp_farm_img = None
        data[farm['name']] = tmp_farm
        data[farm['picname']] = tmp_farm_img
    data['page'] = 'home'
    return data

'''
函数功能：购宠页面数据适配器，
作者：胡怀勇
时间：2014-9-22
'''
def buy_main_adapter(re):
    cur_url = '/buy/?'
    url = cur_url
    price = None
    #筛选条件
    types = [u'泰迪',u'比熊',u'金毛',u'萨摩耶',u'哈士奇',u'拉布拉多',u'边牧',u'松狮',u'阿拉斯加',u'博美',u'巴哥',u'雪纳瑞',u'约克夏',u'德牧',u'古牧',u'比格',u'喜乐蒂',u'斗牛犬',u'杜宾',u'罗威纳',u'吉娃娃']
    princes = [{'a':'1','b':600,'c':1000},{'a':'2','b':1000,'c':1500},{'a':'3','b':1500,'c':2000},{'a':'4','b':2000,'c':2500},{'a':'5','b':2500,'c':1000000}]
    directs = [u'东',u'西',u'南',u'北',u'中']
    epidemics = [u'已种疫苗',u'可种疫苗',u'未种疫苗']
    ages = [{'a':'1','b':0,'c':3},{'a':'2','b':3,'c':5},{'a':'3','b':5,'c':12},{'a':'4','b':12,'c':100000}]
    
    #筛选条件所对应的数据表列名称，从enums中获取
    typekey = None
    princekey = None
    directkey = None
    epidemickey = None
    agekey = None
    searchkey = None
    if 'key' in re.GET:
        #只是简单检索养殖场名称、养殖场地址
        searchkey = re.REQUEST.get('key')
        url = cur_url + 'key=' + searchkey + '&'
    
    #数据库查询语句整合
    kwargs = {}
    kwargs['dele'] = False
    kwargs['sale_out'] = False
    
    #取消某筛选条件时的url需要独立处理
    type_all_url = url
    prince_all_url = url
    direct_all_url = url
    epidemic_all_url = url
    age_all_url = url
    search_all_url = cur_url
    
    #数据库查询语句生成和部分不依赖数据库的数据生成
    enums = [['type','type'],['prince','min_price'],['direct','farm__direct'],['age','age'],['epidemic','epidemic_period']]
    for enum in enums:
        if enum[0] in re.GET:
            url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            search_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            if enum[0] != 'type':
                type_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            else:
                typekey = re.REQUEST.get(enum[0])
                
            if enum[0] != 'direct':
                direct_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            else:
                directkey = re.REQUEST.get(enum[0])
            
            if enum[0] != 'epidemic':
                epidemic_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            else:
                epidemickey = re.REQUEST.get(enum[0])
                
            if enum[0] != 'prince' and enum[0] != 'age':
                kwargs[enum[1]] = re.REQUEST.get(enum[0])
                prince_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
                age_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            elif enum[0] == 'prince':
                price = string.atoi(re.REQUEST.get(enum[0]))
                if price > len(princes):
                    price = len(princes)
                elif price < 1:
                    price = 1
                #kwargs[enum[1] + '__gte'] = princes[price - 1]['b']
                #kwargs[enum[1] + '__lte'] = princes[price - 1]['c']
                princekey = price.__str__()
                age_all_url += '%s=%d&' % (enum[0], price)
            elif enum[0] == 'age':
                age = string.atoi(re.REQUEST.get(enum[0]))
                if age > len(ages):
                    age = len(ages)
                elif age < 1:
                    age = 1
                kwargs[enum[1] + '__gte'] = ages[age - 1]['b']
                kwargs[enum[1] + '__lte'] = ages[age - 1]['c']
                agekey = age.__str__()
                prince_all_url += '%s=%d&' % (enum[0], age)
    
    urls = {}
    urls['url'] = url
    urls['type_all_url'] = type_all_url
    urls['prince_all_url'] = prince_all_url
    urls['direct_all_url'] = direct_all_url
    urls['epidemic_all_url'] = epidemic_all_url
    urls['age_all_url'] = age_all_url
    urls['search_all_url'] = search_all_url
    
    #查询数据库获取数据
    pets_imgs = []
    pets = nestofpet.objects.filter(**kwargs)
    if searchkey:
        pets = pets.filter(Q(farm__name__contains=searchkey)|Q(farm__detail_address__contains=searchkey))
    for pet_one in pets:
        try:
            petimg = nestofpet_img.objects.filter(nestofpet_id = pet_one,dele=False,img_usefor='buy_main')[0]
        except:
            petimg = None
        othor_pets = pet_one.pet_set.filter(dele=False)
        min_price = string.atoi(othor_pets.order_by('-price')[0].price)
        max_price = string.atoi(othor_pets.order_by('price')[0].price)
        if price != None:
            if (min_price < princes[price - 1]['b'] or min_price > princes[price - 1]['c'])\
            and (max_price < princes[price - 1]['b'] or max_price > princes[price - 1]['c'])\
            and (min_price > princes[price - 1]['b'] and max_price < princes[price - 1]['c']):
                continue
        pets_imgs.append({'pet':pet_one,'img':petimg,'min_price':min_price,'max_price':max_price})
    return {'pets_imgs':pets_imgs,'urls':urls,'types':types,'typekey':typekey,'princes':princes,
            'princekey':princekey,'directs':directs,'directkey':directkey,'searchkey':searchkey,'epidemics':epidemics,
            'epidemickey':epidemickey,'ages':ages,'agekey':agekey,'page':'buy'}

'''
函数功能：首页数据适配器
作者：胡怀勇
时间：2014-9-22
'''
def buy_detail_adapter(re):
    if 'petid' in re.GET:
        '''获取当前这窝宠物信息'''
        petid = string.atoi(re.REQUEST.get('petid'))
        try:
            nest_pet = nestofpet.objects.filter(id=petid,dele=False,sale_out=False)[0]
            curtype = nest_pet.type
        except:
            return False
        petimgs = nest_pet.nestofpet_img_set.filter(dele=False,img_usefor='narmol')
        if petimgs.count() == 0:
            petimg_first = None
        else:
            petimg_first = petimgs[0]
        allpets = nest_pet.pet_set.filter(dele=False).order_by('-price')
        price = {'min_prince':allpets.order_by('-price')[0].price,'max_prince':allpets.order_by('price')[0].price}
        price['min_price'] = allpets.order_by('-price')[0].price
        price['max_price'] = allpets.order_by('price')[0].price
        
        '''获取本养殖场的所有宠物信息'''
        farm_imgs = nest_pet.farm.pet_farm_img_set.filter(dele=False)[0:4]
        pets_img = []
        farm_pet_types = []
        farm_pets = nest_pet.farm.nestofpet_set.filter(dele=False,sale_out=False)
        for farm_pet in farm_pets:
            try:
                img = farm_pet.nestofpet_img_set.filter(dele=False,img_usefor='buy_main')[0]
            except:
                img = None
            othor_pets = nest_pet.pet_set.filter(dele=False)
            min_price = othor_pets.order_by('-price')[0].price
            max_price = othor_pets.order_by('price')[0].price
            count = othor_pets.count()
            if farm_pet.type not in farm_pet_types:
                farm_pet_types.append(farm_pet.type)
            pets_img.append({'pet':farm_pet,'img':img,'min_price':min_price,'max_price':max_price,'count':count})
        
        '''
                            以下部分是获取本页面推荐的内容
        '''
        recommendpets_img = []
        recommendpets = nestofpet.objects.filter(Q(type = nest_pet.type)|Q(color=nest_pet.color)|Q(farm__district=nest_pet.farm.district),dele=False,sale_out=False)
        recommendpets = recommendpets.exclude(id=nest_pet.id)
        for recommendpet in recommendpets:
            try:
                img = nestofpet_img.objects.filter(nestofpet_id = recommendpet,dele=False,img_usefor='buy_main')[0]
            except:
                img = None
            othor_pets = recommendpet.pet_set.filter(dele=False)
            min_price = othor_pets.order_by('-price')[0].price
            max_price = othor_pets.order_by('price')[0].price
            recommendpets_img.append({'pet':recommendpet,'img':img,'min_price':min_price,'max_price':max_price})
            
        return {'nestpet':nest_pet,'price':price,'nowimgs':petimgs[1:],'farmimgs':farm_imgs,'pets_img':pets_img,'curtype':curtype,
                'pet_types':farm_pet_types,'petimg_a':petimg_first,'recommendpets_img':recommendpets_img,'allpets':allpets,'page':'buy'}
        '''
    elif 'farmid' in re.GET:
        farmid = string.atoi(re.REQUEST.get('farmid'))
        try:
            if 'type' in re.GET:
                curtype = re.REQUEST.get('type')
                nestpets = nestofpet.objects.filter(farm=get_object_or_404(pet_farm,pk=farmid),type=curtype,dele=False,sale_out=False)
            else:
                nestpets = nestofpet.objects.filter(farm=get_object_or_404(pet_farm,pk=farmid),dele=False,sale_out=False)
            pets_imgs = []
            for nestpet in nestpets:
                try:
                    img = nestofpet_img.objects.filter(nestofpet_id=nestpet,dele=False)[0]
                    pets_imgs.append({'pet':nestpet,'img':img})
                except:
                    None
            return {'pets_imgs':pets_imgs}
        except:
            return False
        '''
    else:
        return False

def buy_attention_adapter(req):
    data = {"status": "error", "message": "error"}
    if 'petid' not in req.GET or 'name' not in req.GET or 'tel' not in req.GET:
        data['message'] = "信息不完整，可能系统有虫子，请联系我们，谢谢~！"
        return simplejson.dumps(data,ensure_ascii = False)
    petid = string.atoi(req.REQUEST.get('petid'))
    name = req.REQUEST.get('name')
    tel = req.REQUEST.get('tel')
    try:
        nestofpet.objects.get(id=petid,dele=False,sale_out=False)
    except:
        data['message'] = "实在抱歉，您想预定的宠物售罄了！"
        return simplejson.dumps(data,ensure_ascii = False)
    p = re.compile(r'1\d{10}')
    if not p.match(tel):
        p = re.compile(r'(\d{4}-|\d{3}-)?(\d{8}|\d{7})')
        if not p.match(tel):
            data['message'] = "您这电话号码不对哦，任谁都通过它联系不到您呢~！"
            return simplejson.dumps(data,ensure_ascii = False)
    p = re.compile(ur'^([\u4e00-\u9fa5]+|([a-zA-Z]+\s?)+)$')
    if not p.match(name):
        data['message'] = "您的名字~！"
        return simplejson.dumps(data,ensure_ascii = False)
    try:
        user =  attention_user(name=name,tel=tel)
        user.save()
        attention = nestofpet_attention(nestofpet_id=get_object_or_404(nestofpet,pk=petid),user=user)
        attention.save()
    except:
        data['message'] = "服务器内部错误，请反馈给我们，多谢亲！"
        return simplejson.dumps(data,ensure_ascii = False)
    sendTemplateSMS(tel,["chongwug","test1"])
    data = {"status": "success"}
    return simplejson.dumps(data,ensure_ascii = False)

from yuntongxun.CCPRestSDK import REST

accountSid= '8a48b55148fe48600149087c6c3105ae';

accountToken= '4ac0351d9f384db99983e8d4683f24af';

appId='aaf98f8948fe3e9c0149087cae01056e';

serverIP='sandboxapp.cloopen.com';

serverPort='8883';

softVersion='2013-12-26';

def sendTemplateSMS(to,datas,tempId=1):
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    rest.sendTemplateSMS(to,datas,tempId)