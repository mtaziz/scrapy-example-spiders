# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LawsocietyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Source_Urls = scrapy.Field()
    Name = scrapy.Field()
    Solicitor_Title = scrapy.Field()
    SRA_ID = scrapy.Field()
    SRA_Status = scrapy.Field()
    Association_At = scrapy.Field()
    Telephone = scrapy.Field()
    Email = scrapy.Field()
    Practice_Area = scrapy.Field()
    Language_Spoken = scrapy.Field()  