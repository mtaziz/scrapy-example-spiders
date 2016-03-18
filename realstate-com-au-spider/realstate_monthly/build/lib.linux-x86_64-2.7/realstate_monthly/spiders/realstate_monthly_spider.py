# -*- coding: utf-8 -*-
import scrapy
#import validators
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from collections import defaultdict
from functools import partial
#from selenium import webdriver
#from ..items RealstateItem
#from .. items import RealstateMonthlyItem
#import os
#from newscrawler.items import NewsItem
import urllib2
import re
import json
#from bs4 import BeautifulSoup
import logging
import datetime
import base64
#from urllib import request
from realstate_monthly.items import RealstateMonthlyItem

class RealstateMonthlySpiderSpider(CrawlSpider):
    name = "realstate_monthly_spider"
    allowed_domains = ["realstate.com.au"]
    start_urls = (
        # 'https://www.realestate.com.au/neighbourhoods/Alkimos-6038-wa',
        # 'https://www.realestate.com.au/neighbourhoods/Anketell-6167-wa',
        'https://www.realestate.com.au/neighbourhoods/East%20Perth-6004-wa',
        'https://www.realestate.com.au/neighbourhoods/Applecross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Ardross-6153-wa',
        'https://www.realestate.com.au/neighbourhoods/Armadale-6112-wa',
        'https://www.realestate.com.au/neighbourhoods/Ashby-6065-wa',
        'https://www.realestate.com.au/neighbourhoods/Ascot-6104-wa',
        )

    rules = (Rule(LinkExtractor(allow=(),), callback='parse',follow=True),)

    #def link_callback(self, links):
    #   return links
    #service_args = [
    #    '--ignore-ssl-errors=true',
    #]
    #driver = webdriver.PhantomJS(service_args=service_args)
    #from scrapy.selector import Selector
    #import json
    #response_json = json.loads(response.body_as_unicode())
    #html = response_json['content_html']
    #sel = Selector(text=html)
    #for url in sel.xpath('//@href').extract():
    #yield Request(url, callback=self.somecallbackfunction)
    def getListOfUnitMonthlyDates(self, unit_monthly_date, item):
        
        unitMonthlyDateList = ['unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 
        'unit_mly_may', 'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 
        'unit_mly_nov', 'unit_mly_dec']
        
        for x in unitMonthlyDateList:
            item[x] = ''
            index = 0
            for x in zip(unit_monthly_date):
                item[unitMonthlyDateList[index]] = x
                index=index+1

    def getListOfUnitMonthlyPrice(self, unit_monthly_price,item):
        unitMonthlyPriceList = ['unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 'unit_mly_p_apr',
         'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 
         'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec']
        for y in unitMonthlyPriceList:
            item[y] = ''
            index_p = 0
            for y in zip(unit_monthly_price):
                item[unitMonthlyPriceList[index_p]] = y
                index_p=index_p+1
                
    def getListofUnitMonthlyNoOfSales(self, replaced_unit_monthly_no_of_sales, item):
        unitMonthlyNoofsalesList = ['unit_mly_nos_jan', 'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 
        'unit_mly_nos_may', 'unit_mly_nos_jun', 'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 
        'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec']
        
        # item['unit_mly_nos_jan'] = 
        for z in unitMonthlyNoofsalesList:
            item[z] = ''
            index_s = 0
            for z in replaced_unit_monthly_no_of_sales:
                item[unitMonthlyNoofsalesList[index_s]] = z
                index_s=index_s+1
                #print len(replaced_unit_monthly_no_of_sales)

    def parse(self, response):
        #self.driver.get(response.url)
        #sel = Selector(text=self.driver.page_source)
        item = RealstateMonthlyItem()
        sel = Selector(response)
        main_title = sel.xpath('.//div[@class="section"]/h1[@id="suburb-name"]/text()').extract()
        suburb = sel.xpath('.//div[@class="section"]/div[@class="subtitle h3 white"]/text()').extract()
        # items = []
        
        item['links'] = response.url
        item['title'] = main_title
        item['suburb_name'] = suburb
        items = []
        # items.append(item)
        house_trends = sel.xpath('//*[@class="slide-content"]')
        for house_trend in house_trends:
            item = RealstateMonthlyItem()
            house_avg_sales_jan_1 = []
            #house_avg_sales_jan_1 = sel.css('#highcharts-8 > svg > g.highcharts-series-group > g:nth-child(2) > path:nth-child(12)/text()').extract()
            #house_avg_sales_jan_1 = house_trend.xpath('//*[@id="highcharts-8"]').extract()
            #working_1: house_avg_sales_jan_1 = house_trend.xpath('//div[@class="slide-section median-price-subsections trend"] and contains(.., "price")').extract()
            #house_avg_sales_jan_1 = sel.xpath('.//div[contains(@class, "slide-section median-price-subsections trend") and contains(name(), '"price"') and contains(name(),'"count"')]').extract()
            house_avg_sales_jan_1 = house_trend.xpath('//div[contains(@class, "slide-section median-price-subsections trend") and contains(name(), '"price"') and contains(name(),'"count"')]').extract()
            #house_avg_sales_jan_1_demo = house_trend.xpath('//div[contains(@class, "slide-section median-price-subsections trend")]').extract()

            #item['created_time'] = re.search('[\d\-: ]+', selector.xpath('//div[@class="zwfbtime"]/text()').extract()[0]).group(0)
            #convert list object to string
            house_and_unit_data = str(house_avg_sales_jan_1)
            #clean up html tags and get unit price container
            unit_price_data = re.findall(r'\"unit\":\{\"\d+-\d+-\d+(?=).+true\}\}\,', house_and_unit_data)
            #get house price date and count data
            house_price_data = re.findall(r'\"house\":\{\"\d+-\d+-\d+(?=).+true\}\}\}\}', house_and_unit_data)
            #monthly data for unit
            unit_monthly_data = re.findall('\"2015\-\d+\-\d+\"\:\{\"price\"\:\d.+\,\"count\"\:\d+', str(unit_price_data))
            #yearly data for units
            unit_yearly_data = re.findall('\"20[0-9]{1}[^5]\-\d+\-\d+\"\:\{\"price\"\:\d+.\d+\,\"count\"\:\d+\}', str(unit_price_data))
            #monthly data for house
            house_monthly_data = re.findall('"2015\-\d+\-\d+\"\:\{\"price\"\:\d.+\,\"count\"\:\d+', str(house_price_data))
            #yearly data for house
            house_yearly_data = re.findall('\"20[0-9]{1}[^5]\-\d+\-\d+\"\:\{\"price\"\:\d+.\d+\,\"count\"\:\d+\}', str(house_price_data))
            #try:
            #street_number = re.search(r'([0-9\-]+)\s', data).group(1)
            #street_name = data.replace(street_number, '', 1).strip()
            #    return {'street_number': street_number, 'street_name': street_name}
            #except:
            #    return {'street_number': "", 'street_name': data.strip()}
            unit_monthly_date = re.findall(r'2015\-\d+\-\d+',str(unit_monthly_data))
            self.getListOfUnitMonthlyDates(unit_monthly_date, item)
            unit_monthly_price = re.findall(r'[0-9]{6}',str(unit_monthly_data))
            self.getListOfUnitMonthlyPrice(unit_monthly_price, item)

            unit_monthly_no_of_sales = re.findall(r'\"count\":\d+',str(unit_monthly_data))
            #replaced_unit_monthly_no_of_sales = str(unit_monthly_no_of_sales).replace('"count":', '')
            replaced_unit_monthly_no_of_sales = re.findall(r'\d+', str(unit_monthly_no_of_sales))
            # str_unit_monthly_no_of_sales = str(replaced_unit_monthly_no_of_sales)
            # self.getListofUnitMonthlyNoOfSales(str_unit_monthly_no_of_sales, item)
            self.getListofUnitMonthlyNoOfSales(replaced_unit_monthly_no_of_sales, item)


            #class_dict= defaultdict(lambda: defaultdict(lambda: defaultdict(str)))

            # unit_monthly_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            # for (umdate, umprice, umcount) in zip(unit_monthly_date, unit_monthly_price, replaced_unit_monthly_no_of_sales):
            #     unit_monthly_dict[umdate][umprice].append(umcount)
            # unit_monthly_dict= defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
            # for (umdate, umprice, umcount) in zip(unit_monthly_date, unit_monthly_price, replaced_unit_monthly_no_of_sales):
            #     l = len(unit_monthly_dict[umdate][umprice])
            #     unit_monthly_dict[umdate][umprice][l+1] = umcount

            # unit_monthly_dict = dict(zip(unit_monthly_date, zip(unit_monthly_price, replaced_unit_monthly_no_of_sales)))

            unit_yearly_date = re.findall('\d+\-\d+\-\d+',str(unit_yearly_data))
            unit_yearly_price = re.findall('[0-9]{6}',str(unit_yearly_data))
            unit_yearly_no_of_sales = re.findall('\"count\":\d+',str(unit_yearly_data))
            replaced_unit_yearly_no_of_sales = str(unit_yearly_no_of_sales).replace('"count":', '')

            #d = dict(zip(maker,zip(year,model)))
            # unit_yearly_dict = defaultdict(partial(defaultdict,list))
            # for (uydate, uyprice, uycount) in zip(unit_yearly_date, unit_yearly_price, replaced_unit_yearly_no_of_sales):
            #     unit_yearly_dict[uydate][uyprice].append(uycount)
            
            # unit_yearly_dict = dict(zip(unit_yearly_date, zip(unit_yearly_price, replaced_unit_yearly_no_of_sales)))

            house_monthly_date = re.findall(r'2015\-\d+\-\d+',str(house_monthly_data))
            house_monthly_price = re.findall(r'[0-9]{6}',str(house_monthly_data))
            house_monthly_no_of_sales = re.findall(r'\"count\":\d+',str(house_monthly_data))
            replaced_house_monthly_no_of_sales = str(house_monthly_no_of_sales).replace('"count":', '')
            #dict of monnthly data for house
            # house_monthly_dict = defaultdict(partial(defaultdict, list))
            # for (hmdate, hmprice, hmcount) in zip(house_monthly_date, house_monthly_price, replaced_house_monthly_no_of_sales):
            #     house_monthly_dict[hmdate][hmprice].append(hmcount)

            # house_monthly_dict = dict(zip(house_monthly_date, zip(house_monthly_price, replaced_house_monthly_no_of_sales)))

            house_yearly_date = re.findall('\d+\-\d+\-\d+',str(house_yearly_data))
            house_yearly_price = re.findall('[0-9]{6}',str(house_yearly_data))
            house_yearly_no_of_sales = re.findall('\"count\":\d+',str(house_yearly_data))
            replaced_house_yearly_no_of_sales = str(house_yearly_no_of_sales).replace('"count":', '')
            #dict of yearly data for house
            # house_yearly_dict = dict(zip(house_yearly_date, zip(house_yearly_price, replaced_house_yearly_no_of_sales)))
            # house_yearly_dict = defaultdict(partial(defaultdict, list))
            # # for (hydate, hyprice, hycount) in zip(house_yearly_date, house_yearly_price, replaced_house_monthly_no_of_sales):
            #     house_yearly_dict[hydate][hyprice].append(hycount)
            
            
            # item['unit_monthly_info'] = unit_monthly_dict
            # item['unit_yearly_info'] = unit_yearly_dict
            # item['house_monthly_info'] = house_monthly_dict
            # item['house_yearly_info'] = house_yearly_dict

            # item['unit_mly_date'] = unit_monthly_date
            # item['unit_mly_price'] = unit_monthly_price
            # item['unit_mly_no_of_sales'] = replaced_unit_monthly_no_of_sales
            # item['unit_yly_date'] =  unit_yearly_date
            # item['unit_yly_price'] = unit_yearly_price
            # item['unit_yly_no_of_sales'] = replaced_unit_yearly_no_of_sales
            # item['house_mly_date'] =  house_monthly_date
            # item['house_mly_price'] = house_monthly_price
            # item['house_mly_no_of_sales'] = replaced_house_monthly_no_of_sales
            # item['house_yly_date'] =  house_yearly_date
            # item['house_yly_price'] = house_yearly_price
            # item['house_yly_no_of_sales'] = replaced_house_yearly_no_of_sales
            main_title = sel.xpath('.//div[@class="section"]/h1[@id="suburb-name"]/text()').extract()
            suburb = sel.xpath('.//div[@class="section"]/div[@class="subtitle h3 white"]/text()').extract()
            item['links'] = response.url
            item['title'] = main_title
            item['suburb_name'] = suburb
            #items.append(item)
            return item

        #     items.append(item)
        #     # return items
        #     return items
        # item = RealstateMonthlyItem()
        # main_title = sel.xpath('.//div[@class="section"]/h1[@id="suburb-name"]/text()').extract()
        # suburb = sel.xpath('.//div[@class="section"]/div[@class="subtitle h3 white"]/text()').extract()
        # # items = []
        
        # item['links'] = response.url
        # item['title'] = main_title
        # item['suburb_name'] = suburb
        # items.append(item)
        # return items
        # #items.append(item_info)
        # return item
        
        #//*[@id="suburb-name"]
        #//*[@id="title"]/div
    #yield item
