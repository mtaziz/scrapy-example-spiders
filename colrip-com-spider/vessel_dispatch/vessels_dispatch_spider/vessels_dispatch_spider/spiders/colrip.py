# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import VesselsDispatchSpiderItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time 
import sys


class ColripSpider(scrapy.Spider):
    name = "colrip"
    allowed_domains = ["colrip.com"]
    start_urls = (
        'http://colrip.com/dispatch-info/dispatch-status/',
    )
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(50)
        super(ColripSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
    	self.driver.get(response.url)
    	sel = Selector(text=self.driver.page_source)
        # item = VesselsDispatchSpiderItem()
        # item['Source_Urls'] = response.url
        
        ###{{First attempt
        ## arrivals = sel.xpath('//*[@id="main"]/div[2]//tr')
        # //*[@id="main"]/div[2]
        # for arrival in arrivals:
      #   	item = VesselsDispatchSpiderItem()
	     #    # vessel_arrivals_name_data = arrival.xpath('/html/body/div[3]/div/div/main/div[1]/text()').extract()
	     #    v_vessel_data = map(unicode.strip, arrival.xpath('//tr//td[1]/text()').extract())
	     #    # /html/body/div[3]/div/div/main/div[2]/table/tbody/tr[3]
	     #    						  #/html/body/div[3]/div/div/main/div[2]/table/tbody/tr[3]/td[1]
	    	# v_from_data = map(unicode.strip, arrival.xpath('//tr//td[2]/text()').extract())
	    	# v_to_data = map(unicode.strip, arrival.xpath('//tr//td[3]/text()').extract())
	    	# v_time_data = map(unicode.strip, arrival.xpath('//tr//td[4]/text()').extract())
	    	# v_tug_data = map(unicode.strip, arrival.xpath('//tr//td[5]/text()').extract())
	    	# v_loa_data = map(unicode.strip, arrival.xpath('//tr//td[6]/text()').extract())
	    	# # //*[@id="main"]/div[2]/table/tbody/tr[2]/td[1]
      #   	# item['Vessel_Arrivals_Name'] = vessel_arrivals_name_data
      #   	item['V_Vessel'] = v_vessel_data
      #   	item['V_From']  = v_from_data
      #   	item['V_To'] = v_to_data
      #   	item['V_Time'] = v_time_data
      #   	item['V_Tug'] = v_tug_data
      #   	item['V_LOA'] = v_loa_data
      #   	yield item
        item = VesselsDispatchSpiderItem()
        items = []
	        # vessel_arrivals_name_data = arrival.xpath('/html/body/div[3]/div/div/main/div[1]/text()').extract()
        v_vessel_data = map(unicode.strip, sel.xpath('//tr//td[1]/text()').extract())
        # /html/body/div[3]/div/div/main/div[2]/table/tbody/tr[3]
        						  #/html/body/div[3]/div/div/main/div[2]/table/tbody/tr[3]/td[1]
    	v_from_data = map(unicode.strip, sel.xpath('//tr//td[2]/text()').extract())
    	v_to_data = map(unicode.strip, sel.xpath('//tr//td[3]/text()').extract())
    	v_time_data = map(unicode.strip, sel.xpath('//tr//td[4]/text()').extract())
    	v_tug_data = map(unicode.strip, sel.xpath('//tr//td[5]/text()').extract())
    	v_loa_data = map(unicode.strip, sel.xpath('//tr//td[6]/text()').extract())
    	# //*[@id="main"]/div[2]/table/tbody/tr[2]/td[1]
    	# item['Vessel_Arrivals_Name'] = vessel_arrivals_name_data
    	item['V_Vessel'] = v_vessel_data
    	item['V_From']  = v_from_data
    	item['V_To'] = v_to_data
    	item['V_Time'] = v_time_data
    	item['V_Tug'] = v_tug_data
    	item['V_LOA'] = v_loa_data
    	items.append(item)
        return items


        	# return data
    # Vessel_Arrivals_Name = Field()
    # V_Vessel = Field()
    # V_From = Field()
    # V_To = Field()
    # V_Time = Field()
    # V_Tug = Field()
    # V_LOA = Field()