class MySpider(BaseSpider):
    name = "youtubecrawler"
    allowed_domains = ["gdata.youtube.com"]
    start_urls = ['http://gdata.youtube.com/feeds/api/standardfeeds/DE/most_popular?v=2&alt=json']

    def parse(self, response):
        items = []
        jsonresponse = json.loads(response.body_as_unicode())
        for video in jsonresponse["feed"]["entry"]:
            item = YoutubeItem()
            print video["media$group"]["yt$videoid"]["$t"]
            print video["media$group"]["media$description"]["$t"]
            item ["title"] = video["title"]["$t"]
            print video["author"][0]["name"]["$t"]
            print video["category"][1]["term"]
            items.append(item)
        return items
#+++++++++++++++++++++++++
pattern = re.compile(r"qubit_product_list = (.*?);", re.M)
        script = hxs.select("//script[contains(., 'qubit_product_list')]/text()").extract()[0]
        data = pattern.search(script).group(1)

        j_data = json.loads(data)
        self.log('After calling LOAD Begins')
        self.log(j_data) #It is not printing ANYTHING!!!!
        self.log('After calling LOAD Ends')

        self.log('\n---------------------------------\n')
        #typecasting the JSON to string for json.loads to work
        data = str(data)
        #returning type dict from json
        j_data = json.loads(data)
        #typecasting the dict to string before writing to log
        self.log(str(j_data)) 
        #from scrapy.http import FormRequest
from scrapy.selector import Selector
# other imports

class SpiderClass(Spider)
    # spider name and all
    page_incr = 1
    pagination_url = 'http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php'

    def parse(self, response):

        sel = Selector(response)

        if page_incr > 1:
            json_data = json.loads(response.body)
            sel = Selector(text=json_data.get('content', ''))

        # your code here 

        #pagination code starts here 
        # if page has content
        if sel.xpath('//div[@class="panel-wrapper"]'):
            self.page_incr +=1
            formdata = {
                    'sorter':'recent',
                    'location':'main loop',
                    'loop':'main loop',
                    'action':'sort',
                    'view':'grid',
                    'columns':'3',
                    'paginated':str(self.page_incr),
                    'currentquery[category_name]':'reviews'
                    }
            yield FormRequest(url=self.pagination_url, formdata=formdata, callback=self.parse)
        else:
            return
I have tested using scrapy shell and its working,
In scrapy Shell
In [0]: response.url
Out[0]: 'http://www.pcguia.pt/category/reviews/#paginated=1'

    In [1]: from scrapy.http import FormRequest

In [2]: from scrapy.selector import Selector

In [3]: import json

In [4]: response.xpath('//h2/a/text()').extract()
Out[4]: 
        [u'HP Slate 8 Plus',
         u'Astro A40 +MixAmp Pro',
         u'Asus ROG G751J',
         u'BQ Aquaris E5 HD 4G',
         u'Asus GeForce GTX980 Strix',
         u'AlienTech BattleBox Edition',
         u'Toshiba Encore Mini WT7-C',
         u'Samsung Galaxy Note 4',
         u'Asus N551JK',
         u'Western Digital My Passport Wireless',
         u'Nokia Lumia 735',
         u'Photoshop Elements 13',
         u'AMD Radeon R9 285',
         u'Asus GeForce GTX970 Stryx',
         u'TP-Link AC750 Wifi Repeater']

In [5]: url = "http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php"

In [6]: formdata = {
        'sorter':'recent',
        'location':'main loop',
        'loop':'main loop',
        'action':'sort',
        'view':'grid',
        'columns':'3',
        'paginated':'2',
        'currentquery[category_name]':'reviews'
        }

In [7]: r = FormRequest(url=url, formdata=formdata)

