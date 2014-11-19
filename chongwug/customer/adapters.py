# -*- coding: UTF-8 -*-
'''
文件功能：针对购宠用户涉及的页面，根据展示的数据需要，整理出格式化的数据返回
'''
from manager.models import ad,dog123,pclady,supplies
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img,pet
from customer.models import user,nestofpet_attention,smssend_countor,buyselectinfo
from django.db.models import Q
from django.shortcuts import get_object_or_404
from chongwug.config import __onepageofdata__,__petfeaturescore,__farmpictypes,__transpay,__servpay,__appointtime,__addresses,__petpictypes,__pettypes,__prices,__ages,__epidemics,__directs,__regular_expression_username,__regular_expression_telnum,__regular_expression_chinatelnum
import datetime,string,re,json
from chongwug.commom import __errorcode__,sendSMS
from django.contrib.auth.models import User
from django.contrib import auth
import traceback

def is_wap(request):
    #if request.META['HTTP_ACCEPT'].find('wap') == -1:
        #return False
    return False

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
    directs = __directs
    direct_farms = []
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
            pet = nestofpet.objects.filter(farm=city_farm,dele=False,sale_out=False).order_by('min_price')[0]
            city_farm.min_prince = pet.min_price
            city_farm.save()
        except:
            None
    for direct in directs:
        tmp_farm = city_farms.filter(direct=direct,dele=False).order_by('-manage_score')
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
        direct_farms.append({'direct':direct,'farm':tmp_farm,'pic':tmp_farm_img})
    data['direct_farms'] = direct_farms
    data['page'] = 'home'
    return data

'''
函数功能：购宠页面数据适配器，
作者：胡怀勇
时间：2014-9-22
'''
def buy_main_adapter(request,directkey='all',typekey='all',princekey=0,agekey=0,epidemickey='all',searchkey='all',curpage=1):
    #筛选条件
    types = __pettypes
    princes = __prices
    directs = __directs
    epidemics = __epidemics
    ages = __ages
    if 'key' in request.GET:
        searchkey = request.REQUEST.get('key')
    #数据库查询语句整合
    kwargs = {}
    kwargs['dele'] = False
    kwargs['sale_out'] = False
    if directkey != 'all':
        kwargs['farm__direct'] = directkey
    if typekey != 'all':
        kwargs['type'] = typekey
    if agekey != 0:
        kwargs['age__gte'] = ages[agekey - 1]['b']
        kwargs['age__lte'] = ages[agekey - 1]['c']
    
    #查询数据库获取数据
    pets_imgs = []
    pets = nestofpet.objects.filter(**kwargs)
    if searchkey != 'all':
        pets = pets.filter(Q(farm__name__contains=searchkey)|Q(farm__detail_address__contains=searchkey))
    for pet_one in pets:
        if epidemickey != 'all' and pet_one.pet_set.filter(epidemic_period=epidemickey).count() <= 0:
            continue;
        try:
            petimg = nestofpet_img.objects.filter(nestofpet_id = pet_one,dele=False,img_usefor=__petpictypes[0][1])[0]
        except:
            petimg = None
        othor_pets = pet_one.pet_set.filter(dele=False)
        min_price = othor_pets.order_by('price')[0].price
        max_price = othor_pets.order_by('-price')[0].price
        if princekey > 0:
            if (max_price < princes[princekey - 1]['b'] or min_price > princes[princekey - 1]['c']):
                continue
        for epidemic in __epidemics:
            if othor_pets.filter(epidemic_period = epidemic).count() > 0:
                epidemic_period = epidemic
                break
        pets_imgs.append({'pet':pet_one,'img':petimg,'min_price':min_price,'max_price':max_price,'count':othor_pets.count(),'epidemic':epidemic_period})
    selectinfo = buyselectinfo(directkey=directkey,typekey=typekey,princekey=princekey,agekey=agekey,epidemickey=epidemickey,searchkey=searchkey,curpage=curpage)
    selectinfo.save()
    #分页实现
    startpos = (curpage - 1) * __onepageofdata__  
    endpos = startpos + __onepageofdata__  
    petscount = len(pets_imgs)
    pets_imgs = pets_imgs[startpos:endpos]  
    pages = []
    allPostCounts = petscount
    allpage = allPostCounts / __onepageofdata__  
    remainPost = allPostCounts % __onepageofdata__  
    if remainPost > 0:  
        allpage += 1
    i = 0
    while i < allpage:
        i += 1
        pages.append(i)
    return {'pets_imgs':pets_imgs,'urls': '/buy/','types':types,'typekey':typekey,'princes':princes,'princekey':str(princekey),
            'directs':directs,'directkey':directkey,'searchkey':searchkey,'epidemics':epidemics,'epidemickey':epidemickey,
            'ages':ages,'agekey':str(agekey),'curpage':curpage,'pageup':curpage-1,'pagedown':curpage+1,'pages':pages,'allpage':allpage,'page':'buy'}

