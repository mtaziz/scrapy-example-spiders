# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoximityItem
from scrapy.selector import Selector
import urlparse

class DoximitySpiderSpider(CrawlSpider):
    name = "doximity_spider"
    allowed_domains = ["doximity.com"]
    start_urls = (
        'https://www.doximity.com/pub/dot-jorgen-quistgaard-md',
    )
    #regex:    (/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))
    rules = (
        Rule(
            #\/pub\/\w.+
            # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
            LinkExtractor(allow=(r'/pub/\w.+$')),
            process_links='process_links',
            callback='parse_links',
            follow=True, 
            # max_pages=5
            ),
        )
#     rules = [Rule(LinkExtractor(allow=("^https://www.ghcjobs.apply2jobs.com/ProfExt/index.cfm\?fuseaction=mExternal.returnToResults&CurrentPage=[1-1000]$")), 'parse_inner_page')]

# def parse_inner_page(self, response):
#      # Rule(SgmlLinkExtractor(allow=('/look/\d+')),
     #  process_links='process_links', 
     #  callback='parse_look')
    # def process_links(self,links):
    #     return (link for link in links if self.valid_links(link))

    # def valid_links(self,link):
    #     urlp=urlparse.urlparse(link.url)
    #     querydict=urlparse.parse_qs(urlp.query)
    #     return "locale" not in querydict

#                 # allow=r'((/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+)))'), callback='parse_links', follow=True),
#                 allow=r'\/\w+\-\w+\-\w+'), 'parse_links',),
#         )
# rules = [
#         Rule(
#             LinkExtractor(allow_domains=allowed_domains),
#             process_links='process_links',
#             callback='parse_item',
#             follow=True
#         ),
#     ]
#rules = [Rule(LinkExtractor(allow=['/technology-\d+']), 'parse_story')]
# Rule(SgmlLinkExtractor(allow = (r'/people/(\w+-?)+$', )), callback = 'parse_page'),
    #Rule(SgmlLinkExtractor(allow = (r'/question/\d+', )),  follow = True),
    def parse_links(self, response):
        item = DoximityItem()
        item['urls'] = response.url
        sel = Selector(response)
        names_data = sel.xpath('//*[@id="show_header_app"]/h1/text()').extract()
        office_address_data = sel.xpath('//*[@id="officeinfo"]/ul/li/text()').extract()
        speciality_data = sel.xpath('//*[@id="header_specialty"]/text()').extract()
        #xpath: .//div[@class="profile-section"]//li/text()').extract()
        summary_data = sel.xpath('.//div[@class="profile-section"]//li/text()').extract()
        #html body.grid.profiles.public div.wrap div.page div div.row div.section.profile_public.profiles-content div.col-3-4 div.col-2-3 div.profiler div.profile-section ul li
        item['name'] = names_data
        item['office_address'] = office_address_data
        item['speciality'] = speciality_data
        item['profile_summary'] = summary_data
        return item