In [8]: fetch(r)
        2015-05-12 18:29:16+0530 [default] DEBUG: Crawled (200) <POST http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php> (referer: None)
        [s] Available Scrapy objects:
        [s]   crawler    <scrapy.crawler.Crawler object at 0x7fcc247c4590>
        [s]   item       {}
        [s]   r          <POST http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php>
        [s]   request    <POST http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php>
        [s]   response   <200 http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php>
        [s]   settings   <scrapy.settings.Settings object at 0x7fcc2a74f450>
        [s]   spider     <Spider 'default' at 0x7fcc239ba990>
        [s] Useful shortcuts:
        [s]   shelp()           Shell help (print this help)
        [s]   fetch(req_or_url) Fetch request (or URL) and update local objects
        [s]   view(response)    View response in a browser

In [9]: json_data = json.loads(response.body)

In [10]: sell = Selector(text=json_data.get('content', ''))

In [11]: sell.xpath('//h2/a/text()').extract()
Out[11]: 
        [u'Asus ROG GR8',
         u'Devolo dLAN 1200+',
         u'Yezz Billy 4,7',
         u'Sony Alpha QX1',
         u'Toshiba Encore2 WT10',
         u'BQ Aquaris E5 FullHD',
         u'Toshiba Canvio AeroMobile',
         u'Samsung Galaxy Tab S 10.5',
         u'Modecom FreeTab 7001 HD',
         u'Steganos Online Shield VPN',
         u'AOC G2460PG G-Sync',
         u'AMD Radeon R7 SSD',
         u'Nvidia Shield',
         u'Asus ROG PG278Q GSync',
         u'NOX Krom Kombat']
EDIT
import scrapy
import json
from scrapy.http import FormRequest, Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from pcguia.items import ReviewItem
from dateutil import parser
import re


class PcguiaSpider(scrapy.Spider):
    name = "pcguia" #spider name to call in terminal
    allowed_domains = ['pcguia.pt'] #the domain where the spider is allowed to crawl
    start_urls = ['http://www.pcguia.pt/category/reviews/#paginated=1'] #url from which the spider will start crawling
    page_incr = 1
    pagination_url = 'http://www.pcguia.pt/wp-content/themes/flavor/functions/ajax.php'

    def parse(self, response):
        sel = Selector(response)
        if self.page_incr > 1:
            json_data = json.loads(response.body)
            sel = Selector(text=json_data.get('content', ''))
        review_links = sel.xpath('//h2/a/@href').extract()
        for link in review_links:
            yield Request(url=link, callback=self.parse_review)
        #pagination code starts here 
        # if page has content
        if sel.xpath('//div[@class="panel-wrapper"]'):
            self.page_incr +=1
            formdata = {
                        'sorter':'recent',
                        'location':'main loop',
                        'loop':'main loop',
                        'action':'sort',
                        'view':'grid',
                        'columns':'3',
                        'paginated':str(self.page_incr),
                        'currentquery[category_name]':'reviews'
                        }
            yield FormRequest(url=self.pagination_url, formdata=formdata, callback=self.parse)
        else:
            return

    def parse_review(self, response):
        month_matcher = 'novembro|janeiro|agosto|mar\xe7o|fevereiro|junho|dezembro|julho|abril|maio|outubro|setembro'
        month_dict = {u'abril': u'April',
                                u'agosto': u'August',
                                u'dezembro': u'December',
                                u'fevereiro': u'February',
                                u'janeiro': u'January',
                                u'julho': u'July',
                                u'junho': u'June',
                                u'maio': u'May',
                                u'mar\xe7o': u'March',
                                u'novembro': u'November',
                                u'outubro': u'October',
                                u'setembro': u'September'}
        review_date = response.xpath('//span[@class="date"]/text()').extract()
        review_date = review_date[0].strip().strip('Publicado a').lower() if review_date else ''
        month = re.findall('%s'% month_matcher, review_date)[0]
        _date = parser.parse(review_date.replace(month, month_dict.get(month))).strftime('%Y-%m-%dT%H:%M:%T')
        title = response.xpath('//h1[@itemprop="itemReviewed"]/text()').extract()
        title = title[0].strip() if title else ''
        item_pub = ReviewItem(
            date=_date,
            title=title)
        yield item_pub
output
{'date': '2014-11-05T00:00:00', 'title': u'Samsung Galaxy Tab S 10.5'}
By: John Dene
Score: 0
