# -*- coding:utf-8 -*-
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector
import MySQLdb,os,datetime  
from webspider.items import WebspiderItem  

if 'SERVER_SOFTWARE' in os.environ:
   MYSQL_HOST = 'chongwug.mysql.rds.aliyuncs.com'
   MYSQL_PORT = 3306
   MYSQL_USER = 'chongwug'
   MYSQL_PASS = 'weet6321'
   MYSQL_DB   = 'chongwug'
else:
   # Make `python manage.py syncdb` works happy!
   MYSQL_HOST = 'localhost'
   MYSQL_PORT = 3306
   MYSQL_USER = 'root'
   MYSQL_PASS = ''
   MYSQL_DB   = 'chongwug'

conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASS,db=MYSQL_DB,port=MYSQL_PORT)
conn.set_character_set('utf8')
class webspiderSpider(Spider):  
    """webspiderSpider"""  
  
    name = "dog126"  
    download_delay = 1
    allowed_domains = ["dog126.com"]  
    start_urls = [  
        "http://www.dog126.com/ggjs.html",
        #"http://www.dog126.com/doginfo_136.html"
    ]  
    
    def parse(self, response):  
  
        sel = Selector(response)
        #for site in sites:  
        item = WebspiderItem()
        tmp = sel.xpath('//div[@class="Details_main"]/ul/li[1]/text()').extract()
        if tmp.__len__() != 0:
            item['name'] = tmp[0].encode('utf8').split('：')[1]
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[2]/text()').extract()
            item['ename'] = tmp[0].encode('utf8').split('：')[1] 
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[3]/text()').extract() 
            item['where'] = tmp[0].encode('utf8').split('：')[1]  
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[4]/text()').extract() 
            item['age'] = tmp[0].encode('utf8').split('：')[1]
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[5]/text()').extract() 
            item['nickname'] = tmp[0].encode('utf8').split('：')[1]
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[6]/text()').extract() 
            item['maleheight'] = tmp[0].encode('utf8').split('：')[1]
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[7]/text()').extract() 
            item['fmaleheight'] = tmp[0].encode('utf8').split('：')[1]
            tmp = sel.xpath('//div[@class="Details_main"]/ul/li[8]/span[2]/em/@style').extract() 
            #item['score'] = [t.encode('utf-8') for t in tmp]
            item['score'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            article_url = str(response.url)
            item['url'] = article_url.encode('utf8')
            
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[1]/span[2]/em/@style').extract()
            item['nianren'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[2]/span[2]/em/@style').extract()
            item['xijiao'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[3]/span[2]/em/@style').extract()
            item['diaomao'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[4]/span[2]/em/@style').extract()
            item['tiwei'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[5]/span[2]/em/@style').extract()
            item['meirong_hz'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[6]/span[2]/em/@style').extract()
            item['kidfred'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[7]/span[2]/em/@style').extract()
            item['otherfred'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[8]/span[2]/em/@style').extract()
            item['animfred'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[9]/span[2]/em/@style').extract()
            item['yundong'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[10]/span[2]/em/@style').extract()
            item['xulian'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[11]/span[2]/em/@style').extract()
            item['koushui'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[12]/span[2]/em/@style').extract()
            item['naihan'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[13]/span[2]/em/@style').extract()
            item['naire'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="pet-feature-dea"]/li[14]/span[2]/em/@style').extract()
            item['cityfred'] = tmp[0].encode('utf8').split(':')[1].split('%')[0]
            tmp = sel.xpath('//div[@class="Details_img"]/img/@src').extract()
            item['image_urls'] = sel.xpath('//div[@class="Details_img"]/img/@src').extract()
            imgpath = u'http://chongwug-pic.b0.upaiyun.com/pettypepic/%s' % (item['image_urls'][0].split('/')[-1]).decode('utf8')
            cur = conn.cursor()
            sql = u"INSERT INTO `manager_dog123`(`url`, `name`, `ename`, `where`, `age`, `nickname`, `maleheight`, `fmaleheight`, `score`,\
            `nianren`, `xijiao`, `diaomao`, `tiwei`, `meirong_hz`, `kidfred`, `otherfred`, `animfred`, `yundong`,`xulian`, `koushui`,\
            `naihan`, `naire`, `cityfred`, `imgurl`) VALUES ('" + item['url'].decode('utf8') + u"','" + item['name'].decode('utf8') + u"','" + \
            item['ename'].decode('utf8') + u"','" + item['where'].decode('utf8') + u"','" + item['age'].decode('utf8') + u"','" + \
            item['nickname'].decode('utf8') + u"','" + item['maleheight'].decode('utf8') + u"','" + item['fmaleheight'].decode('utf8')\
            + u"','" + item['score'].decode('utf8') + u"','" + item['nianren'].decode('utf8') + u"','" + item['xijiao'].decode('utf8') + \
            u"','" + item['diaomao'].decode('utf8') + u"','" + item['tiwei'].decode('utf8') + u"','" + item['meirong_hz'].decode('utf8') + \
            u"','" + item['kidfred'].decode('utf8') + u"','" + item['otherfred'].decode('utf8') + u"','" + item['animfred'].decode('utf8') + \
            u"','" + item['yundong'].decode('utf8') + u"','" + item['xulian'].decode('utf8') + u"','" + item['koushui'].decode('utf8') + \
            u"','" + item['naihan'].decode('utf8') + u"','" + item['naire'].decode('utf8') + u"','" + item['cityfred'].decode('utf8') + u"','" + imgpath + u"')"
            cur.execute(sql)
            conn.commit()
            #conn.close()
            yield item
        #获得下一篇文章的url  
        urls = sel.xpath('//div[@class="jieshao"]/dl/dt/a/@href').extract()  
        for url in urls:
            url = "http://www.dog126.com/" + url
            if url != str(response.url):
                yield Request(url, callback=self.parse)
        urls = sel.xpath('//div[@class="publicTabNew"]/ul[@class="tab"]/li[2]/a/@href').extract()  
        for url in urls: 
            url = "http://www.dog126.com" + url
            if url != str(response.url):
                yield Request(url, callback=self.parse)