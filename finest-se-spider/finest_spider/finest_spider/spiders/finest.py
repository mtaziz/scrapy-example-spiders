# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from scrapy.http import TextResponse
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, CrawlSpider, Rule
from ..items import FinestSpiderItem
from scrapy.selector import Selector
from selenium.webdriver.common.proxy import *
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import sys
import re
import os
from level1 import *
# from level2 import *
# from level3 import *
reload(sys)
sys.setdefaultencoding('utf-8')


class FinestSpider(scrapy.Spider):
    name = "finest"
    allowed_domains = ["finest.se"]
    start_urls = getStartURLS()
    # start_urls = ['http://finest.se/madelenehedberg']
    # start_urls = ['http://finest.se/blogs-topbloggers']
    # start_urls = ['http://finest.se/member-blog']
    # start_urls = [l.strip() for l in open('/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/urls_list3.txt').readlines()]
    # start_urls = [l.strip() for l in open('/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/level3_part1.txt').readlines()]
    # start_urls = [l.strip() for l in open('/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/urls_general_blogger_3.csv').readlines()]
    # urls_general_blogger_3
    # level3_start_urls_as_list

    # def __init__(self, filename=None):
    #     if filename:
    #     with open(filename, 'r') as f:
    #         self.start_urls = f.readlines()
    #         print self.start_urls

    # def start_requests(self):
    #     df = pd.read_csv('test.csv')
    #     saved_column = df.ProductName
    #     for url in saved_column:
    #         yield Request(url, self.parse)

    # def start_requests(self):
    #     self.filename = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/level3_start_urls_as_list.txt'
    #     with open(self.filename, 'r') as myfile:
    #         for url in myfile:
    #             yield Request(url, self.parse)

    def __init__(self, *args, **kwargs):
        super(FinestSpider, self).__init__(*args, **kwargs)
        self.js_bin = settings.get('JS_BIN')
    #     self.filename = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/level1_start_urls.txt'
    #     # # self.js_wait = settings.get('JS_WAIT')
    #     # # self.start_urls = ['http://finest.se/blog-toplist']
    #     # # service_args = ['--ignore-ssl-errors=true', '--load-images=false', '--ssl-protocol=any']
    #     # # service_args = ['--proxy=%s' % settings.get('HTTP_PROXY'), '--ignore-ssl-errors=true','--proxy-type=socks5', '--load-images=false','--ssl-protocol=any']
        service_args = ['--ignore-ssl-errors=true', '--load-images=false', '--ssl-protocol=any']
    #     # # self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS(service_args=service_args)
        # # self.driver = webdriver.PhantomJS(executable_path=self.js_bin)
        self.driver.implicitly_wait(10)
    #     # if self.filename:
    #     #     with open(self.filename, 'r') as myfile:
    #     #         self.start_urls = myfile.readlines()

    def parse(self, response):
        sel = Selector(response)
        # self.driver.get(response.url)
        # sel = Selector(text=self.driver.page_source)
        item = FinestSpiderItem()
        item['Blogger_Urls'] = response.url
        response_url = response.url
        # item['Blogger_Name'] = response_url.lstrip('http://finest.se/').strip('/')
        item['Blogger_Name'] = re.findall(r'\w+\Z', str(response_url))
        if not item['Blogger_Name']:
            item['Blogger_Name'] = response_url.lstrip('http://finest.se/').strip('/')
        # blog name: re.findall(r'\w+\Z', str(test2))
        # clean1 = re.findall(r'\w+@\w+',str(dolk))
        # item['Blogger_Email'] = map(unicode.strip, sel.xpath('//*[contains(text(),"@")]/text()').extract())
        emails_data = map(unicode.strip, sel.xpath('//*[contains(text(),"@")]/text()').extract())
        emails_data_clean = ''.join(emails_data).strip()
        item['Profile_Info'] = emails_data_clean
        # regex = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    # "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    # "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
        # instagram.+|(\w+@\w+.\w+)
        # list(dropwhile(lambda x: not re.match(r'(?i)email:', x), div.strings))
        # Email: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b
        emails_only_data = ','.join(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b', str(emails_data))).strip()
        item['Blogger_Email'] = emails_only_data
        yield item
