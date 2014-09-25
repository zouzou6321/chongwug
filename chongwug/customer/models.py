# -*- coding: UTF-8 -*-
from django.db import models
import datetime
from petfarm.models import nestofpet,pet_farm
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    nickname = models.TextField()
    realname = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    id_num = models.TextField(blank=True, null=True)
    pwd = models.TextField()
    desc = models.TextField(blank=True, null=True)
    regtime = models.DateTimeField(default=datetime.datetime.now)
    #用户类型分为三种：0是普通消费者，1是养殖场用户，2是其他用户
    type = models.IntegerField(default=0)
    petfarm = models.ForeignKey(pet_farm,blank=True, null=True)
    auth_user = models.ForeignKey(User)
    dele = models.BooleanField(default=False)

class attention_user(models.Model):
    name = models.TextField()
    tel = models.TextField()
    dele = models.BooleanField(default=False)

class nestofpet_attention(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now)
    nestofpet_id = models.ForeignKey(nestofpet)
    user = models.ForeignKey(attention_user)
    #attention_type：表示关注、预约、预定
    attention_type = models.TextField(default=0)
    dele = models.BooleanField(default=False)