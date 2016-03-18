# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FinestSpiderItem
from scrapy.selector import Selector
from selenium.webdriver.common.proxy import *
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


class FinestSpider(CrawlSpider):
    name = "finest"
    allowed_domains = ["finest.se"]
    # start_urls = ['http://finest.se/blog-toplist','http://finest.se/member-blog','http://finest.se/blogs-topbloggers']
    # start_urls = ['http://finest.se']

    # rules = (
    #     Rule(LinkExtractor(allow=(r'\/finest\.se/\w+.$'), deny=(r'\/gallaries', r'\/events/', r'\/elections/', r'\/questions', r'\/feed', r'\/magazine')),
    #         process_links='process_links',
    #         callback='parse_finest',
    #         follow=True,
    #         # max_pages=5
    #         ),
    #     )

    def __init__(self, *args, **kwargs):
        super(FinestSpider, self).__init__(*args, **kwargs)
        self.js_bin = settings.get('JS_BIN')
        self.js_wait = settings.get('JS_WAIT')
        self.start_urls = ['http://finest.se/blog-toplist']
        service_args = ['--proxy=%s' % settings.get('HTTP_PROXY'), '--proxy-type=http', '--load-images=false']
        self.driver = webdriver.PhantomJS(
            executable_path=self.js_bin, service_args=service_args)
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1920, 1080)

        # self.driver = webdriver.PhantomJS()
        self.rules = (Rule(LinkExtractor(
            allow=(r'\/finest\.se/\w+.$'), deny=(r'\/gallaries', r'\/events/', r'\/elections/', r'\/questions', r'\/feed', r'\/magazine')),
            process_links='process_links',
            # callback='parse_finest',
            follow=True,),)

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(self.js_wait)
        tries = 0
        MAXTRIES = 10
        lastHeight = newHeight = 0
        pageSize = maxSize = 0

        while True:
            try:
                button = self.driver.find_element_by_class_name(
                    "btn btn-block btn-customize-more load-more-toplist")
                button.click()
                # self.maxPages = self.driver.page_source
                sel2 = Selector(text=self.driver.page_source)
                for url in list(set(sel2.xpath('//*[@class="ser_desc"]//@href').extract())):
                    size_urls = "%s" % url
            # photo_id = url.split('/')[-2]
                    item = FinestSpiderItem()
            # item['emotion'] = self.emotion
                    item['Size_Url'] = size_urls
                    yield Request(url=item['Size_Url'], callback=self.parse_download)
            except:

                lastHeight = newHeight
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(self.js_wait)
                newHeight = self.driver.execute_script(
                    "return document.body.scrollHeight")
                pageSize = len(self.driver.page_source)

                if lastHeight == newHeight:
                    tries += 1

                if pageSize > maxSize:
                    maxSize = pageSize
                    maxPage = self.driver.page_source
                    if tries > MAXTRIES:
                        break
                else:
                    break
                print "New height:%s with page size: %s \n" % (newHeight, maxSize)
            # sel2 = Selector(text=maxPages)
            # for url in list(set(sel2.xpath('//*[@class="ser_desc"]//@href').extract())):
            #     size_urls = "%s" % url
            # # photo_id = url.split('/')[-2]
            #     item = FinestSpiderItem()
            # # item['emotion'] = self.emotion
            #     item['Size_Url'] = size_urls
            #     yield Request(url=item['Size_Url'], callback=self.parse_download)

    def parse_download(self, response):
        sel = Selector(response)
        # self.driver.get(response.url)
        # sel = Selector(text=self.driver.page_source)
        item = FinestSpiderItem()
        item['Blogger_Source_Urls'] = response.url
        response_url = response.url
        item['Blogger_Name'] = response_url.lstrip('http://finest.se/').strip('/')
        # item['Blogger_Name'] = map(unicode.strip, sel.xpath('/html/body/div[4]/div[2]/div[3]/header/hgroup/h1/a/text()').extract())
        # map(unicode.strip
        # r'(\w+@\w+\.com)'
        # r = re.compile(r'\w+@\w+\.com')
        # r = re.compile(r"\b[A-Z0-9._%+-]+(?:@|[(\[]at[\])])[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
        # item['Blogger_Email'] = r.findall(response.url)
        item['Blogger_Email'] = map(unicode.strip, sel.xpath('//*[contains(text(),"@")]/text()').extract())
        # http://finest.se/liinadolk
        # r = re.compile(r"\b[A-Z0-9._%+-]+(?:@|[(\[]at[\])])[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
        # Email Regex: (\w+@[a-zA-Z_]+?\.[a-zA-Z])
        # item['Service_Description'] = sel.css('div#business-profile-page.listing.listing-data div.bpp-layout div.bpp-layout-middle.clamp-widest div.bpp-layout-primary-content div.business-details.global-width.primary-contacts-3 div.contact-details div.media-object.clearfix.inside-gap-medium.image-on-right div.body.left h3.listing-short-description::text').extract()
        # item['Phone_No'] = sel.css('div#business-profile-page.listing.listing-data div.bpp-layout div.bpp-layout-middle.clamp-widest div.bpp-layout-primary-content div.business-details.global-width.primary-contacts-3 div#contact-card-scroll-to.primary-contacts-container div.primary-contacts.count-3 div.left div.contacts div.main a.click-to-call.contact.contact-preferred.contact-phone div.text-and-image.inside-gap.inside-gap-medium.grow span.text.middle div::text').extract()
        # item['Email'] = sel.css('div#business-profile-page.listing.listing-data div.bpp-layout div.bpp-layout-middle.clamp-widest div.bpp-layout-primary-content div.business-details.global-width.primary-contacts-3 div#contact-card-scroll-to.primary-contacts-container div.primary-contacts.count-3 div.left div.contacts div.main a.contact.contact-main.contact-email div.text-and-image.inside-gap.inside-gap-medium.grow span.image.top span.glyph.icon-email.border.border-dark-blue span.alt::text').extract()
        # item['Company_Website'] = sel.css('div#business-profile-page.listing.listing-data div.bpp-layout div.bpp-layout-middle.clamp-widest div.bpp-layout-primary-content div.business-details.global-width.primary-contacts-3 div#contact-card-scroll-to.primary-contacts-container div.primary-contacts.count-3 div.left div.contacts div.main a.contact.contact-main.contact-url div.text-and-image.inside-gap.inside-gap-medium.grow span.image.top span.glyph.icon-website.border.border-dark-blue span.alt::text').extract()
        yield item
        # items.append(item)
        # return items
        # # self.driver.quit()
