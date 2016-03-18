# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinestSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Blogger_Urls = scrapy.Field()
    Blogger_Name = scrapy.Field()
    Profile_Info = scrapy.Field()
    Blogger_Email = scrapy.Field()
    # pass
