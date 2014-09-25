# -*- coding: UTF-8 -*-
from django.db import models

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