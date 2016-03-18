# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import HillsboroughItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time 
import sys


class HillsboroughSpider(CrawlSpider):
    name = "hillsborough_spider"
    allowed_domains = ["gis.hcpafl.org"]
    # http://gis.hcpafl.org/propertysearch/#/search/advanced/prop=0700,0040,0000,0006&mvlow=1000&mvhigh=30000&pagesize=80&page=%d
    start_urls = ['http://gis.hcpafl.org/propertysearch/#/parcel/basic/172730028R00000000100U']
    # start_urls = ['http://gis.hcpafl.org/propertysearch/#/search/advanced/prop=0700,0040,0000,0006&mvlow=1000&mvhigh=30000&pagesize=80&page=%d' %(n) for n in range(1,3)]
    
    ###{{{Rules To Be Applied for all the links found in subsequent pages
    rules = (
        # http://gis.hcpafl.org/propertysearch/#/parcel/basic/172730028R00000000070U
        # http://gis.hcpafl.org/propertysearch/#/parcel/basic/172730028R00000000080U
        # http://gis.hcpafl.org/propertysearch/#/parcel/basic/172730028R00000000090U
        # http://gis.hcpafl.org/propertysearch/#/parcel/basic/172730028R00000000100U
        # Rule(LinkExtractor(allow=(r'/parcel/basic/\d+\\d+\w.+$')),
        # http://gis\.hcpafl\.org/propertysearch/\#/parcel/basic/\w+\d+
        Rule(LinkExtractor(allow=(r'http://gis.hcpafl.org/propertysearch/\#/parcel/basic/\w+\d+$')),
            process_links='process_links',
            callback='parse_hillsborough',
            follow=True,
            # max_pages=5
            ),
        )
    ###}}}
    
    ###{{{
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(60)
        super(HillsboroughSpider, self).__init__(*args, **kwargs)
    ###}}}
    
    def parse_hillsborough(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = HilllsboroughItem()
        item['Source_Urls'] = response.url
        #div#content div#details.tabcontent div.property-data div.propcard-section span.multiline
        item['Company_Name'] = sel.css('div#content div#details.tabcontent div.property-data div.propcard-section span.multiline::text').extract()[0]
        #html.ie.ie9 body form#form1 div.main_wrapper div.content_wrapper div.container div.content_block.no-sidebar.row div.fl-container.span12 div.row div.posts-block.span12 div#content div#details.tabcontent div.property-data div.propcard-section span.multiline
        #div#content div#details.tabcontent div.property-data div.propcard-section span.multiline
        item['Mailing_Address'] = sel.css('div#content div#details.tabcontent div.property-data div.propcard-section span.multiline::text').extract()
        return item 
        self.driver.quit()
