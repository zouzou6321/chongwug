# -*- coding: UTF-8 -*-
from back_manager.models import ad,pet_farm,pet_farm_img,pet,pet_img
import datetime,string
from django.db.models import Q
def buy_home_adapter(request):
    #前期只有一个城市：成都
    contry = "china"
    province = "四川"
    city = "成都"
    enum_farms = []
    
    #获取首页需要展示的广告信息
    ads = ad.objects.filter(Q(type__exact = 'nav_m'),Q(dele__exact = False),Q(start_time__lte = datetime.datetime.now),Q(end_time__gte = datetime.datetime.now)).order_by('prince')
    
    #目前是3个广告，需要考虑数据库中找不全可用广告的场景
    ads0 = False
    ads1 = False
    ads2 = False
    ads_count = ads.count()
    print(ads_count)
    if ads_count > 0:
        ads0 = ads[0]
    if ads_count > 1:
        ads1 = ads[1]
    if ads_count > 2:
        ads2 = ads[2]
    data = {'ads0':ads0,'ads1':ads1,'ads2':ads2}
    
    #获取养殖场信息，同时考虑信息获取不完整的情况，确保页面不崩溃
    city_farms = pet_farm.objects.filter(contry=contry,province=province,city=city)
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
    return data

def buy_main_adapter(re):
    url = '/buy/?'
    
    types = [u'泰迪',u'比熊',u'金毛',u'萨摩耶',u'哈士奇',u'拉布拉多',u'边牧',u'松狮',u'阿拉斯加',u'博美',u'巴哥',u'雪纳瑞',u'约克夏',u'德牧',u'古牧',u'比格',u'喜乐蒂',u'斗牛犬',u'杜宾',u'罗威纳',u'吉娃娃']
    princes = [{'a':'1','b':600,'c':1000},{'a':'2','b':1000,'c':1500},{'a':'3','b':1500,'c':2000},{'a':'4','b':2000,'c':2500},{'a':'5','b':2500,'c':1000000}]
    directs = [u'东',u'西',u'南',u'北',u'中']
    epidemics = [u'已种疫苗',u'可种疫苗',u'未种疫苗']
    ages = [{'a':'1','b':0,'c':3},{'a':'2','b':3,'c':5},{'a':'3','b':5,'c':12},{'a':'4','b':12,'c':100000}]
    
    typekey = None
    princekey = None
    directkey = None
    epidemickey = None
    agekey = None
    
    kwargs = {}
    kwargs['dele'] = False
    kwargs['sale_out'] = False
    
    type_all_url = url
    prince_all_url = url
    direct_all_url = url
    epidemic_all_url = url
    age_all_url = url
    
    enums = [['type','type'],['prince','price'],['direct','farm__direct'],['age','age'],['epidemic','epidemic_period']]
    for enum in enums:
        if enum[0] in re.GET:
            url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
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
                kwargs[enum[1] + '__gte'] = princes[string.atoi(re.REQUEST.get(enum[0])) - 1]['b']
                kwargs[enum[1] + '__lte'] = princes[string.atoi(re.REQUEST.get(enum[0])) - 1]['c']
                princekey = re.REQUEST.get(enum[0])
                age_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
            elif enum[0] == 'age':
                kwargs[enum[1] + '__gte'] = ages[string.atoi(re.REQUEST.get(enum[0])) - 1]['b']
                kwargs[enum[1] + '__lte'] = ages[string.atoi(re.REQUEST.get(enum[0])) - 1]['c']
                agekey = re.REQUEST.get(enum[0])
                prince_all_url += enum[0] + '=' + re.REQUEST.get(enum[0]) + '&'
    
    urls = {}
    urls['url'] = url
    urls['type_all_url'] = type_all_url
    urls['prince_all_url'] = prince_all_url
    urls['direct_all_url'] = direct_all_url
    urls['epidemic_all_url'] = epidemic_all_url
    urls['age_all_url'] = age_all_url
    
    pets_imgs = []
    pets = pet.objects.filter(**kwargs)
    for pet_one in pets:
        try:
            petimg = pet_img.objects.filter(pet_id = pet_one,dele=False,img_usefor='buy_main')[0]
            pets_imgs.append({'pet':pet_one,'img':petimg})
        except:
            None
    return {'pets_imgs':pets_imgs,'urls':urls,'types':types,'typekey':typekey,'princes':princes,
            'princekey':princekey,'directs':directs,'directkey':directkey,'epidemics':epidemics,
            'epidemickey':epidemickey,'ages':ages,'agekey':agekey}