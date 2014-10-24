# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WebspiderItem(Item):
    url = Field()
    name = Field()
    content = Field()
    title = Field()
    image_urls = Field()
    image_paths = Field()
    imgpath = Field()
