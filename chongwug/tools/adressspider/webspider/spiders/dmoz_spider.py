# -*- coding: UTF-8 -*-
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector
import MySQLdb,os,datetime,string,time
from webspider.items import WebspiderItem
from webspider import settings
import time 
import codecs
class webspiderSpider(Spider):  
    """webspiderSpider"""  
    myfile = codecs.open('58.txt', 'wb', encoding='utf-8') 
    name = "58"  
    download_delay = 4
    allowed_domains = ["58.com"]  
    start_urls = [  
        "http://www.58.com/hezu/changecity/",
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
        #"http://cd.58.com/gaoxinxiqu/hezu/",
        #"http://www.dog126.com/doginfo_136.html"
    ]
    data = []
    citystmp = []
    distictstmp = []
    useragents = [
                  'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/18.0.1084.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/18.0.1084.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/17.0.1084.54 Safari/536.5',
                  'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/18.0.1085.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/18.0.1086.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/18.0.1087.54 Safari/536.5',
                  'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1088.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1089.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1033.54 Safari/536.5',
                  'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_3_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1034.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1035.54 Safari/536.5',
                  'Mozilla/4.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1036.54 Safari/536.5',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1037.54 Safari/536.5',
    ]
    agentindex = 0
    opencount = 0
    def parse(self, response):
        if self.opencount % 10 == 0:
            print'*************************************'
            print self.opencount
            print'*************************************'
        self.opencount = self.opencount + 1
        if self.opencount > 200:
            self.opencount = 0
            settings.USER_AGENT = self.useragents[(self.agentindex + 1)%self.useragents.__len__()]
        sel = Selector(response)
        #for site in sites:  
        item = WebspiderItem()
        contents = sel.xpath('//div[@class="relative"]//dl//dd//div[@class="subarea"]//a').extract()
        item['area'] = ''
        count = 0
        if contents.__len__() != 0:
            for distict in self.distictstmp:
                if distict['url'] == response.url:
                    curdistict = distict
                    break
            for content in contents:
                count += 1
                contentsel = Selector(text=content)
                localcontens = contentsel.xpath("string(//a)").extract()
                self.data[curdistict['provinceindex']]['sublist'][curdistict['cityindex']]['sublist'][curdistict['distictindex']]['sublist'].append({'name':localcontens[0],'index':count - 1})
                item['area'] += u"{'index':%d,'name':'%s'}," % (count-1, localcontens[0])
            #conn.close()
            myfile = codecs.open('adress.json', 'wb', encoding='utf-8')
            myfile.write(self.data.__str__())
            myfile.close()
            yield item
            return
        
        #urls = sel.xpath('//div[@class="index_bo"]/dl/dd/a/@href').extract()
        dds = sel.xpath('//div[@class="index_bo"]//dl//dd').extract()
        provinces = sel.xpath('//div[@class="index_bo"]//dl//dt//text()').extract()
        count = 0
        for province in provinces:
            count = count + 1
            if count == 1:
                continue
            self.data.append({'name':province,'index':count - 2,'sublist':[]})
            contentsel = Selector(text=dds[count - 1])
            citys = contentsel.xpath("//dd//a//text()").extract()
            urls = contentsel.xpath("//dd/a/@href").extract()
            citycount = 0
            myfile = codecs.open('adress.json', 'wb', encoding='utf-8')
            myfile.write(self.data.__str__())
            myfile.close()
            for url in urls:
                if url != str(response.url):
                    citycount = citycount + 1
                    self.data[count - 2]['sublist'].append({'name':citys[citycount - 1],'index':citycount - 1,'sublist':[]})
                    self.citystmp.append({'url':url,'cityindex':citycount - 1,'provinceindex':count - 2})
                    yield Request(url, callback=self.parse)  
        if provinces.__len__() != 0:
            return
        
        urls = sel.xpath('//div[@class="relative"]/dl[@id="filter_quyu"]/dd/a/@href').extract()
        disticts = sel.xpath('//div[@class="relative"]/dl[@id="filter_quyu"]/dd/a/text()').extract()
        count = 0
        curcity = None
        for city in self.citystmp:
            if city['url'] == response.url:
                curcity = city
                break
        if curcity == None:
            return
        for url in urls:
            count = count + 1
            if count == 1:
                continue
            url = 'http://' + response.url.split('/')[2] + url
            if url != str(response.url):
                #self.myfile.write(response.url + '       ' + url + '\n')
                self.data[curcity['provinceindex']]['sublist'][curcity['cityindex']]['sublist'].append({'name':disticts[count - 2],'index':count - 2,'waitpoint':'','sublist':[]})
                self.distictstmp.append({'url':url,'provinceindex':curcity['provinceindex'],'cityindex':curcity['cityindex'],'distictindex':count - 2})
                self.opencount = self.opencount + 1
                yield Request(url, callback=self.parse)