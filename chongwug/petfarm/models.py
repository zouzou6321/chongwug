# -*- coding: UTF-8 -*-
from django.db import models
import datetime

# Create your models here.
class pet_farm(models.Model):
    name = models.TextField()
    desc = models.TextField(blank=True, null=True)
    contry = models.TextField(default='china')
    province = models.TextField()
    city = models.TextField()
    district = models.TextField()
    #direct代指宠物养殖场相对city的方向位置
    direct = models.TextField()
    detail_address = models.TextField()
    sale_count = models.IntegerField(default=0)
    sale_score = models.FloatField(default=0)
    min_prince = models.IntegerField()
    #添加时间
    start_time = models.DateTimeField(default=datetime.datetime.now)
    #删除时间
    end_time = models.DateTimeField(blank=True, null=True)
    #manage_score：系统赋予的积分，用来限制养殖场卖家权限，小于等于0时，卖家被拉黑
    manage_score = models.FloatField(default=1.0)
    dele = models.BooleanField(default=False)
    
class pet_mam(models.Model):
    type = models.TextField()
    age = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    alive = models.BooleanField(default=True)
    dele = models.BooleanField(default=False)

class pet_dad(models.Model):
    type = models.TextField()
    age = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    alive = models.BooleanField(default=True)
    dele = models.BooleanField(default=False)

class nestofpet(models.Model):
    farm = models.ForeignKey(pet_farm,blank=True, null=True)
    mam_id = models.ForeignKey(pet_mam,blank=True, null=True)
    dad_id = models.ForeignKey(pet_dad,blank=True, null=True)
    num = models.TextField(blank=True, null=True)
    color = models.TextField()
    #宠物上架月龄
    age = models.IntegerField()
    #宠物品种
    type = models.TextField()
    #一句话介绍
    short_desc = models.TextField(max_length=20)
    #详细介绍
    txt_desc = models.TextField(blank=True, null=True)
    #上架时间
    start_time = models.DateTimeField(default=datetime.datetime.now)
    sale_out = models.BooleanField(default=False)
    dele = models.BooleanField(default=False)

class pet(models.Model):
    nestofpet = models.ForeignKey(nestofpet)
    #详情页展示的序号:A/B/C/D...
    index = models.TextField()
    color = models.TextField()
    epidemic_period = models.TextField()
    price = models.IntegerField()
    sex = models.TextField()
    sale_out = models.BooleanField(default=False)
    dele = models.BooleanField(default=False)

class pet_farm_img(models.Model):
    pet_farm_id = models.ForeignKey(pet_farm)
    img_url = models.URLField()
    img_with = models.IntegerField()
    img_height = models.IntegerField()
    #img_type:jpg/png/...
    img_type = models.TextField()
    #图片用途
    img_usefor = models.TextField()
    dele = models.BooleanField(default=False)

class nestofpet_img(models.Model):
    nestofpet_id = models.ForeignKey(nestofpet)
    img_url = models.URLField()
    img_with = models.IntegerField()
    img_height = models.IntegerField()
    img_type = models.TextField()
    #图片用途
    img_usefor = models.TextField()
    dele = models.BooleanField(default=False)