'''
函数功能：首页数据适配器
作者：胡怀勇
时间：2014-9-22
'''
def buy_detail_adapter(re,petid):
    if 'range' in re.GET:
        addresses = __addresses[string.atoi(re.REQUEST.get('range'))]['sublist'][string.atoi(re.REQUEST.get('province'))]
        if 'city' in re.GET:
            addresses = addresses['sublist'][string.atoi(re.REQUEST.get('city'))]
        if 'district' in re.GET:
            addresses = addresses['sublist'][string.atoi(re.REQUEST.get('district'))]
        arr = []
        for address in addresses['sublist']:
            arr.append({'id': address['index'], 'name': address['name']})
        return {'locations': arr}
    elif petid != -1:
        '''获取当前这窝宠物信息'''
        try:
            nest_pet = nestofpet.objects.filter(id=petid,dele=False,sale_out=False)[0]
            curtype = nest_pet.type
        except:
            return False
        petimgs = nest_pet.nestofpet_img_set.filter(dele=False)
        if petimgs.count() == 0:
            petimg_first = None
        else:
            petimg_first = petimgs[0]
        allpets = nest_pet.pet_set.filter(dele=False).order_by('-price')
        price = {'min_prince':allpets.order_by('price')[0].price,'max_prince':allpets.order_by('-price')[0].price}
        price['min_price'] = allpets.order_by('price')[0].price
        price['max_price'] = allpets.order_by('-price')[0].price
        
        '''获取本养殖场的所有宠物信息'''
        farm_imgs = nest_pet.farm.pet_farm_img_set.filter(dele=False)[0:4]
        pets_img = []
        farm_pet_types = []
        farm_pets = nest_pet.farm.nestofpet_set.filter(dele=False,sale_out=False)
        for farm_pet in farm_pets:
            try:
                img = farm_pet.nestofpet_img_set.filter(dele=False,img_usefor=__petpictypes[0][1])[0]
            except:
                img = None
            othor_pets = farm_pet.pet_set.filter(dele=False)
            min_price = othor_pets.order_by('price')[0].price
            max_price = othor_pets.order_by('-price')[0].price
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
                img = nestofpet_img.objects.filter(nestofpet_id = recommendpet,dele=False,img_usefor=__petpictypes[0][1])[0]
            except:
                img = None
            othor_pets = recommendpet.pet_set.filter(dele=False)
            min_price = othor_pets.order_by('price')[0].price
            max_price = othor_pets.order_by('-price')[0].price
            recommendpets_img.append({'pet':recommendpet,'img':img,'min_price':min_price,'max_price':max_price})
        cuser = None
        if re.user.is_authenticated():
            cuser = user.objects.get(auth_user=auth.get_user(re),dele = False)
        appointdays = []
        now = datetime.datetime.now()
        days = 0
        weeks = [u'周一',u'周二',u'周三',u'周四',u'周五',u'周六',u'周日']
        while days < 14:
            days += 1
            delta = datetime.timedelta(days=days)
            n_days = now + delta
            appointdays.append({'day':n_days.day,'year':n_days.year,'mouth':n_days.month,'week':weeks[n_days.weekday()],'selectable':{'time1':True,'time2':True}})
        return {'cuser':cuser,'appointtime':__appointtime,'appointdays':appointdays,'addresses':__addresses,'nestpet':nest_pet,'price':price,'nowimgs':petimgs[1:],'farmimgs':farm_imgs,'pets_img':pets_img,'curtype':curtype,
                'pet_types':farm_pet_types,'petimg_a':petimg_first,'recommendpets_img':recommendpets_img,'allpets':allpets,'page':'buy','urls':'/buy/detail/'}
    else:
        return False

