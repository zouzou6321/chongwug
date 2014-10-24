# -*- coding:utf-8 -*-
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector
import MySQLdb,os,datetime,string
from webspider.items import WebspiderItem  
import codecs
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
    myfile = codecs.open('pclady.html', 'wb', encoding='utf-8') 
    name = "pclady"  
    download_delay = 1
    allowed_domains = ["pclady.com.cn"]  
    start_urls = [  
        "http://pet.pclady.com.cn/baike/ggsy/zbyg/",
        #"http://www.dog126.com/doginfo_136.html"
    ]  
    urllist = ['http://pet.pclady.com.cn/baike/ggsy/zbyg/']
    def parse(self, response):  
  
        sel = Selector(response)
        #for site in sites:  
        item = WebspiderItem()
        tmp = sel.xpath('//div[@class="artText"]//table//tr//td//p[3]//a[1]//text()').extract()
        print tmp
        if tmp.__len__() != 0 and tmp[0] != u'':
            item['name'] = tmp[0].encode('utf8')
            article_url = str(response.url)
            item['url'] = article_url.encode('utf8')
            tmp = sel.xpath('//div[@class="layAB"]//div[@class="artCon"]//h1//text()').extract()
            if tmp.__len__() != 0:
                item['title'] = tmp[0].encode('utf8')
            else:
                item['title'] = ''
            pcontens = sel.xpath('//div[@class="artText"]//table//tr//td//p//text()').extract()
            print pcontens.__len__()
            item['content'] = ''
            for pconten in pcontens:
                item['content'] += pconten.encode('utf8')
            item['image_urls'] = sel.xpath('//div[@class="artText"]//table//tr//td//p[2]//a//img//@src').extract()

            imgpath = u'http://chongwug-pic.b0.upaiyun.com/petbringpic/%s' % (item['image_urls'][0].split('/')[-1]).decode('utf8')
            cur = conn.cursor()
            sql = u"INSERT INTO `manager_pclady`(`url`, `name`,`imgurl`, `title`, `content`) VALUES ('" + item['url'].decode('utf8') + u"','" + item['name'].decode('utf8') + u"','" + imgpath + u"','" + item['title'].decode('utf8') + u"','" + item['content'].decode('utf8') + u"')"
            cur.execute(sql)
            conn.commit()
            #conn.close()
            yield item
        #获得下一篇文章的url  
        urls = sel.xpath('//div[@class="layAB"]/ul[@class="picListA"]/li/i[@class="iPic"]/a/@href').extract()  
        for url in urls:
            if url != str(response.url):
                self.myfile.write(url)
                yield Request(url, callback=self.parse)
        urls = sel.xpath('//div[@class="layAB"]/div[@class="pclady_page"]/a/@href').extract()  
        for url in urls:
            if url != str(response.url):
                for urla in self.urllist:
                    if url == urla:
                        return
                self.urllist.append(url)
                yield Request(url, callback=self.parse)