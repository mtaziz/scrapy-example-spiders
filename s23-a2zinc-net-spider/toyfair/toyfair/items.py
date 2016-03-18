# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToyfairItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = scrapy.Field()
    Exhibitors_Name = scrapy.Field()
    Exhibitors_Address = scrapy.Field()
    Exhibitors_Website = scrapy.Field()
    Booth_ID = scrapy.Field()
    About_Exhibitors = scrapy.Field()
    Brands_Name = scrapy.Field()