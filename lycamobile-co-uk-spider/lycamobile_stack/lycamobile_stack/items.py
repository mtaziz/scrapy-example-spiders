# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LycamobileSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Bundles = scrapy.Field()
    Type = scrapy.Field()
    Price_GBP = scrapy.Field()
    Validity_Days = scrapy.Field()
    Data = scrapy.Field()
    Natl_Mins = scrapy.Field()
    Natl_Text = scrapy.Field()
    Intl_Mins = scrapy.Field()
    Combined_Natl_Intl = scrapy.Field()
    Lyca_To_Lyca_Calls = scrapy.Field()
    Lyca_To_Lyca_Texts = scrapy.Field()
    Notes = scrapy.Field()
    pass