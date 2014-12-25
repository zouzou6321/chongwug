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
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
DOWNLOAD_DELAY = 4
CONCURRENT_REQUESTS = 1
ITEM_PIPELINES = {
    'webspider.pipelines.WebspiderPipeline':1
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webspider (+http://www.yourdomain.com)'
