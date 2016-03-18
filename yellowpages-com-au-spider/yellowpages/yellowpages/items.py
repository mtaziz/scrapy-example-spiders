# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field 


class YellowpagesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = Field()
    Company_Name = Field()
    Service_Type = Field()
    Service_Description = Field()
    Phone_No = Field()
    Email = Field()
    Company_Website = Field()
    # Practice_Area = scrapy.Field()
    # Language_Spoken = scrapy.Field()  