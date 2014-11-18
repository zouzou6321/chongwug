# -*- coding: UTF-8 -*-
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector
import MySQLdb,os,datetime,string,time
from webspider.items import WebspiderItem  
import codecs

class webspiderSpider(Spider):  
    """webspiderSpider"""  
    myfile = codecs.open('58.txt', 'wb', encoding='utf-8') 
    name = "58"  
    download_delay = 1
    allowed_domains = ["cd.58.com"]  
    start_urls = [  
        #"http://cd.58.com/wuhou/hezu/",
        #"http://cd.58.com/jinjiang/hezu/",
        #"http://cd.58.com/chenghua/hezu/",
        #"http://cd.58.com/jinniu/hezu/",
        #"http://cd.58.com/qingyangqu/hezu/",
        #"http://cd.58.com/xindu/hezu/",
        #"http://cd.58.com/pixian/hezu/",
        #"http://cd.58.com/wenjiang/hezu/",
        #"http://cd.58.com/longquanyi/hezu/",
        #"http://cd.58.com/shuangliu/hezu/",
        #"http://cd.58.com/cdgaoxin/hezu/",
        "http://cd.58.com/gaoxinxiqu/hezu/",
        #"http://www.dog126.com/doginfo_136.html"
    ]
    def parse(self, response):  
  
        sel = Selector(response)
        #for site in sites:  
        item = WebspiderItem()
        contents = sel.xpath('//div[@class="relative"]//dl//dd//div[@class="subarea"]//a').extract()
        item['area'] = ''
        count = 0
        for content in contents:
            print content
            contentsel = Selector(text=content)
            localcontens = contentsel.xpath("string(//a)").extract()
            print localcontens[0]
            item['area'] += u"{'name':'%s','index':%d}," % (localcontens[0], count)
            count += 1

        #conn.close()
        yield item