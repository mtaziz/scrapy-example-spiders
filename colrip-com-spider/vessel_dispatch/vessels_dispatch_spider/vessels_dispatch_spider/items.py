# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class VesselsDispatchSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Vessel_Arrivals_Name = Field()
    V_Vessel = Field()
    V_From = Field()
    V_To = Field()
    V_Time = Field()
    V_Tug = Field()
    V_LOA = Field()
    pass
