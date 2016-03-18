# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item


class StudentveteransSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ChapterName = Field()
    StudentLeaderFirstName = Field()
    StudentLeaderLastName = Field()
    Address = Field()
    Website = Field()
    StudentLeaderFirstName = Field()
    StudentLeaderLastName = Field()
    StudentLeaderEmail = Field()
    ChapterAdvisorFirstName = Field()
    ChapterAdvisorLastName = Field()
    ChapterAdvisorEmail = Field()
    ChapterLeaderPhone = Field()
    ChapterAdvisorPhone = Field()
    SchoolType = Field()
    ChapterEmail = Field()
    ChapterPhone = Field()
    OPEID = Field()
    IPEDSID = Field()
    pass
