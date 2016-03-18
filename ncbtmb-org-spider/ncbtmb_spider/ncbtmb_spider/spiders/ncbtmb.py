# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NcbtmbSpiderItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time
import sys


class NcbtmbSpider(CrawlSpider):
    name = "ncbtmb"
    allowed_domains = ["ncbtmb.org"]
    ##New York##
    start_urls = ['http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=&email=&name=&phone=&state=NY&zipcode=&country=All&page=2&modality=',]
    ## SanFrancisco
    # start_urls = ['http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=San%20Francisco&email=&name=&phone=&state=All&zipcode=&country=All&page=0&modality=',]
                 # http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=San%20Francisco&email=&name=&phone=&state=All&zipcode=&country=All&page=1&modality=
                 # http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?name=&phone=&city=San%20Francisco&state=All&zipcode=&country=All&modality=
    #Chicago
    #http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=Chicago&email=&name=&phone=&state=All&zipcode=&country=All&page=0&modality=
    # start_urls = ['http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=Chicago&email=&name=&phone=&state=All&zipcode=&country=All&page=0&modality=',]

    ##
    # start_urls = ['http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=&email=&name=&phone=&state=NY&zipcode=&country=All&page=2&modality=',]

            # %(n) for n in range(1,20)
    rules = (Rule(LinkExtractor(allow=(r'/find\-a\-certified\-massage\-therapist/results\?city=&email=&name=&phone=&state=NY&zipcode=&country=All&page=\d+\&modality=')),
    ###San Francisco
    # rules = (Rule(LinkExtractor(allow=(r'/find\-a\-certified\-massage\-therapist/results\?city=San\%20Francisco&email=&name=&phone=&state=All&zipcode=&country=All&page=\d+\&modality=')),
        # http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=San%20Francisco&email=&name=&phone=&state=All&zipcode=&country=All&page=\d+\&modality=
        # #Chicago
        # # http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=Chicago&email=&name=&phone=&state=All&zipcode=&country=All&page=0&modality=

    # rules = (Rule(LinkExtractor(allow=(r'/find\-a\-certified\-massage\-therapist/results\?city=Chicago&email=&name=&phone=&state=All&zipcode=&country=All&page=\d+\&modality=')),
            process_links='process_links',
            callback='parse_ncbtmb',
            follow=True,
            # max_pages=5
            ),
        )
    # def parse_ncbtmb(self, response):
    def parse_ncbtmb(self, response):
    # def parse_ncbtmb(self, response):
        sel = Selector(response)
        # infos = sel.xpath('//tr[contains(@class, "odd board-certified-Yes views-row-first") or contains(@class, "even board-certified-Yes") or contains(@class, "even board-certified-No") or contains(@class, "odd board-certified-Yes") or contains(@class, "odd board-certified-no")]')
        # Yes
        # infos = sel.xpath('//tr[contains(@class, "odd board-certified-Yes views-row-first") or contains(@class, "even board-certified-Yes views-row-first") or contains(@class,"odd board-certified-Yes views-row-last") or contains(@class,"even board-certified-Yes views-row-last") or contains(@class, "even board-certified-Yes") or contains(@class, "odd board-certified-Yes")]')
        # No
        infos = sel.xpath('//tr[contains(@class, "odd board-certified-No views-row-first") or contains(@class, "even board-certified-No views-row-first") or contains(@class,"odd board-certified-No views-row-last") or contains(@class,"even board-certified-No views-row-last") or contains(@class, "even board-certified-No") or contains(@class, "odd board-certified-No")]')

#         <tr
#         contains(@class,"even board-certified-No views-row-last")
#         >
# <tr class="odd board-certified-No views-row-first">
        for info in infos:
            item = NcbtmbSpiderItem()
            items = []
            # /html/body/div[2]/div[4]/div/div/div/section/article/div/div/table/tbody/tr[2]/td[1]
            Name_data = map(unicode.strip, info.xpath('.//td[1]/text()').extract())
            City_data = map(unicode.strip, info.xpath('.//td[2]/text()').extract())
            State_data = map(unicode.strip, info.xpath('.//td[3]/text()').extract())
            Zip_data = map(unicode.strip, info.xpath('.//td[4]/text()').extract())
            Phone_data = map(unicode.strip, info.xpath('.//td[5]/text()').extract())
            Email_data = map(unicode.strip, info.xpath('.//td[6]/a/text()').extract())
            # Yes_No_data = 'Yes'
            # /html/body/div[2]/div[4]/div/div/div/section/article/div/div/table/tbody/tr[1]/td[1]
            # //*[@id="main"]/div[2]/table/tbody/tr[2]/td[1]
            # item['Vessel_Arrivals_Name'] = vessel_arrivals_name_data
            item['Name'] = Name_data
            item['City'] = City_data
            item['State'] = State_data
            # item['State_Info'] = State_data
            item['Zip'] = Zip_data
            item['Phone'] = Phone_data
            item['Email'] = Email_data
            # item['Yes_No'] = 'Yes'
            item['Yes_No'] = 'No'

            yield item
        # items.append(item)
        # return items
