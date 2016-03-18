# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import StadlistanSwedenItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time 
import sys

class StadlistanSpiderSpider(CrawlSpider):
    name = "stadlistan_spider"
    allowed_domains = ["stadlistan.se"]
    # start_urls = ['http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True&Page=%d' %(n+2) for n in range(1,500)]
    start_urls = (
    	'http://www.stadlistan.se/s/st%C3%A4dning/stockholm',
    	'http://www.stadlistan.se/s/st%C3%A4dning/',
    	'http://www.stadlistan.se/s/st%C3%A4dning/g%C3%B6teborg',
    	'http://www.stadlistan.se/s/st%C3%A4dning/malm%C3%B6',
        # 'http://www.stadlistan.se/c/malm%C3%B6/kms-services/1111955122',
    )
    # LinkExtractor(allow=(r'/lawyer/\w.+$'), deny=(r'/contact', r'/vcard', r'/questions', r'tel'),), #working Latestv1
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.stadlistan.se/\w.+/\w.+/\w.+'), deny=(r'/ajax/company/'),),
            process_links='process_links',
            callback='parse_stadlistan',
            follow=True,
            # max_pages=5
            ),
        )
    ###}}}
    
    ###{{{
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(20)
        super(StadlistanSpiderSpider, self).__init__(*args, **kwargs)

    def parse_stadlistan(self, response):
    	self.driver.get(response.url)
    	sel = Selector(text=self.driver.page_source)
    	item = StadlistanSwedenItem()
    	item['Source_Urls'] = response.url
    	# //*[@id="company-main"]/div[1]/h1/span
    	item['Company_Name'] = sel.xpath('//*[@id="company-main"]/div[1]/h1/span/text()').extract()
    	item['Company_Website'] = sel.xpath('//*[@id="company-main"]/div[3]/div[3]/address/a[2]//@href').extract()
    	item['Email'] = sel.xpath('//*[@id="company-main"]/div[3]/div[2]/a[2]/@href').extract()
    	return item
        pass
