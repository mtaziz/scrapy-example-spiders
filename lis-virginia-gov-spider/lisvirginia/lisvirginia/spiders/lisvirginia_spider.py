# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LisvirginiaItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time 
import sys

class LisvirginiaSpiderSpider(CrawlSpider):
    name = "lisvirginia_spider"
    allowed_domains = ["lis.virginia.gov"]
    start_urls = (
        'http://lis.virginia.gov/cgi-bin/legp604.exe?151+lst+PAS',
        # 'http://lis.virginia.gov/cgi-bin/legp604.exe?151+sum+HB1275',
    	# 'http://lis.virginia.gov/cgi-bin/legp604.exe?151+lst+PAS+HB1476',
    	# 'http://lis.virginia.gov/cgi-bin/legp604.exe?151+lst+PAS+HB1662',
    	# 'http://lis.virginia.gov/cgi-bin/legp604.exe?151+lst+PAS+HB1818',
     #    'http://lis.virginia.gov/cgi-bin/legp604.exe?151+lst+PAS+HB1986',
    )
    ###{{{StackOverFlow
    # def process_onclick(value):
    # m = re.search("window.open\('(.+?)'", value)
    # if m:
    #     return m.group(1)
    ###}}}
    # LinkExtractor(allow=(r'/lawyer/\w.+$'), deny=(r'/contact', r'/vcard', r'/questions', r'tel'),), #working Latestv1
    # <a href="/cgi-bin/legp604.exe?151+lst+PAS+HB1476"><b>More...</b></a>
    # <a onclick="window.open('page.asp?ProductID=3679','productwin','width=700,height=475,scrollbars,resizable,status');" href="#internalpagelink">Link Text</a>

    rules = (
        # Rule(LinkExtractor(allow=(r'http://www.stadlistan.se/\w.+/\w.+/\w.+'), deny=(r'/ajax/company/'),),
        # Rule(LinkExtractor(allow=(r'http://lis\.virginia\.gov/cgi\-bin/legp604\.exe\?151\+sum\+\w.+')),
        # /cgi\-bin/legp604\.exe\?\d+\+\w+\+\w.+
        Rule(LinkExtractor(allow=(r'/legp604.exe\?\d+\+\w+\+\w.+$')), #allow allow
        # Rule(LinkExtractor(allow=(r'/cgi\-bin/legp604\.exe\?\d+\+\w+\+\w.+')),
        # /html/body/div/div[2]/div[2]/h3/a[3]
        # //*[@id="mainC"]/h3/a[3]
#         rules=( Rule(SgmlLinkExtractor(allow=(),
#                            attrs=('onclick',),
#                            process_value=process_onclick),
#         callback='parse_item'),
# )
        # Rule(LinkExtractor(allow=(),
            # (r'/cgi\-bin/legp604.exe\?\d+\+\w+\+\w.+')),
            # /cgi-bin/legp604.exe?151+lst+PAS+HB1476
        # Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="mainC"]/h3/a[3]')),
            process_links='process_links',
            callback='parse_lisvirginia',
            follow=True,
            # max_pages=5
            ),
        )
    ###}}}
    
    ###{{{
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(50)
        super(LisvirginiaSpiderSpider, self).__init__(*args, **kwargs)

    def parse_lisvirginia(self, response):
    	# self.driver.get(response.url)
    	# sel = Selector(text=self.driver.page_source)
        sel = Selector(response)
    	item = LisvirginiaItem()
    	item['Source_Urls'] = response.url
    	item['Bill_Number'] =  sel.xpath('/html/body/div/div[2]/div[2]/h3/text()').extract()[0:2]
        item['Bill_Title'] = sel.xpath('/html/body/div/div[2]/div[2]/h3/text()').extract()[2:]
    	item['Author'] = sel.xpath('/html/body/div/div[2]/div[2]/p[1]/a[1]/text()').extract()
    	item['Summary'] = sel.xpath('/html/body/div/div[2]/div[2]/p[2]/text()').extract()
    	yield item    	