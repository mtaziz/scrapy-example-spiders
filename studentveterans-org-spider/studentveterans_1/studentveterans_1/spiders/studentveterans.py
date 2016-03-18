# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from selenium import webdriver
from ..items import StudentveteransSpiderItem
# from selenium import webdriver
from selenium.webdriver import phantomjs
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class StudentveteransSpider(CrawlSpider):
    name = "studentveterans"
    allowed_domains = ["studentveterans.org"]
    start_urls = (
        'http://studentveterans.org/index.php/chapter/directory',
        # 'http://studentveterans.org/index.php/chapter/directory/2451-abraham-baldwin-agricultural-college',
        # 'http://studentveterans.org/index.php/chapter/directory/1376-adelphi-university'
    )
    rules = (
    	Rule(
    		LinkExtractor(
    # 			allow=(r'\/index\.php\/chapter\/directory\/\w+\-\w.+'),),
    			allow=(r'\/index\.php\/chapter\/directory\/\d+\-\w.+'),),
    		# \/index\.php\/chapter\/directory\/\d+\-\w.+
    # 			\/\/studentveterans\.org\/index\.php\/chapter\/directory\/\w+?\w.*
                process_links='process_links',
                callback='parse_students',
                follow='True',
                ),)

    # def __init__(self, *args, **kwargs):
    #     super(StudentveteransSpider, self).__init__(*args, **kwargs)
    #     # self.js_bin = settings.get('JS_BIN')
    # #     self.filename = '/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/finest_spider/finest_spider/page_source/level1_start_urls.txt'
    # #     # # self.js_wait = settings.get('JS_WAIT')
    # #     # # self.start_urls = ['http://finest.se/blog-toplist']
    # #     # # service_args = ['--ignore-ssl-errors=true', '--load-images=false', '--ssl-protocol=any']
    # #     # # service_args = ['--proxy=%s' % settings.get('HTTP_PROXY'), '--ignore-ssl-errors=true','--proxy-type=socks5', '--load-images=false','--ssl-protocol=any']
    #     service_args = ['--ignore-ssl-errors=true', '--load-images=false', '--ssl-protocol=any']
    # #     # # self.driver = webdriver.Firefox()
    #     self.driver = webdriver.PhantomJS(service_args=service_args)
    #     # # self.driver = webdriver.PhantomJS(executable_path=self.js_bin)
    #     self.driver.implicitly_wait(10)

    def parse_students(self, response):
    	# self.driver.get(response.url)
     #    sel = Selector(text=self.driver.page_source)
        sel = Selector(response)
        infos = sel.xpath('//div[@class="span4"]/ul[@class="fields"]')
        for info in infos:
            item = StudentveteransSpiderItem()
            ChapterName = info.xpath(".//div[contains(text(), 'Chapter Name')]/following-sibling::*[1]/text()").extract()
            StudentLeaderFirstName = info.xpath(".//div[contains(text(), 'Student Leader First Name')]/following-sibling::*[1]/text()").extract()
            StudentLeaderLastName = info.xpath(".//div[contains(text(), 'Student Leader Last Name')]/following-sibling::*[1]/text()").extract()
            Address = info.xpath(".//div[contains(text(), 'Address')]/following-sibling::*[1]/text()").extract()
            Website = info.xpath("//*[contains(text(), 'Website')]/following-sibling::*[1]/text()").extract()
            StudentLeaderFirstName = info.xpath("//*[contains(text(), 'Student Leader First Name')]/following-sibling::*[1]/text()").extract()
            StudentLeaderLastName = info.xpath("//*[contains(text(), 'Student Leader Last Name')]/following-sibling::*[1]/text()").extract()
            StudentLeaderEmail = info.xpath("//*[contains(text(), 'Student Leader Email')]/following-sibling::*[1]/text()").extract()
            ChapterAdvisorFirstName = info.xpath("//*[contains(text(), 'Chapter Advisor First Name')]/following-sibling::*[1]/text()").extract()
            ChapterAdvisorLastName = info.xpath("//*[contains(text(), 'Chapter Advisor Last Name')]/following-sibling::*[1]/text()").extract()
            ChapterAdvisorEmail = info.xpath("//*[contains(text(), 'Chapter Advisor Email')]/following-sibling::*[1]/text()").extract()
            ChapterLeaderPhone = info.xpath("//*[contains(text(), 'Chapter Leader Phone')]/following-sibling::*[1]/text()").extract()
            ChapterAdvisorPhone = info.xpath("//*[contains(text(), 'Chapter Advisor Phone')]/following-sibling::*[1]/text()").extract()
            SchoolType = info.xpath("//*[contains(text(), 'School Type')]/following-sibling::*[1]/text()").extract()
            ChapterEmail = info.xpath("//*[contains(text(), 'Chapter E-Mail')]/following-sibling::*[1]/text()").extract()
            ChapterPhone = info.xpath("//*[contains(text(), 'Chapter Phone')]/following-sibling::*[1]/text()").extract()
            OPEID = info.xpath("//*[contains(text(), 'OPE ID')]/following-sibling::*[1]/text()").extract()
            IPEDSID = info.xpath("//*[contains(text(), 'IPEDS ID')]/following-sibling::*[1]/text()").extract()

            # ChapterName = info.xpath("//*[contains(text(), 'Chapter Name')]/following-sibling::*[1]/text()")
            # StudentLeaderFirstName = info.xpath("//*[contains(text(), 'Student Leader First Name')]/following-sibling::*[1]/text()")
            # StudentLeaderLastName = info.xpath("//*[contains(text(), "Student Leader Last Name")]/following-sibling::*[1]/text()")
            # Address = info.xpath("//*[contains(text(), "Address")]/following-sibling::*[1]/text()")
            # Website = info.xpath("//*[contains(text(), "Website")]/following-sibling::*[1]/text()")
            # StudentLeaderFirstName = info.xpath("//*[contains(text(), "Student Leader First Name")]/following-sibling::*[1]/text()")
            # StudentLeaderLastName = info.xpath("//*[contains(text(), "Student Leader Last Name")]/following-sibling::*[1]/text()")
            # StudentLeaderEmail = info.xpath("//*[contains(text(), "Student Leader Email")]/following-sibling::*[1]/text()")
            # ChapterAdvisorFirstName = info.xpath("//*[contains(text(), "Chapter Advisor First Name")]/following-sibling::*[1]/text()")
            # ChapterAdvisorLastName = info.xpath("//*[contains(text(), "Chapter Advisor Last Name")]/following-sibling::*[1]/text()")
            # ChapterAdvisorEmail = info.xpath("//*[contains(text(), "Chapter Advisor Email")]/following-sibling::*[1]/text()")
            # ChapterLeaderPhone = info.xpath("//*[contains(text(), "Chapter Leader Phone")]/following-sibling::*[1]/text()")
            # ChapterAdvisorPhone = info.xpath("//*[contains(text(), "Chapter Advisor Phone")]/following-sibling::*[1]/text()")
            # SchoolType = info.xpath("//*[contains(text(), "School Type")]/following-sibling::*[1]/text()")
            # ChapterEmail = info.xpath("//*[contains(text(), "Chapter E-Mail")]/following-sibling::*[1]/text()")
            # ChapterPhone = info.xpath("//*[contains(text(), "Chapter Phone")]/following-sibling::*[1]/text()")
            # OPEID = info.xpath("//*[contains(text(), "OPE ID")]/following-sibling::*[1]/text()")
            # IPEDSID = info.xpath("//*[contains(text(), "IPEDS ID")]/following-sibling::*[1]/text()")

            item['ChapterName'] = ChapterName
            item['StudentLeaderFirstName'] = StudentLeaderFirstName
            item['StudentLeaderLastName'] = StudentLeaderLastName
            item['Address'] = Address
            item['Website'] = Website
            item['StudentLeaderFirstName'] = StudentLeaderFirstName
            item['StudentLeaderLastName'] = StudentLeaderLastName
            item['StudentLeaderEmail'] = StudentLeaderEmail
            item['ChapterAdvisorFirstName'] = ChapterAdvisorFirstName
            item['ChapterAdvisorLastName'] = ChapterAdvisorLastName
            item['ChapterAdvisorEmail'] = ChapterAdvisorEmail
            item['ChapterLeaderPhone'] = ChapterLeaderPhone
            item['ChapterAdvisorPhone'] = ChapterAdvisorPhone
            item['SchoolType'] = SchoolType
            item['ChapterEmail'] = ChapterEmail
            item['ChapterPhone'] = ChapterPhone
            item['OPEID'] = OPEID
            item['IPEDSID'] = IPEDSID
            yield item
