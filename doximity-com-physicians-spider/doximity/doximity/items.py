# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoximityItem(scrapy.Item):
    urls = scrapy.Field()
    name = scrapy.Field()
    office_address = scrapy.Field()
    speciality = scrapy.Field()
    profile_summary = scrapy.Field()
    
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
# item['office_address'] = office_address_data
#         item['speciality'] = speciality_data
#         item['profile_summary'] = summary