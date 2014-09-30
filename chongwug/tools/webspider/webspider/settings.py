# -*- coding: utf-8 -*-

# Scrapy settings for webspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webspider'

SPIDER_MODULES = ['webspider.spiders']
NEWSPIDER_MODULE = 'webspider.spiders'

ITEM_PIPELINES = {  
    'webspider.pipelines.WebspiderPipeline':300  
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webspider (+http://www.yourdomain.com)'
