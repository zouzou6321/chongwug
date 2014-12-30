# -*- coding: UTF-8 -*-
from django.db import models
import datetime
from petfarm.models import nestofpet,pet_farm
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    nickname = models.TextField(blank=True, null=True)
    realname = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    #身份证号码
    id_num = models.TextField(blank=True, null=True)
    id_card = models.URLField(blank=True, null=True)
    #0是未验证,1是验证通过,2是未通过,3是不需要验证的非养殖场用户
    verify = models.IntegerField(default=0)
    pwd = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    regtime = models.DateTimeField(default=datetime.datetime.now)
    #用户类型分为三种：0是普通消费者，1是养殖场用户，2是其他用户
    type = models.IntegerField(default=0)
    petfarm = models.ForeignKey(pet_farm,blank=True, null=True)
    auth_user = models.ForeignKey(User)
    location = models.TextField(blank=True, null=True)
    dele = models.BooleanField(default=False)

class nestofpet_attention(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now)
    nestofpet_id = models.ForeignKey(nestofpet)
    user = models.ForeignKey(user)
    appoint_time = models.DateTimeField()
    trans = models.TextField()
    #attention_type：表示关注、预约、预定
    attention_type = models.TextField(default=0)
    dele = models.BooleanField(default=False)

class smssend_countor(models.Model):
    count = models.IntegerField(default=0)
    nexttime = models.DateTimeField(default=datetime.datetime.now)
    attention = models.ForeignKey(nestofpet_attention,blank=True, null=True)
    user = models.ForeignKey(user,blank=True, null=True)
    dele = models.BooleanField(default=False)

class buyselectinfo(models.Model):
    directkey=models.TextField()
    typekey=models.TextField()
    princekey=models.IntegerField()
    agekey=models.IntegerField()
    epidemickey=models.TextField()
    searchkey=models.TextField()
    curpage=models.IntegerField()
    dele = models.BooleanField(default=False)

class appointorders(models.Model):
    orderno = models.TextField(blank=True, null=True)
    attention = models.ForeignKey(nestofpet_attention)
    status = models.TextField(default='')
    time = models.DateTimeField(default=datetime.datetime.now)
    dele = models.BooleanField(default=False)

class pviptongji(models.Model):
    ip = models.CharField(max_length=20)
    pageuri = models.TextField()
    browser = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now)

class uvpviptongji(models.Model):
    ip = models.CharField(max_length=20)
    uv = models.TextField(blank=True, null=True)
    pageuri = models.TextField()
    browser = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now)

class adclicktongji(models.Model):
    ip = models.CharField(max_length=20)
    tarurl = models.TextField()
    browser = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now)