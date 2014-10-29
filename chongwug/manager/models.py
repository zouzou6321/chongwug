# -*- coding: UTF-8 -*-
from django.db import models
import datetime
# Create your models here.
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

class tmppic_monitor(models.Model):
    fname = models.TextField()
    monitor_time= models.DateTimeField(default=datetime.datetime.now)
    dele = models.BooleanField(default=False)

class dog123(models.Model):
    url = models.TextField()
    name = models.TextField()
    ename = models.TextField()
    where = models.TextField()
    age = models.TextField()
    nickname = models.TextField()
    maleheight = models.TextField()
    fmaleheight = models.TextField()
    color = models.TextField(blank=True, null=True)
    siyang = models.TextField(blank=True, null=True)
    jiage = models.TextField(blank=True, null=True)
    gongneng = models.TextField(blank=True, null=True)
    tizhong = models.IntegerField(blank=True, null=True)
    zhishang = models.IntegerField(blank=True, null=True)
    huopo = models.IntegerField(blank=True, null=True)
    score = models.IntegerField()
    nianren = models.IntegerField()
    xijiao = models.IntegerField()
    diaomao = models.IntegerField()
    tiwei = models.IntegerField()
    meirong_hz = models.IntegerField()
    kidfred = models.IntegerField()
    otherfred = models.IntegerField()
    animfred = models.IntegerField()
    yundong = models.IntegerField()
    xulian = models.IntegerField()
    koushui = models.IntegerField()
    naihan = models.IntegerField()
    naire = models.IntegerField()
    cityfred = models.IntegerField()
    imgurl = models.TextField()
    tixing = models.TextField()

class pclady(models.Model):
    url = models.TextField()
    name = models.TextField()
    imgurl = models.TextField()
    title = models.TextField()
    content = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now)
    contentfrom = models.TextField(default='chongwug.com')