# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LisvirginiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Bill Number    Example:  HB234  
    Source_Urls = scrapy.Field()
    Bill_Number = scrapy.Field()
    Bill_Title = scrapy.Field()
    Author = scrapy.Field()
    Summary = scrapy.Field()
    pass