def attention_sendsms(req):
    if not req.user.is_authenticated():
            return __errorcode__(1)
    attention = nestofpet_attention.objects.get(id=req.REQUEST.get('id'),attention_type=1,dele=False)
    cur_user = user.objects.get(auth_user=auth.get_user(req),dele=False)
    if attention.user.id != cur_user.id:
        return __errorcode__(2)
    smsusers = smssend_countor.objects.filter(user=cur_user,dele=False)
    if smsusers.count() > 0:
        smsuser = smsusers[0]
        smsattentions = smssend_countor.objects.filter(attention=attention,dele=False)
        if smsattentions.count() > 0:
            smsattention = smsattentions[0]
        else:
            smsattention = smssend_countor(attention=attention)
            smsattention.save()
    else:
        smsuser = smssend_countor(user=cur_user)
        smsuser.save()
        smsattention = smssend_countor(attention=attention)
        smsattention.save()
    now = datetime.datetime.now()
    if (now - smsuser.nexttime).days >= 1:
        smsuser.nexttime = now
        smsuser.count = 0
    if (now - smsattention.nexttime).days >= 1:
        smsattention.nexttime = now
        smsattention.count = 0

    smsuser.count = smsuser.count + 1
    smsattention.count = smsattention.count + 1
    
    if smsuser.count > 9 or smsattention.count > 3:
        return __errorcode__(23)
    smsuser.save()
    smsattention.save()
    location = get_waitpoint(attention.nestofpet_id.farm.district)
    content = u"%s您好，您的预约信息如下：预约看犬时间为：%s年%s月%s日 %s点%s分,等待接送地点为：%s,预约看犬犬舍为：%s,预约看犬犬种为：%s。祝您就此遇见心仪的爱犬！" % (attention.user.nickname, attention.appoint_time.year, attention.appoint_time.month, attention.appoint_time.day, 
               attention.appoint_time.hour, attention.appoint_time.minute, location.decode('utf8'), attention.nestofpet_id.farm.name, attention.nestofpet_id.type)
    sendSMS(attention.user.tel,content)
    return __errorcode__(0)

def buy_attention_sure(req):
    if 'id' not in req.GET:
        return __errorcode__(7)
    if not req.user.is_authenticated():
            return __errorcode__(1)
    attention = nestofpet_attention.objects.get(id=req.REQUEST.get('id'),attention_type=0,dele=False)
    cur_user = user.objects.get(auth_user=auth.get_user(req),dele=False)
    if attention.user.id != cur_user.id:
        return __errorcode__(2)
    attention.attention_type = 1
    attention.save()
    farmuser = user.objects.get(petfarm=attention.nestofpet_id.farm,dele=False,type=1)
    pets = pet.objects.filter(nestofpet=attention.nestofpet_id,dele=False)
    min_price = pets.order_by('price')[0].price
    max_price = pets.order_by('-price')[0].price
    content = u"【宠物购】接生意了！ 订单信息：%s将于%s年%s月%s日%s时%s分前往贵犬舍挑选%s犬，他/她看中的窝号为%s，价格区间为%s-%s。 稍后宠物购工作人员将会电话与您确认，请保持您所预留的手机/电话畅通！" % (attention.user.nickname, attention.appoint_time.year, attention.appoint_time.month, attention.appoint_time.day,
                attention.appoint_time.hour, attention.appoint_time.minute, attention.nestofpet_id.type, attention.nestofpet_id.num,min_price,max_price)
    sendSMS(farmuser.tel,content)
    return __errorcode__(0)

def get_waitpoint(_district):
    for addresse in __addresses:
        for province in addresse['sublist']:
            for city in province['sublist']:
                for district in city['sublist']:
                    if _district == district['name']:
                        return district['waitpoint']
def buy_attention_adapter(req):
    if ('id' or 'name' or 'phone' or 'location' or 'time' or 'transportation') not in req.POST:
        return __errorcode__(7)
    petid = string.atoi(req.POST['id'])
    name = req.POST['name']
    tel = req.POST['phone']
    transport = req.POST['transportation']
    
    try:
        cupet = nestofpet.objects.get(id=petid,dele=False,sale_out=False)
    except:
        return __errorcode__(8)
    p = re.compile(__regular_expression_username)
    if not p.match(name):
        return __errorcode__(10)
    p = re.compile(__regular_expression_chinatelnum)
    if not p.match(tel):
        return __errorcode__(9)
    try:
        location = json.loads(req.POST['location'])
        province = __addresses[location['range']]['sublist'][location['province']]
        city = province['sublist'][location['city']]
        district = city['sublist'][location['district']]
        street = district['sublist'][location['street']]
        waitpoint = get_waitpoint(cupet.farm.district)
    except:
        return __errorcode__(11)
    try:
        appoint_time = datetime.datetime.strptime(req.POST['time'], u"%Y-%m-%d %H:%M")
    except:
        return __errorcode__(12)
    
    if transport == 'lift':
        totalpay = __transpay + __servpay
    else:
        totalpay = __transpay
    attentions = nestofpet_attention.objects.filter(dele=False,nestofpet_id=cupet)
    
    if req.user.is_authenticated() and auth.get_user(req).username != tel:
        auth.logout(req)
    if not req.user.is_authenticated():
        auth_user = None
        try:
            auth_user = User.objects.create_user(username=tel,email='',password='123456')
            curuser =  user(nickname=name,tel=tel,location=('%s-%s-%s-%s' % (province['name'],city['name'],district['name'],street['name'])),auth_user=auth_user,type=0)
            curuser.save()
        except:
            if auth_user:
                auth_user.delete()
        '''后续注册登录功能完成后，必须修改此处,目前只需要电话号码，不需要密码即可登录,如果用户已经存在，直接登录'''
        authuser = auth.authenticate(username=tel, password='123456')
        if authuser is not None and authuser.is_active:
            # Correct password, and the user is marked "active"
            auth.login(req, authuser)
        else:
            return __errorcode__(1)
    curuser = user.objects.get(auth_user=auth.get_user(req),dele=False)
    curuser.location=('%s-%s-%s-%s' % (province['name'],city['name'],district['name'],street['name']))
    curuser.save()
    
    curattentions = nestofpet_attention.objects.filter(nestofpet_id=cupet,user=curuser,attention_type=0,dele=False)
    if curattentions.count() == 0:
        curattentions = nestofpet_attention.objects.filter(nestofpet_id=cupet,user=curuser,dele=False)
        if curattentions.count() > 0:
            return __errorcode__(24)
        attention = nestofpet_attention(nestofpet_id=cupet,user=curuser,appoint_time=appoint_time,trans=transport)
        attention.save()
        id = attention.id
    else:
        curattentions[0].appoint_time = appoint_time
        curattentions[0].trans = transport
        curattentions[0].save()
        id = curattentions[0].id
    return __errorcode__(0,{'id':id,'count':attentions.count(),'ordernum':'XL%d' % attentions.count(),'waittime':req.POST['time'],
                            'waitpoint':waitpoint,'pay':totalpay,'farm':('%s-%s' % (cupet.farm.city, cupet.farm.district))})

