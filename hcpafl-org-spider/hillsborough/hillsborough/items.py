# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field 


class HillsboroughItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = Field()
    Company_Name = Field()
    Mailing_Address = Field()
