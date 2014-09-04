# -*- coding: UTF-8 -*-
from back_manager.models import ad,pet_farm,pet_farm_img
import datetime
from django.db.models import Q
def buy_home_adapter(request):
    #前期只有一个城市：成都
    contry = "china"
    province = "四川"
    city = "成都"
    enum_farms = []
    
    #获取首页需要展示的广告信息
    ads = ad.objects.get(Q(type__exact = 'nav_m'),Q(dele__exact = False),Q(start_time__lte = datetime.datetime.now),Q(end_time__gte = datetime.datetime.now)).order_by('prince')
    
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