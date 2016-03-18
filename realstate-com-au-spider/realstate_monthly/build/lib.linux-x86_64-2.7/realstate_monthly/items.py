# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RealstateMonthlyItem(scrapy.Item):
    links = scrapy.Field()
    title = scrapy.Field()
    suburb_name = scrapy.Field()

    unit_mly_jan = scrapy.Field()
    unit_mly_feb = scrapy.Field()
    unit_mly_mar = scrapy.Field()
    
    unit_mly_apr = scrapy.Field()
    unit_mly_may = scrapy.Field()
    unit_mly_jun = scrapy.Field()
    
    unit_mly_jul = scrapy.Field()
    unit_mly_aug = scrapy.Field()
    unit_mly_sep = scrapy.Field()
    
    unit_mly_oct = scrapy.Field()
    unit_mly_nov = scrapy.Field()
    unit_mly_dec = scrapy.Field()
#unit_monthly_avg_price
    unit_mly_p_jan = scrapy.Field()
    unit_mly_p_feb = scrapy.Field()
    unit_mly_p_mar = scrapy.Field()
    
    unit_mly_p_apr = scrapy.Field()
    unit_mly_p_may = scrapy.Field()
    unit_mly_p_jun = scrapy.Field()
    
    unit_mly_p_jul = scrapy.Field()
    unit_mly_p_aug = scrapy.Field()
    unit_mly_p_sep = scrapy.Field()
    
    unit_mly_p_oct = scrapy.Field()
    unit_mly_p_nov = scrapy.Field()
    unit_mly_p_dec = scrapy.Field()
#unit_monthly_no_of_sales
    unit_mly_nos_jan = scrapy.Field()
    unit_mly_nos_feb = scrapy.Field()
    unit_mly_nos_mar = scrapy.Field()
    
    unit_mly_nos_apr = scrapy.Field()
    unit_mly_nos_may = scrapy.Field()
    unit_mly_nos_jun = scrapy.Field()
    
    unit_mly_nos_jul = scrapy.Field()
    unit_mly_nos_aug = scrapy.Field()
    unit_mly_nos_sep = scrapy.Field()
    
    unit_mly_nos_oct = scrapy.Field()
    unit_mly_nos_nov = scrapy.Field()
    unit_mly_nos_dec = scrapy.Field()
    # unit_monthly_info = scrapy.Field()
    # unit_yearly_info = scrapy.Field()
    # house_monthly_info = scrapy.Field()
    # house_yearly_info = scrapy.Field()
    
    #unit_mly_date =  scrapy.Field()
    #unit_mly_price = scrapy.Field()
    #unit_mly_no_of_sales = scrapy.Field()
    
    #unit_yly_date =  scrapy.Field()
    #unit_yly_price = scrapy.Field()
    #unit_yly_no_of_sales = scrapy.Field()

    #house_mly_date =  scrapy.Field()
    #house_mly_price = scrapy.Field()
    #house_mly_no_of_sales = scrapy.Field()
    
    #house_yly_date =  scrapy.Field()
    #house_yly_price = scrapy.Field()
    #house_yly_no_of_sales = scrapy.Field()
    #unit monthly_date
    