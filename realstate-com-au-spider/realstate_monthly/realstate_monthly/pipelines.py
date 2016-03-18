# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
from scrapy import signals
from scrapy.exporters import CsvItemExporter, XmlItemExporter
from scrapy import signals, Field
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
from realstate_monthly.exporters import CSVRealstateItemExporter
from unidecode import unidecode
import json
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import logging
from urlparse import urlparse
import re
import time
reload(sys)
sys.setdefaultencoding('utf8')

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
    EXPORT_PATH = os.getenv("HOME")

    def __init__(self):
        self.files = {}
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
# @spider_opened_working
    def spider_opened(self, spider):
        export_dir = settings.get('EXPORT_PATH', '.')
        t = time.strftime('%Y-%m-%d %H-%M-%S GMT+6', time.gmtime(time.time() + 6*3600))
        path = os.path.join(export_dir, '%s.csv' % t)
        self.files = open(path, 'w+b')
        self.exporter = CSVRealstateItemExporter(self.files)
        self.exporter.start_exporting()
# End}}}
    # def spider_opened(self, spider):
    #     # self.file = open('%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H")), 'w+')
    #     path = RealstateMonthlyPipeline.EXPORT_PATH + "/" + spider.name + '_export.csv'
    #     export_file = open(path, 'ab' if os.path.isfile(path) else 'wb')
    #     self.files[spider.name] = export_file
    #     # self.exporter = CsvRealstateItemExporter(self.file)
    #     self.exporter = CSVRealstateItemExporter(self.files)
#         self.exporter.fields_to_export = ['links', 'title', 'subur_name', 'unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may', 
# 'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov', 
# 'unit_mly_dec', 'unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 
# 'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 
# 'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec', 'unit_mly_nos_jan', 
# 'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun', 
# 'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec',
# ]
        self.exporter.start_exporting()

    # def spider_opened(self, spider):
    #     if spider.name in 'realestate':
    #         self.file = open('current_listing.csv', 'w+b')
    #     else:
    #         self.file = open('past_listing.csv', 'w+b')
    #     self.exporter = CsvItemExporter(self.file)
    #     self.exporter.start_exporting()


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.files.close()



# class DumpScrapedData(object):
#     """
#     Dump scraped data into flat file and log it into load_audit metadata.
#     # Could also be done by Feed-Exporters with no extra-code (scrapy crawl spider_name -o output.csv -t csv)
#     # but is less integrated with the code base (output setting must be redefined...)

#     """

#     def __init__(self):
#         self.files = {}
#         self.audit = {}
#         self.counter = 0

#     @classmethod
#     def from_crawler(cls, crawler):
#         pipeline = cls()
#         # TODO: is this needed to do somekind of registration of spider_closed/opened event?
#         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline


#     def spider_opened(self, spider):
#         filename = self.get_dump_filename(spider)
#         f = open(config.SCRAPED_OUTPUT_DIR + filename, 'w')
#         self.files[spider.name] = f
#         self.exporter = CsvItemExporter(f, include_headers_line=True, delimiter='|')
#         # audit record must have correct period (used for filtering when loading staging.reviews)
#         step = "Dump file: " + filename
#         audit_id = service.insert_auditing(job=DumpScrapedData.__name__,
#                                            step=step,
#                                            begin=spider.begin_period,
#                                            end=spider.end_period)
#         self.audit[spider.name] = audit_id
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         f = self.files.pop(spider.name)
#         f.close()
#         service.update_auditing(commit=True,
#                                 rows=self.counter,
#                                 status="Completed",
#                                 id=self.audit[spider.name])


#     def process_item(self, item, spider):
#         item['load_audit_id'] = self.audit[spider.name]
#         self.exporter.export_item(item)
#         self.counter += 1
#         return item

#     def update_audit(self, nb_rows, audit_id):
#         service.update_auditing(rows=nb_rows, status="Completed", id=audit_id)

#     def get_dump_filename(self, spider):
#         return "ReviewOf" + spider.name + '_' + \
#                utils.get_period_text(spider.begin_period, spider.end_period) + '.dat'



# class OldIdeaToLoadDB(object):

#     def insert_data(self, item, insert_sql):
#         keys = item.fields.keys()
#         fields = ','.join(keys)
#         params = ','.join(['%s'] * len(keys))
#         sql = insert_sql % (fields, params)

#         # TODO:
#         # add technical field (TODO: checkout the AsIS('paramvale') for the now())
#         # keys['loading_dts'] = 'now()'

#         # missing scraped value should return None (result in inserting Null)
#         values = [item.get(k, None) for k in keys]

#         self.db_conn.execute(sql, values)

#     def open_spider(self, spider):
#         pass

#     def close_spider(self, spider):
#         # commit once spider has finished scraping
#         self.db_conn.commit()


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

# class JsonExportPipeline(object):

#     def __init__(self):
#         log.start()
#         dispatcher.connect(self.spider_opened, signals.spider_opened)
#         dispatcher.connect(self.spider_closed, signals.spider_closed)
#         self.fjsons = {}

#     def spider_opened(self, spider):
#         fjson = open('output/%s_%s_items.json' % (spider.name, str(int(time.mktime(time.gmtime())))), 'wb')
#         self.fjsons[spider] = fjson
#         self.exporter = JsonItemExporter(fjson)
#         self.exporter.start_exporting()

#     def spider_closed(self, spider):
#         self.exporter.finish_exporting()
#         fjson = self.fjsons.pop(spider)
#         fjson.close()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
class CSVPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        if spider.name in 'realestate':
            self.file = open('current_listing.csv', 'w+b')
        else:
            self.file = open('past_listing.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        return item
# from scrapy.contrib.pipeline.images import ImagesPipeline
# from scrapy import Request


# class ImagePipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         yield Request(item['product_image'])

#     def item_completed(self, results, item, info):
#         images = [x for ok, x in results if ok]
#         if images:
#             image = images[0]
#             path = image['path'].split('/')[-1]
#             item['product_image'] = path
#         return item
