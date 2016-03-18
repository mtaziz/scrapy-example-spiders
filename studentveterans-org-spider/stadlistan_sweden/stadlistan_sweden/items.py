# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StadlistanSwedenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = scrapy.Field()
    Company_Name = scrapy.Field()
    Company_Website = scrapy.Field()
    Email = scrapy.Field()
    pass
