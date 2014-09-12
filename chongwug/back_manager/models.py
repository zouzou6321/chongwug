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
    min_prince = models.FloatField()
    #添加时间
    start_time = models.TimeField(default=datetime.datetime.now)
    #删除时间
    end_time = models.TimeField(blank=True, null=True)
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

class pet(models.Model):
    farm = models.ForeignKey(pet_farm,blank=True, null=True)
    mam_id = models.ForeignKey(pet_mam,blank=True, null=True)
    dad_id = models.ForeignKey(pet_dad,blank=True, null=True)
    color = models.TextField()
    #宠物上架月龄
    age = models.IntegerField()
    #防疫阶段
    epidemic_period = models.TextField()
    #宠物品种
    type = models.TextField()
    txt_desc = models.TextField()
    #上架时间
    start_time = models.DateTimeField(default=datetime.datetime.now)
    #卖出时间
    sale_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField()
    sale_out = models.BooleanField(default=False)
    dele = models.BooleanField(default=False)

class pet_attention(models.Model):
    time = models.TimeField(default=datetime.datetime.now)
    pet_id = models.ForeignKey(pet)
    #attention_type：表示关注、预约、预定
    attention_type = models.TextField(default=0)
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

class pet_mam_img(models.Model):
    pet_mam_id = models.ForeignKey(pet_mam)
    img_url = models.URLField()
    img_with = models.IntegerField()
    img_height = models.IntegerField()
    img_type = models.TextField()
    #图片用途
    img_usefor = models.TextField()
    dele = models.BooleanField(default=False)
    
class pet_dad_img(models.Model):
    pet_dad_id = models.ForeignKey(pet_dad)
    img_url = models.URLField()
    img_with = models.IntegerField()
    img_height = models.IntegerField()
    img_type = models.TextField()
    #图片用途
    img_usefor = models.TextField()
    dele = models.BooleanField(default=False)

class pet_img(models.Model):
    pet_id = models.ForeignKey(pet)
    img_url = models.URLField()
    img_with = models.IntegerField()
    img_height = models.IntegerField()
    img_type = models.TextField()
    #图片用途
    img_usefor = models.TextField()
    dele = models.BooleanField(default=False)

#ad:广告专用
class ad(models.Model):
    #type：标志是哪个模块的广告
    type = models.TextField()
    #默认一个广告就是一张图片，方便前台布局，每一种type的广告图片必须按照要求提交
    img_url = models.URLField()
    #广告点击后的跳转地址
    tar_url = models.URLField(blank=True, null=True)
    #广告价格
    prince = models.IntegerField()
    #当前是否展示
    current_show = models.BooleanField(default=False)
    #广告需要启动展示的时间
    start_time = models.DateTimeField()
    #广告结束展示的时间
    end_time = models.DateTimeField()
    dele = models.BooleanField(default=False)
    
#管理员帐号，不一定每个都有，主要是负责数据编辑的人员使用
class manage(models.Model):
    name = models.TextField()
    passwd = models.TextField()
    #作业类型
    type = models.TextField()
    permission_score = models.IntegerField()
    dele = models.BooleanField(default=False)