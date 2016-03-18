from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from scrapy.xlib.pydispatch import dispatcher


class IettPipeline(object):
    def process_item(self, item, spider):
        return item

def item_type(item):
    return type(item).__name__.replace('Item','').lower()  # TeamItem => team

class MultiCSVItemPipeline(object):
    SaveTypes = ['stop', 'linedetail']
    def __init__(self):
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_opened(self, spider):
        self.files = dict([ (name, open("output/" + name+'.csv','w+b')) for name in self.SaveTypes ])
        self.exporters = dict([ (name,CsvItemExporter(self.files[name])) for name in self.SaveTypes])
        [e.start_exporting() for e in self.exporters.values()]

    def spider_closed(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def process_item(self, item, spider):
        what = item_type(item)
        if what in set(self.SaveTypes):
            self.exporters[what].export_item(item)
        return item
Status API Training Shop Blog About Pricing

#________________End________________
# -*- coding: utf-8 -*-
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
#______________End________
#
import sys, MySQLdb, hashlib, re
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MetrosCubicosPipeline(object):

	def __init__(self):

		self.conn = MySQLdb.connect(user='root', passwd='toor', db='pyScraper', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def getInteger(self, intStr):

		intStr = re.sub("[^0123456789-]", '', intStr)

		if intStr:
			return int(intStr)		
		else:
			return None		

	def getCoordinate(self, floatStr):

		floatStr = re.sub("[^0123456789\.-]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None							

	def getFloat(self, floatStr):

		floatStr = re.sub("[^0123456789\.]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None			

	def process_item(self, item, spider): 

	    try:

	        self.cursor.execute("""INSERT INTO metrosCubicos VALUES (

				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
				%s, %s, %s, %s, %s
				        	
	        	)""", (

	        	item['MC_Listing_URL'].encode('utf-8'),
	        	item['MC_Ad_Code'].encode('utf-8'),	        	

	        	item['MC_Title'].encode('utf-8'),
	        	item['MC_Description'].encode('utf-8'),	        		        	

				item['MC_Categoria_de_inmueble'].encode('utf-8'),
				item['MC_Tipo_de_inmueble'].encode('utf-8'),

				item['MC_Estado'].encode('utf-8'),
				item['MC_Municipio'].encode('utf-8'),
				item['MC_Colonia'].encode('utf-8'),
				item['MC_Calle_avenida'].encode('utf-8'),

				item['MC_Photo_1'].encode('utf-8'),
				item['MC_Photo_2'].encode('utf-8'),
				item['MC_Photo_3'].encode('utf-8'),
				item['MC_Photo_4'].encode('utf-8'),
				item['MC_Photo_5'].encode('utf-8'),
				item['MC_Photo_6'].encode('utf-8'),
				item['MC_Photo_7'].encode('utf-8'),
				item['MC_Photo_8'].encode('utf-8'),
				item['MC_Photo_9'].encode('utf-8'),
				item['MC_Photo_10'].encode('utf-8'),
				item['MC_Video'].encode('utf-8'),

				self.getCoordinate(item['MC_Latitude']),
				self.getCoordinate(item['MC_Longitude']),

				item['MC_Telephone'].encode('utf-8'),

				self.getFloat(item['MC_Metros_cuadrados_de_construccion']),
				self.getInteger(item['MC_Numero_de_recamaras']),
				self.getFloat(item['MC_Numero_de_banos']),
				self.getInteger(item['MC_Numero_de_espacios_para_autos']),
				self.getFloat(item['MC_Edad']),
				self.getInteger(item['MC_Nivel_en_el_que_se_encuentra']),
				item['MC_Ubicacion_cuarto_de_servicio'].encode('utf-8'),
				item['MC_Indiviso'].encode('utf-8'),
				item['MC_Linea_telefonica'].encode('utf-8'),
				self.getInteger(item['MC_Numero_de_departamentos']),
				item['MC_Cuota_de_mantenimiento'].encode('utf-8'),
				item['MC_Clave_interna'].encode('utf-8'),
				item['MC_Gas_Natural'].encode('utf-8'),
				item['MC_Amueblado'].encode('utf-8'),

				item['MC_Estudio'],
				item['MC_Cisterna'],
				item['MC_Aire_acondicionado'],
				item['MC_Jacuzzi'],
				item['MC_Escuelas_cercanas'],
				item['MC_Alberca'],
				item['MC_Zona_arbolada'],
				item['MC_Cocina_integral'],
				item['MC_Chimenea'],
				item['MC_Vigilancia_privada'],
				item['MC_Accesos'],
				item['MC_Casa_de_veraneo'],
				item['MC_Parques_cercanos'],
				item['MC_Vista_panoramica'],
				item['MC_Calefaccion'],
				item['MC_Gimnasios_cercanos'],
				item['MC_Metros_cuadrados_de_jardin'],
				item['MC_No_se_admiten_ninos'],
				item['MC_No_se_admiten_animales'],
				item['MC_Solo_familias'],
				item['MC_Para_ejecutivos'],

				item['MC_Precio_de_venta'],
				self.getFloat(item['MC_Monto_Precio_de_venta']),
				item['MC_Moneda_Precio_de_venta'].encode('utf-8'),
				item['MC_Concepto_precio_de_venta'].encode('utf-8'),

				item['MC_Precio_de_renta'],
				self.getFloat(item['MC_Monto_Precio_de_renta']),
				item['MC_Moneda_Precio_de_renta'].encode('utf-8'),
				item['MC_Concepto_precio_de_renta'].encode('utf-8'),

				item['MC_Renta_vacacional'],

				item['MC_Renta_vacacional_mensual'],
				self.getFloat(item['MC_Monto_Precio_de_renta_vacacional_mensual']),
				item['MC_Moneda_Precio_de_renta_vacacional_mensual'].encode('utf-8'),

				item['MC_Renta_vacacional_semanal'],
				self.getFloat(item['MC_Monto_Precio_de_renta_vacacional_semanal']),
				item['MC_Moneda_Precio_de_renta_vacacional_semanal'].encode('utf-8'),

				item['MC_Renta_vacacional_fin_de_semana'],
				self.getFloat(item['MC_Monto_Precio_de_renta_vacacional_fin_de_semana']),
				item['MC_Moneda_Precio_de_renta_vacacional_fin_de_semana'].encode('utf-8'),

				item['MC_Renta_vacacional_diaria'],
				self.getFloat(item['MC_Monto_Precio_de_renta_vacacional_diaria']),
				item['MC_Moneda_Precio_de_renta_vacacional_diaria'].encode('utf-8')	        	

	        ))

	        self.conn.commit()

	    except MySQLdb.Error, e:
	        print "Error %d: %s" % (e.args[0], e.args[1])	       
	        return item
#_____________End________
## -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
from requests.exceptions import ConnectionError
from scrapy.exceptions import DropItem
from GephiStreamer import Node, Edge, GephiStreamerManager


logger = logging.getLogger(__name__)


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['publication_number'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['publication_number'])
            return item


class GephiPipeline(object):

    def __init__(self, gephi_uri, gephi_ws):
        self.gephi_uri = gephi_uri
        self.gephi_ws = gephi_ws
        self.nodes = set()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            gephi_uri=crawler.settings.get('GEPHI_URI'),
            gephi_ws=crawler.settings.get('GEPHI_WS')
        )

    def open_spider(self, spider):
        self.gephi = GephiStreamerManager(iGephiUrl=self.gephi_uri, iGephiWorkspace=self.gephi_ws)
        logger.info('GephiStream connected %s', self.gephi)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        patent_args = {'size': 5, 'red': 1, 'green': 0, 'blue': 0}
        patent_node = Node(item['publication_number'], **patent_args)
        patent_node.property['type'] = 'patent'
        patent_node.property['title'] = item.get('title')
        patent_node.property['filing_date'] = item.get('filing_date')
        patent_node.property['publication_date'] = item.get('publication_date')
        patent_node.property['priority_date'] = item.get('priority_date')
        patent_node.property['grant_date'] = item.get('grant_date')
        patent_node.property['pdf'] = item.get('pdf')
        if item['publication_number'] in self.nodes:
            self.gephi.change_node(patent_node)
        else:
            self.gephi.add_node(patent_node)

        link_args = {'size': 5, 'red': 0, 'green': 0, 'blue': 1}
        for citation in item.get('citations', []):
            citation_node = Node(citation, **link_args)
            citation_node.property['type'] = 'link'
            self.gephi.add_node(citation_node)
            self.gephi.add_edge(Edge(patent_node, citation_node, True))
            self.nodes.add(citation)

        for cited_by in item.get('cited_by', []):
            cited_by_node = Node(cited_by, **link_args)
            cited_by_node.property['type'] = 'link'
            self.gephi.add_node(cited_by_node)
            self.gephi.add_edge(Edge(cited_by_node, patent_node, True))
            self.nodes.add(cited_by)

        entity_args = {'size': 5, 'red': 0, 'green': 1, 'blue': 0}
        entities = set(item.get('inventors', []) + item.get('assignees', []))
        for entity in entities:
            entity_node = Node(entity, **entity_args)
            entity_node.property['type'] = 'entity'
            self.gephi.add_node(entity_node)
            self.gephi.add_edge(Edge(entity_node, patent_node, True))

        try:
            self.gephi.commit()
        except ConnectionError, e:
            logger.error(e)

        self.nodes.add(item['publication_number'])
        return item


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection_name = spider.name
        if self.collection_name in self.db.collection_names():
            self.db[self.collection_name].drop()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
        # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class MyhomePipeline(object):
    def process_item(self, item, spider):
        return item

# 验证数据
from scrapy.exceptions import DropItem
class PricePipeline(object):
# 	"""docstring for PricePipeline"""
# 	# vat_factor=1.5
	def process_item(self, item, spider):
# 		# if item['deposit']:
# 		# 	if item['price-excludes-vat']:
# 		# 	item['deposit'] *= self.vat_factor
		return item
		# else:
		# 	raise DropItem('Missing deposit in %s' % item)


# 写Json文件
import json
class JsonWriterPipeline(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.file = open('items3.jl','wb')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line)
		return item

# 检查重复
# from scrapy.exceptions import DropItem
# class DuplicatesPipeline(object):
# 	"""docstring for Duplicate"""
# 	def __init__(self):
# 		self.urls_seen = set()
# 	def process_item(self, item, spider):
# 		if item['url'] in self.urls_seen:
# 			raise DropItem("Duplicate item found: %s" % item)
# 		else:
# 			self.urls_seen.add(item['url'])
# 			return item


# Write items to SQLite
class SqlitePipeline(object):
	filename='data.db'

	def __init__(self):
		self.conn = None
		dispatcher.connect(self.initialize, signals.engine_started)
		dispatcher.connect(self.finalize, signals.engine_stopped)

	def process_item(self,item,spider):
		self.conn.execute("insert into Myhome values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
		                  (item['url'],item['address'],
		                  item['rentPrice'],item['currencyCode'],item['deposit'],
		               	  item['leaseTerm'],item['addedOnDate'],item['beds'],
		               	  item['description'],item['negotiator'],item['agentName'],
		               	  item['agentAddress'],item['agentPhone'],item['agentFax'],
		               	  item['agentLicence'],item['latitude'],item['longitude'],
		               	  item['ber'],item['ber_detail'],item['features'],
		               	  item['image_urls'],item['landlordPhone'],item['shortLink'],
		               	  item['services_in_this_area']))
		return item

	def initialize(self):
		if path.exists(self.filename):
			self.conn = sqlite3.connect(self.filename)
		else:
			self.conn = self.create_table(self.filename)

	def finalize(self):
		if self.conn is not None:
			self.conn.commit()
			self.conn.close()
			self.conn = None

	def create_table(self,filename):
		conn = sqlite3.connect(filename)
		conn.execute('''create table Myhome
					(url string primary key, address string, 
					 rentPrice decimal, currencyCode unicode, 
					 deposit decimal, leaseTerm string, 
					 addedOnDate string, beds integer, 
					 description string, negotiator string, 
					 agentName string, agentAddress string, 
					 agentPhone string, agentFax string, 
					 agentLicence string, latitude decimal, 
					 longitude decimal, ber string, ber_detail string, 
					 features string, image_urls string, 
					 landlordPhone string, shortLink string, 
					 services_in_this_area string)''')
		# conn.execute('SELECT * FROM Myhome')
		conn.commit()
		return conn


# Write items to MongoDB
# import pymongo

# class MongoPipeline(object):
# 	"""docstring for  """
# 	def __init__(self, mongo_uri, mongo_db):
# 		self.mongo_uri = mongo_uri
# 		self.mongo_db = mongo_db

# 	@classmethod
# 	def from_crawler(cls, crawler):
# 		return cls(
# 			mongo_uri=crawler.settings.get('MONGO_URI'),
# 			mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
# 		)
	
# 	def open_spider(self, spider):
# 		self.client = pymongo.MongoClient(self.mongo_uri)
# 		self.db = self.client[self.mongo_db]

# 	def close_spider(self, spider):
# 		self.client.close()

# 	def process_item(self, item, spider):
# 		self.db[self.collecton_name].insert(dict(item))
# 		return item
		
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
import re
from meals.models import Stock, Recipe
import re
from bs4 import BeautifulSoup
from django.db.models import Q
from inflect import engine
from nltk import word_tokenize, pos_tag




class GoodFoodStockPipeline(object):

    def process_item(self, item, spider):
        if type(item) != dict:
            item.save()
            ritem = item
        else:
            ritem = item["item"]
            stock = item["stock"]
            ritem.save()

            recipe = Recipe.objects.get(title=ritem['title'])

            for value in stock:
                souped = BeautifulSoup(value['title'], "lxml")
                stock_text = souped.get_text()
                value = self.parse_stock_name(stock_text)
                if value is not None:
                    quantity, name, direction = value
                else:
                    return ritem
                name_list = name.split(" ")
                try:
                    model = Stock.objects.get(title=name)

                except:
                    try:
                        model = Stock.objects.filter(reduce(lambda x, y: x | y, [Q(name__contains=word) for word in name_list]))[0:1]
                    except:
                        model = Stock.objects.create(title=name)
                model['original'] = value['original']
                model.recipes.add(recipe)
                model.save()
        return ritem

    def parse_stock_name(self, stockname):
        p = engine()

        instruction_set = stockname.split(',')
        word_list = instruction_set[0].split(' ')
        index = 1
        categories_ignored = ['RB', 'TO']
        tokens = word_tokenize(instruction_set[0])
        tags = pos_tag(tokens)
        i=0
        while i < len(tags):
            if tags[i][1] in categories_ignored:
                index += 1
                i+= 1
            else:
                break

        quantity = word_list[index-1]
        disallowed = ['g', 'ml', 'x', 'kg', 'cups', 'cup', 'grams', 'can', 'tbsp', 'tsp', 'tbsps', 'tsps',
                 'small', 'bunch', 'piece', 'handful', 'pack', 'chopped', 'large', 'a', 'pinch',
                 'fresh', 'dried', 'heaped', 'thick', 'slices', 'slice', 'of', 'about']
        while index < len(word_list):
            if word_list[index] not in disallowed:
                break
            else:
                index+=1
        sentence = " ".join(word_list[index:])
        tokens = word_tokenize(sentence)
        categories = pos_tag(tokens)
        words = []
        for category in categories:
            if category[1] not in ['NNS', 'VBN', 'VBG']:
                words.append(category[0])
        word = " ".join(words)
        return quantity, word, None

    # def parse_stock_name(self, stockname):
    #     p = engine()
    #     souped = BeautifulSoup(stockname)
    #     stock_text = souped.get_text()
    #     words = stock_text.split(" ")
    #     indicator = 0
    #     quantity = words[indicator]
    #     pattern = re.compile('[0-9]+[a-z]*[A-Z]*')
    #     if pattern.findall(quantity):
    #         indicator = 1
    #     unit = ""
    #     units = ['g', 'ml', 'kg', 'cups', 'cup', 'grams', 'can', 'tbsp', 'tsp', 'tbsps', 'tsps',
    #              'small', 'bunch', 'piece', 'handful', 'pack', 'chopped', 'large', 'a', 'pinch',
    #              'fresh', 'dried', 'heaped', 'thick', 'slices', 'slice']
    #     words = [p.singular_noun(word) for word in words]
    #     while words[indicator] in units:
    #         unit += " "+words[indicator]
    #         indicator += 1
    #     remainder = " ".join(words[indicator:])
    #     instructions = remainder.split(",")
    #     item = instructions[0]
    #     direction = ",".join(instructions[1:])
    #
    #     return quantity, item, direction
#______________End________		
# -*- coding: utf-8 -*-
import os
import re
from urllib2 import urlopen
from datetime import datetime

import scrapy
from scrapy.exceptions import DropItem
from twisted.web import client

import pastebin.settings as s

class FilePipeline():
    '''downloads file specified in the file_url field and places it inside FILES_STORE directory'''

    def __init__(self):
        if os.path.exists(s.FILES_STORE):
            if not os.path.isdir(s.FILES_STORE):
                raise Exception('FILES_STORE is not a directory')
        else:
            os.mkdir(s.FILES_STORE)

    def process_item(self, item, spider):
        fname = self.get_filename(item, spider)
        fpath = os.path.join(s.FILES_STORE, fname)

        item['file_path'] = fpath

        d = client.downloadPage(item['file_url'], fpath)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)

        return d

        # urllib2 method
        # try:
        #     with open(fpath, 'w') as f:
        #         f.write(urlopen(item['file_url']).read())
        # except Exception as e:
        #     self._handle_error(e, item, spider)

        # return item

    def get_filename(self, item, spider):
        fname = item['file_url'].split('/')
        while not fname[-1]:
            fname.pop()
        return fname[-1]

    def _handle_error(self, failure, item, spider):
        item['file_path'] = 'Error occurred: %s' % failure
        spider.log('Fail to download %s:\n    %s' % (item['file_url'], failure), scrapy.log.WARNING)

class FileFilterPipeline():
    '''
    filters items based on the content of the acquired file specified in the file_path field
    fills "matches" field
    removes unmatched files
    '''

    def __init__(self):
        self.compiled = [re.compile(expr, re.I) for expr in s.REGEXES]

    def process_item(self, item, spider):
        if os.path.exists(item['file_path']):
            with open(item['file_path']) as f:
                raw_paste = f.read();

            item['matches'] = []

            for expr in self.compiled:
                if expr.search(raw_paste):
                    item['matches'].append(expr.pattern)

            if not item['matches']:
                os.remove(item['file_path'])
                raise DropItem('No matches')
            else:
                spider.log('Match: %s' % item['matches'], scrapy.log.INFO)

        return item

class TextToFilePipeline(FilePipeline):
    '''
    saves content of the "text" field to a file
    removes "text" field
    '''

    def process_item(self, item, spider):
        fname = self.get_filename(item, spider)
        fpath = os.path.join(s.FILES_STORE, fname)

        item['file_path'] = fpath

        try:
            with open(fpath, 'w') as f:
                f.write(item['text'].encode('UTF-8'))
        except Exception as e:
            spider.log('Fail to save text:\n    %s' % e, scrapy.log.WARNING)

        item.pop('text')

        return item

    def get_filename(self, item, spider):
        fname = item['url'].split('/')
        while not fname[-1]:
            fname.pop()
        return fname[-1]

class FilterPipeline():
    '''
    filters items based on the content of the "text" field
    fills "matches" field
    '''

    def __init__(self):
        self.compiled = [re.compile(expr, re.I) for expr in s.REGEXES]

    def process_item(self, item, spider):
        if not item['text']:
            return item

        item['matches'] = []

        for expr in self.compiled:
            if expr.search(item['text']):
                item['matches'].append(expr.pattern)

        if not item['matches']:
            raise DropItem('No matches')
        else:
            spider.log('Match: %s' % item['matches'], scrapy.log.INFO)

        return item
#__________________
#______________End
# -*- coding: utf-8 -*-

import sys, MySQLdb, hashlib, re
from scrapy.exceptions import DropItem
from scrapy.http import Request

class LamudiPipeline(object):

	def __init__(self):

		self.conn = MySQLdb.connect(user='root', passwd='baggio', db='pyScraper', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def getCorrectAdCode(self, aStr):

		aStr = re.sub("Clave del Inmueble Lamudi:", '', aStr)

		if aStr:
			return aStr.strip()
		else:
			return ''						

	def getInteger(self, intStr):

		intStr = re.sub("[^0123456789-]", '', intStr)

		if intStr:
			return int(intStr)		
		else:
			return None		

	def getCoordinate(self, floatStr):

		floatStr = re.sub("[^0123456789\.-]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None							

	def getFloat(self, floatStr):

		floatStr = re.sub("[^0123456789\.]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None			

	def process_item(self, newItem, spider): 

		if newItem['LM_Amueblado']:
			newItem['LM_Amueblado']=1
		else:						
			newItem['LM_Amueblado']=0														

		try:

			self.cursor.execute("""INSERT INTO lamudi VALUES (

				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s 
				        	
				)""", (

					newItem['LM_Listing_URL'].encode('utf-8'),
					self.getCorrectAdCode(newItem['LM_Ad_Code']).encode('utf-8'),

					newItem['LM_Agente'],
					newItem['LM_Tipo_de_inmueble'].encode('utf-8'),

					self.getFloat(newItem['LM_Superficie']),
					self.getInteger(newItem['LM_Recamaras']),
					self.getFloat(newItem['LM_Banos']),
					self.getInteger(newItem['LM_Nivel']),

					self.getInteger(newItem['LM_Plantas']),
					newItem['LM_Disponible_a_partir_de'].encode('utf-8'),
					newItem['LM_Conservacion'].encode('utf-8'),

					newItem['LM_Titulo'].encode('utf-8'),
					newItem['LM_Descripcion'].encode('utf-8'),

					self.getFloat(newItem['LM_Precio']),
					newItem['LM_Moneda'].encode('utf-8'),

					newItem['LM_Estado'].encode('utf-8'),
					newItem['LM_Municipio_o_Delegacion'].encode('utf-8'),
					newItem['LM_Colonia'].encode('utf-8'),
					
					newItem['LM_Nombre'].encode('utf-8'),
					newItem['LM_Telefono_de_la_oficina'].encode('utf-8'),
					newItem['LM_Telefono_movil'].encode('utf-8'),
					newItem['LM_Telefono_adicional_de_contacto'].encode('utf-8'),

					self.getInteger(newItem['LM_Construido_Ano']),
					self.getInteger(newItem['LM_Estacionamientos']),

					newItem['LM_Amueblado'],
					newItem['LM_Categoria'].encode('utf-8'),
					newItem['LM_Direccion'].encode('utf-8'),

					self.getCoordinate(newItem['LM_Latitude']),				
					self.getCoordinate(newItem['LM_Longitude']),											

					newItem['LM_Condiciones_de_precio'].encode('utf-8'),
					newItem['LM_Deposito_Aval'].encode('utf-8'),
					self.getFloat(newItem['LM_Mantenimiento']),
					self.getFloat(newItem['LM_Comision_del_agente']),

					newItem['LM_Photo_1'].encode('utf-8'),
					newItem['LM_Photo_2'].encode('utf-8'),
					newItem['LM_Photo_3'].encode('utf-8'),
					newItem['LM_Photo_4'].encode('utf-8'),
					newItem['LM_Photo_5'].encode('utf-8'),
					newItem['LM_Photo_6'].encode('utf-8'),
					newItem['LM_Photo_7'].encode('utf-8'),
					newItem['LM_Photo_8'].encode('utf-8'),
					newItem['LM_Photo_9'].encode('utf-8'),
					newItem['LM_Photo_10'].encode('utf-8')
			))

			self.conn.commit()

		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])	       
			return newItem
from scrapy import log

from twisted.internet.defer import inlineCallbacks, returnValue
from txmongo import MongoConnection, connection as mongo_connection
mongo_connection._Connection.noisy = False
from txmongo.filter import sort as mongosort, ASCENDING

from hcicrawler.urllru import url_to_lru_clean, has_prefix
from hcicrawler.resolver import ResolverAgent


class RemoveBody(object):

    def process_item(self, item, spider):
        item.pop('body', None)
        return item


class MongoOutput(object):

    def __init__(self, host, port, db, queue_col, page_col, jobid):
        store = MongoConnection(host, port)[db]
        self.jobid = jobid
        self.pageStore = store[page_col]
        self.queueStore = store[queue_col]
        self.queueStore.create_index(mongosort(ASCENDING('_job')))

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        db = crawler.settings['MONGO_DB']
        queue_col = crawler.settings['MONGO_QUEUE_COL']
        page_col = crawler.settings['MONGO_PAGESTORE_COL']
        jobid = crawler.settings['JOBID']
        return cls(host, port, db, queue_col, page_col, jobid)


class OutputQueue(MongoOutput):

    @inlineCallbacks
    def process_item(self, item, spider):
        d = dict(item)
        d['_job'] = self.jobid
        yield self.queueStore.insert(d, safe=True)
        returnValue(item)

class OutputStore(MongoOutput):

    @inlineCallbacks
    def process_item(self, item, spider):
        d = dict(item)
        d['_id'] = "%s/%s" % (item['lru'], item['size'])
        d['_job'] = self.jobid
        yield self.pageStore.update({'_id': d['_id']}, d, upsert=True, safe=True)
        returnValue(item)


class ResolveLinks(object):

    def __init__(self, proxy_host=None, proxy_port=None):
        self.proxy = None
        if proxy_host and proxy_port:
            self.proxy = {
              "host": proxy_host,
              "port": int(proxy_port)
            }

    @classmethod
    def from_crawler(cls, crawler):
        proxy = crawler.settings['PROXY']
        if proxy != "" and not proxy.startswith(':'):
            return cls(*proxy.split(":"))
        return cls()

    @inlineCallbacks
    def process_item(self, item, spider):
        lrulinks = []
        for url, lru in item["lrulinks"]:
            if self._should_resolve(lru, spider):
                if url in spider.resolved_links:
                    lru = spider.resolved_links[url]
                else:
                    try:
                        agent = ResolverAgent(proxy=self.proxy)
                        rurl = yield agent.resolve(url)
                        if rurl == url and has_prefix(lru, spider.discover_prefixes):
                            rurl = yield agent.resolve(url)
                        lru = url_to_lru_clean(rurl)
                        spider.resolved_links[url] = lru
                    except Exception, e:
                        spider.log("Error resolving redirects from URL %s: %s %s" % (url, type(e), e), log.INFO)
            lrulinks.append(lru)
        item["lrulinks"] = lrulinks
        returnValue(item)

    def _should_resolve(self, lru, spider):
        c1 = has_prefix(lru, spider.discover_prefixes)
        c2 = has_prefix(lru, spider.follow_prefixes)
        c3 = any((match in lru for match in ["url", "link", "redir", "target", "orig", "goto"]))
        return c1 or (c2 and c3)
#_________End______________#
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from norix.items import *
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import logging
import json
from bson import BSON
from bson import json_util

class PlayersPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]

    def process_item(self, item, spider):
        if not isinstance(item,PlayerItem):
            return item # return the item to let other pipeline to handle it
        db = self.db
        players = db['players']
        player_seminars = db['player_seminars__seminar_players']

        players.update(
            {
                'ssn': item['ssn']
            },
            {
                'ssn': item['ssn'],
                'player_name': item['player_name'],
                'email': item['email'],
                'phone': item['phone'],
                'status': item['status']            
            }, 
            upsert=True)
        
        
        player_seminars.insert_one(
            {
                'seminar_players': item['seminars'],
                'player_seminars': item['ssn']
            })        

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            #self.collection.insert(dict(item))
            #self.collection.findAndModify(dict(item), {'upsert':'true'});
            spider.logger.info("Player %s added to collection", item['player_name'])

        return item

class SeminarPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]
        
    def process_item(self, item, spider):
        if not isinstance(item,SeminarItem):
            return item # return the item to let other pipeline to handle it
        db = self.db
        seminar = db['seminars']
        #user_db = db['users']
        user_seminars = db['seminar_seminar_has_users__user_user_has_seminars']        

        seminar.update({'seminar_id': item['seminar_id']}, dict(item), upsert=True)
        
        #find_user = user_db.find({'username': spider.user, 'club': spider.club})
        
        #spider.logger.info(spider.user_obj['_id'])
        
        user_seminars.update({
            'user_user_has_seminars': spider.user_obj['_id'],            
            'seminar_seminar_has_users': item['seminar_id']
            },
            {
            'user_user_has_seminars': spider.user_obj['_id'],
            'seminar_seminar_has_users': item['seminar_id']
            },                        
            upsert=True) 
        
        
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            spider.logger.info("Seminar %s added to collection", item['seminar_name'])
            
        return item
#________________End________________#
# -*- coding: utf-8 -*-

import re
import json
import sys
from collections import defaultdict
from urlparse import urlparse
from traceback import format_exc
from pprint import pprint
from scrapy import log
from scrapy.exceptions import DropItem
from sitemapper.items import DirItem, PageItem


class DirBotPipeline(object):
    '''
    处理dirbot的pipeline
    '''

    def process_item(self, item, spider):
        '''处理item'''

        if not isinstance(item, DirItem):
            return item

        url = item['url']
        size = item['size']
        spider.site_tree.add_url(url)

        return item

    def close_spider(self, spider):
        '''关闭爬虫'''

        if spider.name == 'dirbot':
            try:
                sub_site_tree = spider.site_tree.split(1000)
                log.msg(sub_site_tree.pretty())
                sub_doc.save()
            except:
                pass
            log.msg(spider.site_tree.pretty())
            spider.site_tree.save()


class UrlBotPipeline(object):
    '''
    处理urlbot的pipeline
    '''

    def open_spider(self, spider):
        '''
        打开爬虫, 获取爬虫配置(是否save)
        '''

        self.save = hasattr(spider, 'save') and spider.save
        log.msg('Pipeline saves items: {}'.format(self.save), level=log.INFO)

    def process_item(self, item, spider):
        '''
        处理ITEM, 去除多余空格, 并保存
        '''

        if isinstance(item, PageItem):
            for k in item.fields:
                if k not in item:
                    item[k] = ['']
                item[k] = item[k][0]
                if hasattr(item[k], 'strip'):
                    item[k] = item[k].strip()
            if self.save_item(item):
                return item
            else:
                raise DropItem('drop item')
        else:
            return item

    def item_to_dict(self, item):
        '''
        ITEM转DICT, 过滤掉调试字段(以“_”开始)
        '''

        obj = {}
        for k, v in item.iteritems():
            if not k.startswith('_'):
                obj[k] = v
        return obj

    def save_item(self, item):
        '''
        调用接口, 保存ITEM
        若发生异常, 则打印警告信息
        '''

        if not self.save:
            return True

        try:
            from writeurltomongo.writemongo import WriteUrlToMongo
            o = self.item_to_dict(item)
            p = WriteUrlToMongo(o)
            ok = p.write_url_to_mongo()
            msg = u'{}: {}'.format(u'✓' if ok else u'✗', item)
            log.msg(msg, level=log.DEBUG)
            return True
        except:
            log.msg(format_exc(), level=log.WARNING)
            return False
#________________End________________
# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import time
import pymongo


class NewsCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
          # here we only check if the data is not null
          # but we could do any crazy validation we want
          if not data:
            valid = False
            raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
          self.collection.insert(dict(item))
          log.msg("Item wrote to MongoDB database %s/%s" %
                  (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                  level=log.DEBUG, spider=spider)
        return item


# ignore visited sites
class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(item['url'])
            return item

# export data into json
class JsonExportPipeline(object):

    def __init__(self):
        log.start()
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.fjsons = {}

    def spider_opened(self, spider):
        fjson = open('output/%s_%s_items.json' % (spider.name, str(int(time.mktime(time.gmtime())))), 'wb')
        self.fjsons[spider] = fjson
        self.exporter = JsonItemExporter(fjson)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        fjson = self.fjsons.pop(spider)
        fjson.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
  # Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from scrapy import log
from items import MyspaceprofileItem

class MyspacePipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):
    def __init__(self):
        import pymongo

        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        if self.__get_uniq_key() is not None:
            self.collection.create_index(self.__get_uniq_key(), unique=True)

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            self.collection.insert(dict(item))
        else:
            old_item = self.collection.find_one({"_id": item["_id"]})
            if type(item) is MyspaceprofileItem:
                print "Append profile for", item["_id"]
                for k in item:
                    old_item[k] = item[k]
                old_item["profile"] = True
            else:
                print "Append friend for", item["_id"]
                # old_item = self.collection.find_one({"_id": item["_id"]})

                #crawl infriends first,if _id exists, add outfriends to the item
                if old_item is not None:
                    #?
                    if item["outfriends"] == []:
                        old_item["outfriends"] = item["outfriends"]
                else:
                    old_item = dict(item)
            self.collection.update(
                {self.__get_uniq_key(): item[self.__get_uniq_key()]},
                old_item,
                upsert=True)
        log.msg("Item wrote to MongoDB database %s/%s" %
                (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                level=log.DEBUG, spider=spider)
        return item

    def __get_uniq_key(self):
        if not settings['MONGODB_UNIQ_KEY'] or settings['MONGODB_UNIQ_KEY'] == "":
            return None
        return settings['MONGODB_UNIQ_KEY']
# ________________End________________
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

from scrapy.exceptions import DropItem
import re


class JianshuPipeline(object):
    def process_item(self, item, spider):
        views = int(item['views_count'])
        comments = int(item['comments_count'])
        likes = int(item['likes_count'])
        # 三者按比例简单求和
        votes = views*2 + comments*3 + likes*5

        # wordnum = int(item['wordnum'])
        # followers_count = int(item['followers_count'])
        # total_likes_count = int(item['total_likes_count'])
        starttime = item['datetime']
        # 对文章编辑时间格式化
        parsedstarttime = self.timeparsed(starttime)
        # 对现在时间格式化
        now = datetime.now()
        pattern = '%Y-%m-%d %H:%M'
        nowpattern = now.strftime(pattern)
        parsednowpattern = self.timeparsed(nowpattern)
        totaldelta = parsednowpattern - parsedstarttime
        totalhours = totaldelta.seconds/3600 + 2

        # 公式是votes = （p-1）/(t+2)^1.8 的改版
        rank = (votes - 1)/(pow(totalhours, 1.8))
        item['rank'] = str(rank)
        # item['datetime'] = str(totalhours)
        # 这里rank具体大小，可根据抓取的结果继续优化
        if rank > 36:
            return item
        else:
            raise DropItem('Rank  less than 2', item)

    def timeparsed(self, time1):
        # 针对编辑时间中的‘*’
        # 如果文章是做过修改的，那么简书文章的时间会带有'*'标记，为与系统时间格式保持一致，这里对'*'用''做替换处理
        edittiempattern = re.compile(r'\*')
        datetimeresult = re.search(edittiempattern, time1)
        if datetimeresult:
            time1 = time1.replace('*', '')
        pattern = re.compile(r'\.')
        match = re.search(pattern, time1)
        if match:
            time1 = time1.replace('.', '-')
        pattern = '%Y-%m-%d %H:%M'
        timeparsed = datetime.strptime(time1, pattern)
        return timeparsed
#_________End______________
# -*- coding: utf-8 -*-

from scrapy import log
from webkit import items
import bson
import gridfs
import io
import json
import logging
import os.path
import pymongo
import redis


class WebkitPipeline(object):

    def __init__(self, mdb, rdb, key, tmp):

        self.cnn = mdb.connection
        self.mdb = mdb
        self.gfs = gridfs.GridFS(mdb)
        self.rdb = rdb
        self.key = key
        self.tmp = tmp

    @classmethod
    def from_crawler(cls, crawler):

        settings = crawler.settings

        host = settings.get('MONGO_HOST')
        port = settings.getint('MONGO_PORT')
        db = settings.get('MONGO_DB')
        mdb = pymongo.MongoClient(host=host, port=port)[db]

        host = settings.get('REDIS_HOST')
        port = settings.getint('REDIS_PORT')
        db = settings.getint('REDIS_DB')
        key = settings.get('REDIS_OKEY')
        rdb = redis.StrictRedis(host=host, port=port, db=db)

        tmp = settings.get('FILES_STORE')
        pipe = cls(mdb, rdb, key, tmp)
        return pipe

    def process_item(self, item, spider):

        if not isinstance(item, items.RenderItem):
            return item

        oid = bson.ObjectId(item['oid'])
        sid = bson.ObjectId()
        rid = bson.ObjectId()

        obj = item['obj']
        doc = {
            'time': item['time'],
            'source': sid,
            'render': rid,
        }

        log.msg('=== %s' % (oid,), level=log.INFO)

        self.mdb.page.update({'_id': oid}, {'$push': {'archives': doc}})

        self.save_gfs(sid, 'application/json', json.dumps(obj))

        path = os.path.join(self.tmp, item['files'][0]['path'])
        self.save_gfs(rid, 'image/jpeg', open(path, 'rb'))
        os.remove(path)

        self.rdb.lpush(self.key, '%s#%s#%s' % (oid, sid, rid))

        return item

    def save_gfs(self, id, type, buf):

        log.msg('+++ %s (%s)' % (id, type), level=log.INFO)

        req = self.cnn.start_request()
        gin = self.gfs.new_file(
            _id=id,
            filename=str(id),
            contentType=type
        )
        gin.write(buf)
        gin.close()
        req.end()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import logging
from urlparse import urlparse
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#class RatemdsDrMickeyPipeline(object):
	
	#def open_spider(self,spider):
	#	self.fd = open(spider.name+".txt",'w')
	#
	#def process_item(self, item, spider):
	#	line = ""
	#	for key in ['url', 'name_of_doctor', 'cumulative_rating', 'no_of_total_reviews', 'individual_review_comments','comments_submission_date', 'rating_by_commentors']:
	#		line += item.get(key,"") + '\t'
	#	line += '\n'
	#	self.fd.write(line.encode('utf-8'))
	#	return item
	#
	#def spider_closed(self, spider):
	#	self.fd.close()

#class WebPipeline(object):
class RatemdsDrMickeyPipeline(object):
	def open_spider(self, spider):
	#self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
		self.file = open('%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H")), 'w+')
	#self.file.write('name,food,openings\n')
		self.file.write('url, name_of_doctor, cumulative_rating, no_of_total_reviews, individual_review_comments,comments_submission_date, rating_by_commentors\n')

	def process_item(self, item, spider):
		self.file.write('"%s\n",' % (item['url'].encode('utf-8')))
		self.file.write('"%s"\n' % (item['name_of_doctor'].encode('utf-8')))
		self.file.write('"%s"\n' % (item['cumulative_rating'].encode('utf-8')))
		self.file.write('"%s"\n' % (item['no_of_total_reviews'].encode('utf-8')))
		self.file.write('"%s"\n' % (item['individual_review_comments']))
		self.file.write('"%s"\n' % (item['comments_submission_date']))
		self.file.write('"%s"\n' % (item['rating_by_commentors']))
		self.file.flush()
		return item
	def close_spider(self, spider):
		self.file.close()
#________________End________________
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
import shutil
import dateutil.parser


class JsonWithEncodingPipeline(object):

    def __init__(self):
        try:
            url_file = codecs.open('infocar_cars.json', 'r')
            shutil.copyfile('infocar_cars.json', 'infocar_cars_old.json')
            self.file = codecs.open('infocar_cars.json', 'w', encoding='utf-8')
        except Exception:
            self.file = codecs.open('infocar_cars.json', 'w', encoding='utf-8')


    def _set_odometer(self, item):
        odometer = item['odometer'].replace(u'тыс.км', '')
        if odometer.isdigit():
            item['odometer'] = int(odometer)*1000
        else:
            item['odometer'] = 0

    def _set_boolean_fields(self, item):
        fields = ['is_salon', 'sold', 'custom']
        for field in fields:
            if item.has_key(field):
                if item[field]:
                    item[field] = True
                else:
                    item[field] = False

    def _set_integer_fields(self, item):
        fields = ['doors', 'year', 'price_uah', 'price_usd', "ext_id", "user_ads"]
        for field in fields:
            if item.has_key(field):
                if item[field].isdigit():
                    item[field] = int(item[field])
                else:
                    item[field] = 0

    def process_item(self, item, spider):
        self._set_odometer(item)
        self._set_boolean_fields(item)
        self._set_integer_fields(item)
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()   
# ________________End________________
#!/usr/bin/python
#
# Copyright 2014 LeTV Inc. All Rights Reserved.
__author__ = 'guoxiaohe@letv.com'

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.settings import Settings

from url_filter import UrlFilter
from page_local_writer import PageDataWriter

class CrawlerPipeline(object):
  def __init__(self):
    self.spider_ = None
    self.url_filter_ = UrlFilter()
    dispatcher.connect(self.initialize, signals.engine_started)
    dispatcher.connect(self.finalize, signals.engine_stopped)
    self.data_dir = Settings().get('DATA_DIR', '/letv/crawler_delta/')
    self.crawled_items_ = 0
    self.up_log_time_ = 0

  def initialize(self):
    pass

  def finalize(self):
    pass

  def open_spider(self, spider):
    if not spider:
      raise Exception('faild load spider instance')
    self.spider_ = spider
    self.spider_.log("Crawler pipeline is ready", log.INFO)
    self.file_writer_ = PageDataWriter(self.spider_, 1800, 4000, self.data_dir)

  def close_spider(self, spider):
    print 'call pipeline close spider'
    spider.log('Pipeline close called...', log.INFO)
    self.file_writer_.finalize()

  def process_item(self, item, spider):
    if not item:
      return None
    self.file_writer_.add_item(item)
    self.crawled_items_ += 1
    spider.crawler.stats.inc_value('pipeline/write_pages', spider = spider)
    import time
    nowt = time.time()
    if nowt - self.up_log_time_ >= 60:
      self.spider_.log('crawled pages num[%d]' % self.crawled_items_)
      self.up_log_time_ = nowt
    return item
#________________End________________
#!/usr/bin/python
#
# Copyright 2014 LeTV Inc. All Rights Reserved.
__author__ = 'guoxiaohe@letv.com'

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.settings import Settings

from url_filter import UrlFilter
from page_local_writer import PageDataWriter

class CrawlerPipeline(object):
  def __init__(self):
    self.spider_ = None
    self.url_filter_ = UrlFilter()
    dispatcher.connect(self.initialize, signals.engine_started)
    dispatcher.connect(self.finalize, signals.engine_stopped)
    self.data_dir = Settings().get('DATA_DIR', '/letv/crawler_delta/')
    self.crawled_items_ = 0
    self.up_log_time_ = 0

  def initialize(self):
    pass

  def finalize(self):
    pass

  def open_spider(self, spider):
    if not spider:
      raise Exception('faild load spider instance')
    self.spider_ = spider
    self.spider_.log("Crawler pipeline is ready", log.INFO)
    self.file_writer_ = PageDataWriter(self.spider_, 1800, 4000, self.data_dir)

  def close_spider(self, spider):
    print 'call pipeline close spider'
    spider.log('Pipeline close called...', log.INFO)
    self.file_writer_.finalize()

  def process_item(self, item, spider):
    if not item:
      return None
    self.file_writer_.add_item(item)
    self.crawled_items_ += 1
    spider.crawler.stats.inc_value('pipeline/write_pages', spider = spider)
    import time
    nowt = time.time()
    if nowt - self.up_log_time_ >= 60:
      self.spider_.log('crawled pages num[%d]' % self.crawled_items_)
      self.up_log_time_ = nowt
    return item
#______________#!/usr/bin/python
#
# Copyright 2014 LeTV Inc. All Rights Reserved.
__author__ = 'guoxiaohe@letv.com'

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.settings import Settings

from url_filter import UrlFilter
from page_local_writer import PageDataWriter

class CrawlerPipeline(object):
  def __init__(self):
    self.spider_ = None
    self.url_filter_ = UrlFilter()
    dispatcher.connect(self.initialize, signals.engine_started)
    dispatcher.connect(self.finalize, signals.engine_stopped)
    self.data_dir = Settings().get('DATA_DIR', '/letv/crawler_delta/')
    self.crawled_items_ = 0
    self.up_log_time_ = 0

  def initialize(self):
    pass

  def finalize(self):
    pass

  def open_spider(self, spider):
    if not spider:
      raise Exception('faild load spider instance')
    self.spider_ = spider
    self.spider_.log("Crawler pipeline is ready", log.INFO)
    self.file_writer_ = PageDataWriter(self.spider_, 1800, 4000, self.data_dir)

  def close_spider(self, spider):
    print 'call pipeline close spider'
    spider.log('Pipeline close called...', log.INFO)
    self.file_writer_.finalize()

  def process_item(self, item, spider):
    if not item:
      return None
    self.file_writer_.add_item(item)
    self.crawled_items_ += 1
    spider.crawler.stats.inc_value('pipeline/write_pages', spider = spider)
    import time
    nowt = time.time()
    if nowt - self.up_log_time_ >= 60:
      self.spider_.log('crawled pages num[%d]' % self.crawled_items_)
      self.up_log_time_ = nowt
    return item
########
##!/usr/bin/python
#
# Copyright 2014 LeTV Inc. All Rights Reserved.
__author__ = 'guoxiaohe@letv.com'

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.settings import Settings

from url_filter import UrlFilter
from page_local_writer import PageDataWriter

class CrawlerPipeline(object):
  def __init__(self):
    self.spider_ = None
    self.url_filter_ = UrlFilter()
    dispatcher.connect(self.initialize, signals.engine_started)
    dispatcher.connect(self.finalize, signals.engine_stopped)
    self.data_dir = Settings().get('DATA_DIR', '/letv/crawler_delta/')
    self.crawled_items_ = 0
    self.up_log_time_ = 0

  def initialize(self):
    pass

  def finalize(self):
    pass

  def open_spider(self, spider):
    if not spider:
      raise Exception('faild load spider instance')
    self.spider_ = spider
    self.spider_.log("Crawler pipeline is ready", log.INFO)
    self.file_writer_ = PageDataWriter(self.spider_, 1800, 4000, self.data_dir)

  def close_spider(self, spider):
    print 'call pipeline close spider'
    spider.log('Pipeline close called...', log.INFO)
    self.file_writer_.finalize()

  def process_item(self, item, spider):
    if not item:
      return None
    self.file_writer_.add_item(item)
    self.crawled_items_ += 1
    spider.crawler.stats.inc_value('pipeline/write_pages', spider = spider)
    import time
    nowt = time.time()
    if nowt - self.up_log_time_ >= 60:
      self.spider_.log('crawled pages num[%d]' % self.crawled_items_)
      self.up_log_time_ = nowt
    return item
++++++++++++
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
from scrapy import log
from scrapy.exceptions import DropItem
import baidu

class BaiduPipeline(object):
 
    def open_spider(self,spider):

        M_SQLDB_CONF = spider.settings.get("M_SQLDB_CONF")
        assert M_SQLDB_CONF, "Please set SQL DATABASE conf in baidu/settings.py ! eg:M_SQLDB_CONF={'host':'localhost','port':3306,'user':'wangpan','passwd':'wangpan','db':'wangpan'}"
         
        self.dbpool = adbapi.ConnectionPool('MySQLdb',cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True,**M_SQLDB_CONF)
      
     
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        
        return item
 
    def _conditional_insert(self, tx, item):
        # create record if doesn't exist. 
        # all this block run on it's own thread
        #tx.execute("select * from baidu_user where uk = %s", (item['uk'], ))
        #result = tx.fetchone()
        
        sql=item.sql()
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
        if not sql:
            return
        #print "[SQL]",sql
        tx.execute(sql)
        
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
 
    def handle_error(self, e):
        #print "-----------",e
        log.err(e)
+++++++# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
from scrapy import log
from scrapy.exceptions import DropItem
import baidu

class BaiduPipeline(object):
 
    def open_spider(self,spider):

        M_SQLDB_CONF = spider.settings.get("M_SQLDB_CONF")
        assert M_SQLDB_CONF, "Please set SQL DATABASE conf in baidu/settings.py ! eg:M_SQLDB_CONF={'host':'localhost','port':3306,'user':'wangpan','passwd':'wangpan','db':'wangpan'}"
         
        self.dbpool = adbapi.ConnectionPool('MySQLdb',cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True,**M_SQLDB_CONF)
      
     
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        
        return item
 
    def _conditional_insert(self, tx, item):
        # create record if doesn't exist. 
        # all this block run on it's own thread
        #tx.execute("select * from baidu_user where uk = %s", (item['uk'], ))
        #result = tx.fetchone()
        
        sql=item.sql()
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
        if not sql:
            return
        #print "[SQL]",sql
        tx.execute(sql)
        
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
 
    def handle_error(self, e):
        #print "-----------",e
        log.err(e)
++++++++
# -*- coding: utf-8 -*-

# Define your item pipelines here

import json
import datetime as dt
import time

import logging

from kafka import KafkaClient, SimpleProducer

from crawling.items import RawResponseItem

class KafkaPipeline(object):

    """Pushes serialized item to appropriate Kafka topics."""

    def __init__(self, producer, topic_prefix, aKafka):
        self.producer = producer
        self.topic_prefix = topic_prefix
        self.topic_list = []
        self.kafka = aKafka

    @classmethod
    def from_settings(cls, settings):
        kafka = KafkaClient(settings['KAFKA_HOSTS'])
        producer = SimpleProducer(kafka)
        topic_prefix = settings['KAFKA_TOPIC_PREFIX']
        return cls(producer, topic_prefix, kafka)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        datum = dict(item)
        datum["timestamp"] = dt.datetime.utcnow().isoformat()
        prefix = self.topic_prefix
        appid_topic = "{prefix}.crawled_{appid}".format(prefix=prefix,
                                                       appid=datum["appid"])
        firehose_topic = "{prefix}.crawled_firehose".format(prefix=prefix)
        try:
            message = json.dumps(datum)
        except:
            message = 'json failed to parse'

        self.checkTopic(appid_topic)
        self.checkTopic(firehose_topic)

        self.producer.send_messages(appid_topic, message)
        self.producer.send_messages(firehose_topic, message)

        return item

    def checkTopic(self, topicName):
        if topicName not in self.topic_list:
            self.kafka.ensure_topic_exists(topicName)
            self.topic_list.append(topicName)	
#________________End________________
## -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
from scrapy import log
from scrapy.exceptions import DropItem


class CnblogsPipeline(object):
 
    def open_spider(self,spider):

        M_SQLDB_CONF = spider.settings.get("M_SQLDB_CONF")
        assert M_SQLDB_CONF, "Please set SQL DATABASE conf in baidu/settings.py ! eg:M_SQLDB_CONF={'host':'localhost','port':3306,'user':'wangpan','passwd':'wangpan','db':'wangpan'}"
         
        self.dbpool = adbapi.ConnectionPool('MySQLdb',cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True,**M_SQLDB_CONF)
      
     
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        
        return item
 
    def _conditional_insert(self, tx, item):
        # create record if doesn't exist. 
        # all this block run on it's own thread
        #tx.execute("select * from baidu_user where uk = %s", (item['uk'], ))
        #result = tx.fetchone()
        
        sql=item.sql()
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
        if not sql:
            return
        #print "[SQL]",sql
        tx.execute(sql)
        
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
 
    def handle_error(self, e):
        #print "-----------",e
        log.err(e)
+++++++
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
from scrapy import log
from scrapy.exceptions import DropItem


class CsdnPipeline(object):
 
    def open_spider(self,spider):

        M_SQLDB_CONF = spider.settings.get("M_SQLDB_CONF")
        assert M_SQLDB_CONF, "Please set SQL DATABASE conf in baidu/settings.py ! eg:M_SQLDB_CONF={'host':'localhost','port':3306,'user':'wangpan','passwd':'wangpan','db':'wangpan'}"
         
        self.dbpool = adbapi.ConnectionPool('MySQLdb',cursorclass=MySQLdb.cursors.DictCursor,
                use_unicode=True,**M_SQLDB_CONF)
      
     
    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        
        return item
 
    def _conditional_insert(self, tx, item):
        # create record if doesn't exist. 
        # all this block run on it's own thread
        #tx.execute("select * from baidu_user where uk = %s", (item['uk'], ))
        #result = tx.fetchone()
        
        sql=item.sql()
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
        if not sql:
            return
        #print "[SQL]",sql
        tx.execute(sql)
        
        #log.msg("stored in db: table:%s action:%s sql:%s" % (item["table_name"],item["table_action"],sql), level=log.DEBUG)
 
    def handle_error(self, e):
        #print "-----------",e
        log.err(e)
++++++
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
#model
from model.notifications import Notification
from model.db_config import DBSession
#debug
from ipdb import set_trace

class CrystalPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        #set_trace()
        self.validate_item(item)
        notification = Notification(url=item['url'].encode('utf8'),
                title=item['title'].encode('utf8'),
                college=item['college'].encode('utf8'),
                speaker=item['speaker'].encode('utf8'),
                venue=item['venue'].encode('utf8'),
                time=item['time'].encode('utf8'),
                notify_time=item['notify_time'].encode('utf8'))
        #set_trace()
        self.session.add(notification)
        self.session.commit()
        
        return item

    def validate_item(self, item):
        if 'url' not in item:
            raise DropItem("Invalid item found: %s" % item)

        if 'title' not in item:
            item['title'] = ''

        if 'college' not in item:
            item['college'] = ''
            
        if 'speaker' not in item:
            item['speaker'] = ''
            
        if 'venue' not in item:
            item['venue'] = ''
            
        if 'time' not in item:
            item['time'] = ''
            
        if 'notify_time' not in item:
            item['notify_time'] = item['time']


    def close_spider(self, spider):
        self.session.close()
  ++++++++
  # -*- coding: utf-8 -*-
import time
##################################################
# rdryan@sina.com
# Copyright (c) 2015
##################################################

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YelpPipeline(object):
        
    def open_spider(self, spider):
        self.file = open('output/%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H%M")), 'w+')
        self.file.write('name,category,ratevalue,reviewcount,address,postcode,city,area,telephone,website,price,url\n')
        
    def process_item(self, item, spider):
        #self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['name'].encode('utf-8')))
        self.file.write('"%s",' % (item['category'].encode('utf-8')))
        self.file.write('"%s",' % (item['ratevalue'].encode('utf-8')))
        self.file.write('"%s",' % (item['reviewcount'].encode('utf-8')))
        self.file.write('"%s",' % (item['address'].encode('utf-8')))
        self.file.write('"%s",' % (item['postcode'].encode('utf-8')))
        self.file.write('"%s",' % (item['city'].encode('utf-8')))
        self.file.write('"%s",' % (item['area'].encode('utf-8')))
        self.file.write('"%s",' % (item['telephone'].encode('utf-8')))
        self.file.write('"%s",' % (item['website'].encode('utf-8')))
        self.file.write('"%s",' % (item['price'].encode('utf-8')))
        self.file.write('"%s"\n' % (item['url'].encode('utf-8')))
        
        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()

+++++
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import redis
from scrapy.exceptions import DropItem
from proxyhunter import settings
from proxyhunter.utils import rdb

class BasicPipeline(object):

    def process_item(self, item, spider):

        for k in item.fields:
            v = item[k]
            if isinstance(v, list):
                v = v[0]
            item[k] = v

        if self.check(item):
            return item
        else:
            raise DropItem('bad proxy')

    def check(self, item):
        '''校验item是否合法, 并且进行数据清洗
           1. 协议(prot): [http, https]
           2. 地址(ip): xxx.xxx.xxx.xxx
           3. 端口(port): (0,65535]
        '''

        prot = item['prot'].strip().lower()
        if prot not in ['http', 'https']:
            return False
        item['prot'] = prot

        ip = item['ip'].strip()
        if not re.match(r'^\d+\.\d+\.\d+\.\d+$', ip):
            return False
        item['ip'] = ip

        port = int(item['port'].strip())
        if not 0<port<65536:
            return False
        item['port'] = port

        return True


class DebugPipeline(object):

    def open_spider(self, spider):

        self.enabled = hasattr(spider, 'debug') and spider.debug

    def process_item(self, item, spider):

        if self.enabled:
            print item
        return item


class RedisPipeline(object):

    def open_spider(self, spider):

        pass

    def process_item(self, item, spider):

        proxy = str(item)
        if rdb.add(proxy):
            return item
        else:
            raise DropItem('duplicated item')

    def close_spider(self, spider):

        pass
+++++
# -*- coding: utf-8 -*-
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class HelloWeiboPipeline(object):
    def process_item(self, item, spider):
        return item
    
    
class Mysql_scrapy_pipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
                                    dbapiName='MySQLdb',
                                    host='127.0.0.1',
                                    db='yq',
                                    user='root',
                                    passwd='minus',
                                    cursorclass= MySQLdb.cursors.DictCursor,
                                    charset = 'utf8',
                                    use_unicode = False
                                    )
        
    def process_item(self,item,spider):
        self.dbpool.runInteraction(self._conditional_insert,item)
        return item    
        
    def _conditional_insert(self,tx,item): 
        sql = 'insert into post (id ,url,board, site_id, data_type , title , content, post_time, scratch_time , poster_name,language_type,thread_content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE post_time=%s'
        param = (item['topic_url'],item['topic_url'],item['topic_board'], item['site_id'],item['data_type'],item['topic_title'], item['topic_content'], item['topic_post_time'],item['scratch_time'], item['topic_author'],0,item['thread_content'],item['topic_post_time'])
        tx.execute(sql,param)    
++++
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from openpyxl import Workbook
import csv

# class Engin144Pipeline(object):
#     def process_item(self, item, spider):
#         return item
#
# class ENGIN_147_Pipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('w3school_data_utf8.csv', 'wb', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = csv.dumps(dict(item)) + '\n'
#         # print line
#         self.file.write(line.decode("unicode_escape"))
#         return item
#
# def write_to_csv(item):
#        writer = csv.writer(codecs.open('w3school_data_utf8.csv', 'wb', encoding='utf-8'), dialect='excel', lineterminator='\n')
#        writer.writerow([item[key] for key in item.keys()])
#
# class WriteToCsv(object):
#     def process_item(self, item, spider):
#             write_to_csv(item)
#             return item
#
#
# class TuniuPipeline(object):  # 设置工序一
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['游戏名', '开发者', '邮箱', '游戏链接'])  # 设置表头
#
#
# def process_item(self, item, spider):  # 工序具体内容
#     line = [item['name'], item['dev_name'], item['email'], item['url']]  # 把数据中每一项整理出来
#     self.ws.append(line)  # 将数据以行的形式添加到xlsx中
#     self.wb.save('C:/Users/Administrator/Scrapy_proj/ENGIN_147/tuniu.xlsx')  # 保存xlsx文件
#     return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import alibaba
import pymongo
from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem
 
 
 #db.shop.ensureIndex({"url":1},{"unique":true,"dropDups":true})

class MongoDBPipeline(object):
    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        #self.col = settings['MONGODB_COLLECTION']
        connection = pymongo.Connection(self.server, self.port)
        self.db = connection[self.db]
        self.tables = {"ShopItem":"shop",
            'GoodsItem':'goods',
            "IndexItem":'index',
        }
 
    def process_item(self, item, spider):
        err_msg = ''
        for field, data in item.items():
            if not data:
                err_msg += 'Missing %s of poem from %s\n' % (field, item['url'])
        if err_msg:
            raise DropItem(err_msg)
        
        collection = self.db[self.tables[ item.__class__.__name__ ]]
        collection.insert(dict(item))
        # log.msg('Item written to MongoDB database %s/%s' % (self.db, collection),
        #          level=log.INFO, spider=spider)
        return item
