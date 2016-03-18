# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NcbtmbSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Vessel_Arrivals_Name = Field()
    Name = Field()
    City = Field()
    State = Field()
    Zip = Field()
    Phone = Field()
    Email = Field()
    Yes_No = Field()
    pass
