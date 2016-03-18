import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.contrib.spiders import CrawlSpider
from scrapy.utils.response import open_in_browser
from scrapy.item import Item, Field
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from selenium.common.exceptions import NoSuchElementException       


class googleSpider(CrawlSpider):
 
    name = "googlish"
    allowed_domains = ["google.com"]
    start_urls = ["http://www.google.com"]
            
    def __init__(self):
        self.driver = webdriver.Firefox()
   
    def parse(self, response):
        self.driver.get(response.url)      
        login_form = self.driver.find_element_by_name('q')        
        login_form.send_keys("scrapy\n")
        time.sleep(4)
        found = False
        while not found:
            try :
                for element in self.driver.find_elements_by_xpath("//div[@class='rc']"):
                    print element.text + "\n"
   
                for i in self.driver.find_elements_by_id('pnnext'):
                    i.click()
                time.sleep(5)        
            except NoSuchElementException:
                found = True
                pass

        self.driver.close()
#___________________________#
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytest.items import MytestItem
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ZomatoRestrComments(scrapy.Spider):

    name = "zomcomment"
    allowed_domains = ["zomato.com"]
    start_urls = [
        "https://www.zomato.com/ncr/lutyens-cocktail-house-janpath-new-delhi"
        ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        # use of selenium 
        self.driver.get(response.url)
        next = self.driver.find_element(By.XPATH,'//div[contains(@class,"clearfix zs-load-more res-page-load-more")]')
        while True:
            try:
                next.click()
            except:
                break

        # use of scrapy
        items = []
        page = self.driver.page_source
        sel = etree.HTML(page)
        filename = response.url.split('/')[-1]+".txt"
        f = open(filename,'a')      
        films = sel.xpath('//div[contains(@class, "zs-following-list")]')
        for film in films:
            # Populate film fields
            item = MytestItem()
            item['comment'] = film.xpath('//div[contains(@itemprop, "description")]/div/text()')
            items.append(item)
        for i in range(0,len(items)):
            all_comments = ''.join(items[i]['comment']).encode('utf8').replace('\n',' ')
            all_comments =all_comments.split('          ')

        for final_comments in all_comments:
                if(final_comments!=""):
                    print final_comments.strip()
                    f.write(final_comments.strip()+"\n\n")

        # closing selenium
        self.driver.close()
        return items
 
    
 
    def __normalise(self, value):
        # Convert list to string
        value = value if type(value) is not list else ' '.join(value)
        # Trim leading and trailing special characters (Whitespaces, newlines, spaces, tabs, carriage returns)   div[contains(@class, "rev-text") or 
        value = value.strip()
 
        return value
 
    def __to_absolute_url(self, base_url, link):
        import urlparse
        link = urlparse.urljoin(base_url, link)
        return link
 
    def __to_int(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
 
        return value
 
    def __to_float(self, value):
        try:
            value = float(value)
        except ValueError:
            value = 0.0
 
        return value
#___________________________#
import logging
import scrapy
from scrapy.utils.log import configure_logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time



class ASpyder(scrapy.Spider):
    name = 'a'
    start_urls = ['']

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('')
        self.driver.find_element_by_xpath('//img[@id="gridview"]').click()

    def parse(self, response):
        self.driver.get(response.url)
        for i in range(3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        i = 2
        while True:
            try:
                self.driver.find_element_by_xpath('//di' % i).click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                i += 1
            except NoSuchElementException:
                break
        time.sleep(1)
        for entry in self.driver.find_elements_by_xpath('//di'):
            item = ImartItem()
            item['name'] = entry.find_element_by_xpath('p//span//span[@itemprop="name"]').text
            item['address'] = entry.find_element_by_xpath('span//span[@itemprop="streetAddress"]').text
            item['city'] = entry.find_element_by_xpath('span//span[@class="cityLocation"]').text
            item['pincode'] = entry.find_element_by_xpath('//span[@itemprop="postalCode"]').text
            item['state'] = entry.find_element_by_xpath('//span[@itemprop="addressRegion"]').text
            item['telephone'] = entry.find_element_by_xpath('div/span//span[@itemprop="telephone"]').text
            yield item
import scrapy
import time 
from selenium import webdriver 


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        print response.body
        with open(filename, 'wb') as f:
            f.write(response.body)

class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = [
        "https://www.google.com/about/careers/search"
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        search_bar = self.driver.find_element_by_id("gbqfq")
        search_bar.send_keys("Summer")
        button = self.driver.find_element_by_class_name("gbqfb")
        button.click()

        while True:
            next_page = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/div/div[6]/a[4]/img")
            try:
                next_page.click()
                hxs = HtmlXPathSelector(response)
                print hxs
                titles = hxs.select("//span[@class='pl']")
                for title in titles:
                    title = titles.select("a/text()").extract()
                    link = titles.select("a/@href").extract()
                    #print title, link
            except:
                break

        filename = "Google"
        with open(filename, 'wb') as f:
            f.write(response.body)


class FacebookSpider(scrapy.Spider):
    name = "facebook"
    allowed_domains = ["facebook.com"]
    start_urls = [
        "https://www.facebook.com/careers/university"
    ]

    def parse(self, response):
        filename = "Facebook"
        with open(filename, 'wb') as f:
            f.write(response.body)