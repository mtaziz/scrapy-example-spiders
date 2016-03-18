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


class UklawsocietySpider(CrawlSpider):
    name = "uklawsociety"
    allowed_domains = ["solicitors.lawsociety.org.uk"]
    start_urls = (
        # 'http://www.solicitors.lawsociety.org.uk/',
        'http://solicitors.lawsociety.org.uk/search/results?Name=&Type=1&IncludeNlsp=false&IncludeNlsp=True&Location=&AreaOfPractice1=&AreaOfPractice2=&SraId=&Pro=True&Language=',

    )

    """ 
    # Rule settings 
    # Regex Pattern Identification
    # http://solicitors.lawsociety.org.uk/person/299116/helen-annabel-abear
    # http://solicitors.lawsociety.org.uk/person/5028/lynette-ann-acourt
    # http://solicitors.lawsociety.org.uk/person/18630/peter-malcolm-acourt
    # http://solicitors.lawsociety.org.uk/person/225171/leenamari-aantaa-collier
    """
    rules = (
        Rule(
            #\/pub\/\w.+
            # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
            # deny=('/users/', '/collections/'), unique=True
            # LinkExtractor(allow=(r'/lawyer/(\w+)-*(\w+)-*\w+-*(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/(((\w+)-*(\w+)-*\w+-*-*\w+-*)|((\w+)-*(\w+)-*\w+-*)|((\w+)-*(\w+)))(\d+)'),deny=(r'/contact', r'/vcard')), #working Latestv1
            # LinkExtractor(allow=(r'/lawyer/\w.+-(\d+)'),deny=(r'/contact', r'/vcard'), follow=True), #working Latestv1 
            # lastest2
            # LinkExtractor(allow=(r'/person/\w.+$'), deny=(r'/contact', r'/vcard', r'/questions', r'tel'),), #working Latestv1
            LinkExtractor(allow=(r'/person/\d+/\w.+')), #working Latestv1
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
            process_links='process_links',
            callback='parse_solicitors',
            follow=True, 
            # max_pages=5
            ),
        )
    service_args = ['--ignore-ssl-errors=true',]
    driver = webdriver.PhantomJS(service_args=service_args)
    # url = request.url
    # driver.get(url)

    def parse_solicitors(self, response):
        # service_args = ['--ignore-ssl-errors=true',]
        # driver = webdriver.PhantomJS(service_args=service_args)
        # url = request.url
        self.driver.get(response.url)
        # driver.get(url)
        sel = Selector(text=self.driver.page_source)
        item = LawsocietyItem()
        name_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/header/h1/text()').extract()
        solicitor_title_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/header/p/text()').extract()
        sra_id_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        sra_regulated_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/dl/dd/text()').extract()
        association_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[1]/dd[1]/text()').extract()
        telephone_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[1]/text()').extract()
        email_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[1]/div[2]/div/dl[2]/dd[2]/a/text()').extract()
        areas_of_practice_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[2]/div[2]/ul/text()').extract()
        # response.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[3]/div[2]/ul/li/text()').extract()
        language_spoken_data = sel.xpath('/html/body/div[3]/div[2]/div[1]/article/div/div/section[3]/div[2]/ul/li/text()').extract()
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
        item['Solicitor_Title'] = solicitor_title_data
        item['SRA_ID'] = sra_id_data
        item['SRA_Status'] = sra_regulated_data
        item['Association_At'] = association_data
        item['Telephone'] = telephone_data
        item['Email'] = email_data
        item['Practice_Area'] = areas_of_practice_data
        item['Language_Spoken'] = language_spoken_data

        return item 
        driver.quit()

        # /html/body/div[3]/div[2]/div[1]/article/header/h1