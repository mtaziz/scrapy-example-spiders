# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import HomesItem
from scrapy.selector import Selector
import urlparse
import re 


class HomesQuestionsSpider(CrawlSpider):
    name = "homes_questions"
    allowed_domains = ["homes.com"]
    start_urls = (
        'http://www.homes.com/answers/page-2/',
    )
    rules = (
        Rule(
            #\/pub\/\w.+
            # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
            # //*[@id="recentQuestions"]/div[23]/div/a[6]
            # 
            # LinkExtractor(allow=(r'page-\d+$')),
            LinkExtractor(
            	# process_links='process_links',
            	allow=(r'/answers/page\-\d+\/$')
            	# restrict_xpaths='//div[@class="searchPag"]/@href', canonicalize=True,
            	),
            	 process_links='process_links',
            	 callback='parse_links',
            	 follow=True, 
            # max_pages=5
            ),
        )

    def parse_links(self, response):
    	item = HomesItem()
    	sel = Selector(response)
    	url_data = response.url
    	# ('//div[@class="listOfQuestions parentHover"]//a//@title').extract()
    	questions_data = sel.xpath('//div[@class="listOfQuestions parentHover"]//a//@title').extract()
    	# \,Report,
    	# [s.strip().split(': ') for s in data_string.splitlines()]
    	#questions_elimination = re.findall(r'\,Report,', '', str(questions_data))  
    	#questions_stripped = [s.strip().split('?') for s in str(questions_elimination).splitlines()]
    	#questions_clean = (str(questions_data).replace(',Report', '')).strip()
    	item['urls'] = url_data
    	item['questions'] = questions_data
    	return item
        