def get_knowledge_bringup(request):
    page = 0
    if 'page' in request.GET:
        page = string.atoi(request.REQUEST.get('page'))
    return pclady.objects.all().order_by('id')[(page*6):(page*6 + 6)]
def get_knowledge_buy(request):
    if 'id' in request.GET:

        knowledge = dog123.objects.get(id=string.atoi(request.REQUEST.get('id')))
        return {'name':knowledge.name,'ename':knowledge.name,'where':knowledge.where,'age': knowledge.age,'nickname':knowledge.nickname,
                'maleheight':knowledge.maleheight,'fmaleheight':knowledge.fmaleheight,'color':knowledge.color,'siyang':knowledge.siyang,
                'jiage':knowledge.jiage,'gongneng':knowledge.gongneng,'tizhong':knowledge.tizhong,'zhishang':knowledge.zhishang,
                'huopo':knowledge.huopo,'score':knowledge.score,'nianren':knowledge.nianren,
                'xijiao':knowledge.xijiao,'diaomao':knowledge.diaomao,'tiwei':knowledge.tiwei,'meirong_hz':knowledge.meirong_hz,
                'kidfred':knowledge.kidfred,'otherfred':knowledge.otherfred,'animfred':knowledge.animfred,'yundong':knowledge.yundong,
                'xulian':knowledge.xulian,'koushui':knowledge.xulian,'naihan':knowledge.naihan,'naire':knowledge.naire,
                'cityfred':knowledge.cityfred,'imgurl':knowledge.imgurl}

    elif 'filter' in request.GET:
        idlist = []
        kwargs = {}
        args = ()
        enums = [['key','name'],['key','nickname'],['key','ename'],['youshan','kidfred'],['tixing','tixing'],['meirong_hz','meirong_hz'],['xulian','xulian'],
                 ['diaomao','diaomao'],['xijiao','xijiao'],['yundong','yundong'],['koushui','koushui']]
        for enum in enums:
            if enum[0] in request.GET and request.REQUEST.get(enum[0]) != '':
                if 'tixing' == enum[0]:
                    kwargs[enum[1]] = request.REQUEST.get(enum[0])
                elif 'key' == enum[0]:
                    key = request.REQUEST.get(enum[0])
                    args = Q( name__icontains = key )|Q( nickname__icontains = key )|Q( ename__icontains = key )
                else:
                    kwargs[enum[1] + '__lte'] = __petfeaturescore[string.atoi(request.REQUEST.get(enum[0])) - 1]
                    if string.atoi(request.REQUEST.get(enum[0])) >= 2:
                        kwargs[enum[1] + '__gt'] = __petfeaturescore[string.atoi(request.REQUEST.get(enum[0])) - 2]
        if args == ():
            dogsinfo = dog123.objects.filter(**kwargs)
        else:
            dogsinfo = dog123.objects.filter(args,**kwargs)
        for doginfo in dogsinfo:
            idlist.append(doginfo.id)
        return {'idlist':idlist}
    else:
        return dog123.objects.all()

def get_supplies():
    return supplies.objects.filter(dele=False)