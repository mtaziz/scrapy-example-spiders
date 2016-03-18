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
from hillsborough.exporters import HillsboroughItemExporter
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



class HillsboroughPipeline(object):
    def process_item(self, item, spider):
        return item

