# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_url = scrapy.Field()
    store_url = scrapy.Field()
    store_name = scrapy.Field()
    city = scrapy.Field()
    administrative_region = scrapy.Field()
    country = scrapy.Field()
    phone_no = scrapy.Field()

    pass
