# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
       	

class RealstateMonthlyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    links = scrapy.Field()
    title = scrapy.Field()
    suburb_name = scrapy.Field()
    house_avg_sales_jan = scrapy.Field()
    house_avg_sales_feb = scrapy.Field()
    house_avg_sales_mar = scrapy.Field()
    house_avg_sales_apr = scrapy.Field()
    house_avg_sales_may = scrapy.Field()
    house_avg_sales_jun = scrapy.Field()
    house_avg_sales_jul = scrapy.Field()
    house_avg_sales_aug = scrapy.Field()
    house_avg_sales_sep = scrapy.Field()
    house_avg_sales_oct = scrapy.Field()
    house_avg_sales_nov = scrapy.Field()
    house_avg_sales_dec = scrapy.Field()
    house_avg_noofsales_jan = scrapy.Field()
    house_avg_noofsales_feb = scrapy.Field()
    house_avg_noofsales_mar = scrapy.Field()
    house_avg_noofsales_apr = scrapy.Field()
    house_avg_noofsales_may = scrapy.Field()
    house_avg_noofsales_jun = scrapy.Field()
    house_avg_nosales_jul = scrapy.Field()
    house_avg_nosales_aug = scrapy.Field()
    house_avg_nosales_sep = scrapy.Field()
    house_avg_nosales_oct = scrapy.Field()
    house_avg_nosales_nov = scrapy.Field()
    house_avg_nosales_dec = scrapy.Field()
   
    unit_avg_sales_jan = scrapy.Field()
    unit_avg_sales_feb = scrapy.Field()
    unit_avg_sales_mar = scrapy.Field()
    unit_avg_sales_apr = scrapy.Field()
    unit_avg_sales_may = scrapy.Field()
    unit_avg_sales_jun = scrapy.Field()
    unit_avg_sales_jul = scrapy.Field()
    unit_avg_sales_aug = scrapy.Field()
    unit_avg_sales_sep = scrapy.Field()
    unit_avg_sales_oct = scrapy.Field()
    unit_avg_sales_nov = scrapy.Field()
    unit_avg_sales_dec = scrapy.Field()
    unit_avg_noofsales_jan = scrapy.Field()
    unit_avg_noofsales_feb = scrapy.Field()
    unit_avg_noofsales_mar = scrapy.Field()
    unit_avg_noofsales_apr = scrapy.Field()
    unit_avg_noofsales_may = scrapy.Field()
    unit_avg_noofsales_jun = scrapy.Field()
    unit_avg_nosales_jul = scrapy.Field()
    unit_avg_nosales_aug = scrapy.Field()
    unit_avg_nosales_sep = scrapy.Field()
    unit_avg_nosales_oct = scrapy.Field()
    unit_avg_nosales_nov = scrapy.Field()
    unit_avg_nosales_dec = scrapy.Field()

    pass
