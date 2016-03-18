# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LawsocietyItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time
import sys


class UklawsocietySpider(CrawlSpider):
    name = "uklawsociety"
    allowed_domains = ["solicitors.lawsociety.org.uk"]
    start_urls = ['http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True&Page=%d' %(n+2) for n in range(1,5)]
    # start_urls = (
        # 'http://www.solicitors.lawsociety.org.uk/',
        # 'http://solicitors.lawsociety.org.uk/person/111596/natasha-victoria-elizabeth-marie-therese-jarvie-toub',
        # 'http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True',
        # 'http://solicitors.lawsociety.org.uk/person/299116/helen-annabel-abear',
        # 'http://solicitors.lawsociety.org.uk/person/5028/lynette-ann-acourt',
        # 'http://solicitors.lawsociety.org.uk/person/18630/peter-malcolm-acourt',
        # 'http://solicitors.lawsociety.org.uk/person/225171/leenamari-aantaa-collier',
        # 'http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True',
        # 'http://solicitors.lawsociety.org.uk/search/results?Name=&Type=1&IncludeNlsp=false&IncludeNlsp=True&Location=&AreaOfPractice1=&AreaOfPractice2=&SraId=&Pro=True&Language=',
    # )
    # http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True
    # http://solicitors.lawsociety.org.uk/search/results?Type=1&IncludeNlsp=True&Pro=True&Page=2
    ###{{{Rules To Be Applied for all the links found in subsequent pages
    rules = (
        Rule(LinkExtractor(allow=(r'/person/\d+/\w.+')),
            process_links='process_links',
            callback='parse_solicitors',
            follow=True,
            # max_pages=5
            ),
        )
    ###}}}

    ###{{{
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(20)
        super(UklawsocietySpider, self).__init__(*args, **kwargs)
    ###}}}
    # def __init__(self):
    #     self.driver = webdriver.PhantomJS()
    #     self.driver.set_window_size(1120, 550)
    # service_args = ['--ignore-ssl-errors=true',]
    # driver = webdriver.PhantomJS(service_args=service_args)
    # # url = request.url
    # driver.get(url)

    def parse_solicitors(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # service_args = ['--ignore-ssl-errors=true',]
        # driver = webdriver.PhantomJS(service_args=service_args)
        # url = request.url
        # self.driver.get(response.url)
        # driver.get(url)
        # service_args = ['--ignore-ssl-errors=true',]
        # driver = webdriver.PhantomJS(service_args=service_args)
        # driver = webdriver.PhantomJS()
        # self.driver.get(response.url)
        # time.sleep(2)
        # i = 0
        # count = 2
        # while i < count:
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2)
        #     i += 1
        #     print("aggregating tweets! step: " + str(i) + " of " + str(count))
        # # hxs = Selector(text = self.driver.page_source)
        # sel = Selector(text=self.driver.page_source)
        item = LawsocietyItem()
        name_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/header/h1/text()').extract()
        # html body div#page-content.page-content.container div.row div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details header p
        item['Solicitor_Title'] = ''.join(sel.css('html body div#page-content.page-content.container div.row div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details header p *::text').extract()).strip()
        solicitor_title_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/header/p/text()').extract()
        sra_id_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        sra_regulated_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        # html body div#page-content.page-content.container div.row div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details div#details-accordion.accordion.hidden-phone div.accordion-group section div#main-details-accordion.accordion-body.collapse.in.expanded div.panel-half dl dd
        #div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details
        #'div#details-accordion.accordion.hidden-phone div.accordion-group section div#main-details-accordion.accordion-body.collapse.in.expanded div.panel-half dl dd::text')
        item['Association_At'] = ''.join(sel.css('div#details-accordion.accordion.hidden-phone div.accordion-group section div#main-details-accordion.accordion-body.collapse.in.expanded div.panel-half dl dd::text').extract()).strip()
        # association_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[1]/dd[1]/text()').extract()
        telephone_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[1]/text()').extract()
        email_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[2]/a/text()').extract()
        ###html body div#page-content.page-content.container div.row div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details div#details-accordion.accordion.hidden-phone div.accordion-group section div#areas-of-practice-accordion.accordion-body.collapse.in.expanded ul
        #css('div#areas-of-practice-accordion.accordion-body.collapse.in.expanded ul li::text').extract()

        ### areas_of_practice_data = sel.css('div#areas-of-practice-accordion.accordion-body.collapse.in.expanded ul li::text').extract()
        item['Practice_Area'] = ''.join(sel.css('div#areas-of-practice-accordion.accordion-body.collapse.in.expanded ul li::text').extract()).strip()

        # areas_of_practice_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[2]/div[2]/ul/text()').extract()
        # //*[@id="areas-of-practice-accordion"]/ul/li
        # id="areas-of-practice-accordion" class="accordion-body in collapse expanded"
        # html body div#page-content.page-content.container div.row div#main-content.span3.main-content article.solicitor.solicitor-type-individual.details div#details-accordion.accordion.hidden-phone div.accordion-group section div#languages-spoken-accordion.accordion-body.in.collapse.expanded ul
        # div#languages-spoken-accordion.accordion-body.in.collapse.expanded ul
        # language_spoken_data = sel.css('div#languages-spoken-accordion.accordion-body.in.collapse.expanded ul').extract()

        ### language_spoken_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[3]/div[2]//ul//li//text()').extract()
        item['Language_Spoken'] = ''.join(sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[3]/div[2]//ul//li//text()').extract()).strip()

        # sel = Selector(text=self.driver.page_source)
        # item = LawsocietyItem()
        # name_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/header/h1/text()').extract()
        # solicitor_title_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/header/p/text()').extract()
        # sra_id_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        # sra_regulated_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        # association_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[1]/dd[1]/text()').extract()
        # telephone_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[1]/text()').extract()
        # email_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[2]/a/text()').extract()
        # areas_of_practice_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[2]/div[2]/ul/text()').extract()
        # language_spoken_data = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[3]/div[2]/ul/text()').extract()

        source_urls_data = response.url
        item['Source_Urls'] = source_urls_data
        item['Name'] = name_data
        # item['Solicitor_Title'] = solicitor_title_data
        item['SRA_ID'] = sra_id_data
        item['SRA_Status'] = sra_regulated_data
        # item['Association_At'] = association_data
        item['Telephone'] = telephone_data
        item['Email'] = email_data
        # item['Practice_Area'] = areas_of_practice_data
        # item['Language_Spoken'] = language_spoken_data
        # "".join([i.strip() for i in "\n".join(input_list).split("\n")])
        # item["shop_name"] = [n.encode("utf-8") for n in shop_name][0]
        return item
        self.driver.quit()

        # /html/body/div[3]/div[2]/div[1]/article/header/h1
        # #\/pub\/\w.+
            # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
            # deny=('/users/', '/collections/'), unique=True
            # LinkExtractor(allow=(r'/lawyer/(\w+)-*(\w+)-*\w+-*(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/(((\w+)-*(\w+)-*\w+-*-*\w+-*)|((\w+)-*(\w+)-*\w+-*)|((\w+)-*(\w+)))(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/\w.+-(\d+)'),deny=(r'/contact', r'/vcard'), follow=True), #working Latestv1
            # lastest2
            # LinkExtractor(allow=(r'/person/\w.+$'), deny=(r'/contact', r'/vcard', r'/questions', r'tel'),), #working Latestv1
        # #
        # """
            # {{/person/\d+/\w.+
            # """
            ###{{{
            #
            # http://solicitors.lawsociety.org.uk/person/299116/helen-annabel-abear
            # http://solicitors.lawsociety.org.uk/person/5028/lynette-ann-acourt
            ###}}}
            # /lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+[^/]
            # /pub/\w.+$
            # /lawyer/\w.+-(\d+)
            # (\w+-?)+$
            # LinkExtractor(allow=(r'/lawyer/\w+-*\w+-*\w+-*\w+-*\w+-*\d+'),), #working
            # LinkExtractor(allow=(r'/lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+$')), #trying to not include contact
            #/lawyer/(\w+)*-*(\w+)*-*(\w+)*-*\d+
# """
    # # Rule settings
    # # Regex Pattern Identification
    # # http://solicitors.lawsociety.org.uk/person/299116/helen-annabel-abear
    # # http://solicitors.lawsociety.org.uk/person/5028/lynette-ann-acourt
    # # http://solicitors.lawsociety.org.uk/person/18630/peter-malcolm-acourt
    # # http://solicitors.lawsociety.org.uk/person/225171/leenamari-aantaa-collier
    # """
