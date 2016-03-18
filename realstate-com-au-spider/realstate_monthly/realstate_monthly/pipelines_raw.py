# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals, Field
from scrapy.conf import settings
from realstate_monthly.exporters import CSVRealstateItemExporter
from unidecode import unidecode
import time, os

class RealstateMonthlyPipeline(object):
    def process_item(self, item, spider):
        return item
# class CafelandPipeline(object):
#     def process_item(self, item, spider):
#         for field in ['name','updated_time','particulars']:
#             item[field] = [val.strip(' \t\n\r') for val in item[field]]
#             item[field] = [val for val in item[field] if val]

#         pars = item['particulars']
#         for i in range(0, len(pars), 2):
#             if i+1 < len(pars):
#                 new_field, new_val = (unidecode(pars[i]).strip(' \t\n\r'), pars[i+1].strip(' \t\n\r:'))               
#             else:
#                 new_field, new_val = (unidecode(pars[i]).strip(' \t\n\r'), '')
#             item.fields[new_field] = Field()
#             item[new_field] = new_val

#             if i+1 < len(pars):
#                 pars[i] = pars[i] + pars[i+1]
#                 pars[i+1] = ''
#         item['particulars'] = [p for p in pars if p]

#         item['updated_time'] = [val[11:] for val in item['updated_time']]

#         self.exporter.export_item(item)
#         return item

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        export_dir = settings.get('EXPORT_DIR', '.')
        t = time.strftime('%Y-%m-%d %H-%M-%S GMT+6', time.gmtime(time.time() + 6*3600))
        path = os.path.join(export_dir, '%s.csv' % t)
        self.file = open(path, 'w+b')
        self.exporter = CSVRealstateItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()



import os
import sys

from scrapy import signals
from scrapy.exporters import CsvItemExporter, XmlItemExporter

class CrawlerPipeline(object):
    EXPORT_PATH = os.getenv("HOME")

    def __init__(self):
        self.files = {}


    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def spider_opened(self, spider):
        path = CrawlerPipeline.EXPORT_PATH + "/" + spider.spider_id + '_export.csv'
        export_file = open(path, 'ab' if os.path.isfile(path) else 'wb')
        self.files[spider.spider_id] = export_file
        self.exporter = CsvItemExporter(export_file)
        self.exporter.fields_to_export = [
            "item_id", "url", "num_links", "num_images", 
            "num_scripts", "num_styles", "headers", "text"
        ]
        self.exporter.start_exporting()


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        export_file = self.files.pop(spider.spider_id)
        export_file.close()


    def process_item(self, item, spider):
        # This is a common path among ALL crawlers
        self.exporter.export_item(item)
        return item

# class XmlExportPipeline(object):

#     def __init__(self):
#         self.files = {}

#      @classmethod
#      def from_crawler(cls, crawler):
#          pipeline = cls()
#          crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#          crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#          return pipeline

#     def spider_opened(self, spider):
#         file = open('%s_products.xml' % spider.name, 'w+b')
#         self.files[spider] = file
#         self.exporter = XmlItemExporter(file)
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         file = self.files.pop(spider)
#         file.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
# import scrapy

# def serialize_price(value):
#     return '$ %s' % str(value)

# class Product(scrapy.Item):
#     name = scrapy.Field()
#     price = scrapy.Field(serializer=serialize_price)

#      @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline

#     def spider_opened(self, spider):
#         export_dir = settings.get('EXPORT_DIR', '.')
#         t = time.strftime('%Y-%m-%d %H-%M-%S GMT+7', time.gmtime(time.time() + 7*3600))
#         path = os.path.join(export_dir, '%s.csv' % t)
#         self.file = open(path, 'w+b')
#         self.exporter = CSVItemExporter(self.file)
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()

