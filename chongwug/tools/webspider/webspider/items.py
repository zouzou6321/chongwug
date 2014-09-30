# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WebspiderItem(Item):
    url = Field()
    name = Field()
    ename = Field()
    where = Field()
    age = Field()
    nickname = Field()
    maleheight = Field()
    fmaleheight = Field()
    score = Field()
    nianren = Field()
    xijiao = Field()
    diaomao = Field()
    tiwei = Field()
    meirong_hz = Field()
    kidfred = Field()
    otherfred = Field()
    animfred = Field()
    yundong = Field()
    xulian = Field()
    koushui = Field()
    naihan = Field()
    naire = Field()
    cityfred = Field()
