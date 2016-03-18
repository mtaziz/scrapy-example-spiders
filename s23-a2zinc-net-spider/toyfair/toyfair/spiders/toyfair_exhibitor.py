# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ToyfairItem
from scrapy.selector import Selector
import urlparse
from selenium import webdriver
from selenium.webdriver import phantomjs
import time 


class ToyfairExhibitorSpider(CrawlSpider):
    name = "toyfair_exhibitor"
    allowed_domains = ["s23.a2zinc.net"]
    start_urls = (
        'http://www.s23.a2zinc.net/clients/TIA/Toyfair2016/public/eBooth.aspx?IndexInList=522&FromPage=Exhibitors.aspx&ParentBoothID=&ListByBooth=true&BoothID=227432&Nav=False',
        'http://s23.a2zinc.net/clients/TIA/Toyfair2016/public/eBooth.aspx?IndexInList=1063&FromPage=Exhibitors.aspx&ParentBoothID=&ListByBooth=true&BoothID=227199&Nav=False',
        'http://s23.a2zinc.net/clients/TIA/Toyfair2016/public/eventmap.aspx?shMode=E&Mapid=123',
    )
    ###{{{Rules To Be Applied for all the links found in subsequent pages
    rules = (
    	# /TIA/Toyfair2016/public/eBooth.aspx\?IndexInList=\d+\w.+\&Nav=False
        # Rule(LinkExtractor(allow=(r'/person/\d+/\w.+'), unique=True),
        # Rule(LinkExtractor(allow=(r'/TIA/Toyfair2016/public/eBooth.aspx\?IndexInList=\d+\w.+\&Nav=False'), unique=True),
        # /TIA/Toyfair2016/public/eBooth.aspx\?IndexInList=\d.+\w.+=False
        # Rule(LinkExtractor(allow=(r'/TIA/Toyfair2016/public/eBooth.aspx\?IndexInList=\d+\w.+'), unique=True),
        Rule(LinkExtractor(allow=(r'/TIA/Toyfair2016/public/eBooth.aspx\?IndexInList=\d+\w.+=False'), unique=True),
            process_links='process_links',
            callback='parse_exhibitors',
            follow=True,
            # max_pages=5
            ),
        )
    ###}}}
    
    ###{{{
    # service_args = ['--ignore-ssl-errors=true',]
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(20)
        super(ToyfairExhibitorSpider, self).__init__(*args, **kwargs)
    # driver = webdriver.PhantomJS()
    ###}}}

    def parse_exhibitors(self, response):

    	self.driver.get(response.url)
    	sel = Selector(text=self.driver.page_source)
    	source_urls_data = response.url
    	item = ToyfairItem()
    	exhibitors_name_data = sel.xpath('//*[@id="eboothContainer"]/div[2]/div/h1/text()').extract()
    	# //*[@id="eboothContainer"]/div[2]/div
    	# //*[@id="eboothContainer"]/div[2]/div/div/span[1]
    	# exhibitors_address_data = sel.xpath('//*[@id="eboothContainer"]/div[2]/div/text()').extract()
    	# exhibitors_address_data = sel.xpath('//div[@id="eboothContainer"]//div[2]//span//text()').extract() #working1
    	exhibitors_address_data = sel.xpath('//div[@id="eboothContainer"]//div[2]//span//text()').extract()[0:3] #working1
    	exhibitors_website_data = sel.xpath('//div[@id="eboothContainer"]//div[2]//span//text()').extract()[3]
    	# .xpath('//div[@id="eboothContainer"]//div[2]//span//text()').extract()[0:3]
    	#/html/body/form/div[3]/div[2]/div/div[3]/div[1]/div[5]/div[2]/div[1]/div[2]/div/div
    	booth_address_data = sel.xpath('//*[@id="eboothContainer"]/ul/li[1]/text()').extract()
    	about_exhibitors_data = sel.xpath('//*[@id="eboothContainer"]//p//text()').extract()
    	# //*[@id="eboothContainer"]/p[6]/text()
    	brands_data = sel.xpath('//*[@id="eboothContainer"]//p[2]//text()').extract()
    	# //*[@id="eboothContainer"]/p[2]/text()
    	item['Source_Urls'] = source_urls_data
    	item['Exhibitors_Name'] = exhibitors_name_data
    	item['Exhibitors_Address'] = exhibitors_address_data
    	item['Exhibitors_Website'] = exhibitors_website_data
    	item['Booth_ID'] = booth_address_data
    	item['About_Exhibitors'] = about_exhibitors_data
    	item['Brands_Name'] = brands_data
    	return item
    	self.driver.quit()
        
# //*[@id="eboothContainer"]/div[2]/div/div
#     	<div class="BoothContactInfo pull-left"><span class="BoothContactCity">Minneapolis,&nbsp;
# 								</span><span class="BoothContactState">MN&nbsp;
# 								</span><br><span class="BoothContactCountry">United States<br></span><span class="BoothContactUrl"><a id="BoothContactUrl" target="_blank" href="javascript:void(0);" class="aa-BoothContactUrl" aa-href="
# 											Boothurl.aspx?BoothID=227199">http://www.uhccf.org</a><br></span><div class="SocialMediaContainer " style="padding-top: 5px">
#             <div id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_pnlCustomFieldList" style="width:150px;">
	
    
    
#     <span id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_dlCustomFieldList"><span class="spCustomFieldIcon">
            
            
            
#         </span></span>

# </div>
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnCustomFieldID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnCustomFieldID" value="0">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnCustomFieldName" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnCustomFieldName">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnContactID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnContactID" value="0">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnCoID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnCoID" value="7867">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnBoothID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnBoothID" value="227199">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnEventID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnEventID" value="21">
# <input type="hidden" name="ctl00$ContentPlaceHolder1$ctrlCustomField_Logos$hdnLangID" id="ctl00_ContentPlaceHolder1_ctrlCustomField_Logos_hdnLangID" value="1">

#           </div>
#         </div>
