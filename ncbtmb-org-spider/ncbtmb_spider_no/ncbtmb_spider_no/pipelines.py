# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class VesselsDispatchSpiderPipeline(object):
import csv
import itertools

class CSVPipeline(object):
	def __init__(self):
		self.csvwriter = csv.writer(open('colrip.csv', 'wb'), delimiter=',')
		# V_Vessel = Field()
		self.csvwriter.writerow([ 'V_Vessel','V_From','V_To','V_Time', 'V_Tug', 'V_LOA'])
		# self.csvwriter.writerow([ 'Source_Urls', 'UK_Plan_Name','UK_Plan_Bundle_Price','Plan_Validity','National_Mins', 'National_Text', 'National_Data'])
		# self.csvwriter.writerow([ 'UK_Plan_Name','Plan_Validity','National_Mins', 'National_Text', 'National_Data'])
	
	# def process_item(self, item, spider):
	# 	rows = zip(item['Source_Urls'],item['UK_Plan_Name'],item['UK_Plan_Bundle_Price'],item['Plan_Validity'],item['National_Mins'],item['National_Text'],item['National_Data'])
	def process_item(self, item, spider):
		rows = zip(item['V_Vessel'],item['V_From'],item['V_To'],item['V_Time'],item['V_Tug'], item['V_LOA'])
	# def process_item(self, item, spider):
	# 	rows = zip(item['UK_Plan_Name'],item['Plan_Validity'],item['National_Mins'],item['National_Text'],item['National_Data'])

		for row in rows:
			self.csvwriter.writerow(row)
		return item
    # def process_item(self, item, spider):
    #     return item
