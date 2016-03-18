# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from scrapy import signals
from scrapy.exporters import CsvItemExporter, XmlItemExporter
from scrapy import signals, Field
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
from yellopages.exporters import YellowpagesItemExporter
from unidecode import unidecode
import jsonfrom scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import logging
from urlparse import urlparse
import re
import time
import os
reload(sys)
sys.setdefaultencoding('utf8')



class YellowpagesPipeline(object):
    def process_item(self, item, spider):
        return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class RealstateMonthlyPipeline(object):
#     def process_item(self, item, spider):
#         return item
#     EXPORT_PATH = os.getenv("HOME")

#     def __init__(self):
#         self.files = {}
#     @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline
# # @spider_opened_working
#     def spider_opened(self, spider):
#         export_dir = settings.get('EXPORT_PATH', '.')
#         t = time.strftime('%Y-%m-%d %H-%M-%S GMT+6', time.gmtime(time.time() + 6*3600))
#         path = os.path.join(export_dir, '%s.csv' % t)
#         self.files = open(path, 'w+b')
#         self.exporter = CSVRealstateItemExporter(self.files)
#         self.exporter.start_exporting()
#         # self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         self.files.close()

# class CSVPipeline(object):
#     @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline

#     def spider_opened(self, spider):
#         if spider.name in 'realestate':
#             self.file = open('current_listing.csv', 'w+b')
#         else:
#             self.file = open('past_listing.csv', 'w+b')
#         self.exporter = CsvItemExporter(self.file)
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item