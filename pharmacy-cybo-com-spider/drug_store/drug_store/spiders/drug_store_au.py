# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DrugStoreItem
#from ..utils_drug_store_au import 
from scrapy.selector import Selector
import urlparse

class DrugStoreAuSpider(scrapy.Spider):
    name = "drug_store_au"
    allowed_domains = ["pharmacy.cybo.com"]
    start_urls = ['https://pharmacy.cybo.com/AU-biz/chemist-outlet_3K',
    'https://pharmacy.cybo.com/AU-biz/black-magic-spray-tanning',
	'https://pharmacy.cybo.com/AU-biz/salon-first_9M',
	'https://pharmacy.cybo.com/AU-biz/gmp-pharmaceuticals_1V',
	'https://pharmacy.cybo.com/AU-biz/chemsave-day-&-night-chemist',
	'https://pharmacy.cybo.com/AU-biz/australian-blister-sealing_2i',
	'https://pharmacy.cybo.com/AU-biz/weston-imports',
	'https://pharmacy.cybo.com/AU-biz/terry-white-chemists_283W',
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemist_55z',
	'https://pharmacy.cybo.com/AU-biz/chemist-direct-plus',
	'https://pharmacy.cybo.com/m/AU-biz/kids-plus-chemist_3g',
	'https://pharmacy.cybo.com/m/AU-biz/denis-green-pharmacist-advice_29',
	'https://pharmacy.cybo.com/m/AU-biz/mcbeath-peter_2r',
	'https://pharmacy.cybo.com/m/AU-biz/cincotta-discount-chemist-merrylands',
	"'https://pharmacy.cybo.com/m/AU-biz/mcbeath's-pharmacy-westmead",
	'https://pharmacy.cybo.com/m/AU-biz/high-quality-life',
	'https://pharmacy.cybo.com/m/AU-biz/herbalife_259h',
	"https://pharmacy.cybo.com/m/AU-biz/dr-david-o'dowling_2c",
	'https://pharmacy.cybo.com/m/AU-biz/chemist-warehouse-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/argyle-street-medical-centre',
	'https://pharmacy.cybo.com/AU-biz/bpp',
	'https://pharmacy.cybo.com/AU-biz/merrylands-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/dr-luke-nitschke',
	'https://pharmacy.cybo.com/AU-biz/cincotta-chemist-auburn',
	'https://pharmacy.cybo.com/AU-biz/tolar-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/emma-crescent-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/priceline-centro',
	"'https://pharmacy.cybo.com/AU-biz/paul's-pharmacy",
	'https://pharmacy.cybo.com/AU-biz/pnw-pharmacy-nutrition-warehouse',
	'https://pharmacy.cybo.com/AU-biz/pulse-pharmacy_31F',
	'https://pharmacy.cybo.com/AU-biz/survival-emergency-products',
	"https://pharmacy.cybo.com/AU-biz/mcbeath's-chemist",
	'https://pharmacy.cybo.com/AU-biz/gardiners-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/macquarie-st-parramatta',
	'https://pharmacy.cybo.com/AU-biz/pharmasave_7e',
	'https://pharmacy.cybo.com/AU-biz/arcade-pharmacy-wentworthville_23',
	'https://pharmacy.cybo.com/AU-biz/terry-white-chemist_35X',
	'https://pharmacy.cybo.com/AU-biz/ingenius-search-marketing',
	"'https://pharmacy.cybo.com/AU-biz/bickle's-pharmacy-merrylands",
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemist_196t',
	'https://pharmacy.cybo.com/AU-biz/auburn-&-lidcombe-u.f.s.-pharmacy-board_1G',
	'https://pharmacy.cybo.com/AU-biz/oatlands-house_3X',
	"https://pharmacy.cybo.com/AU-biz/darin's-pharmacy_7I",
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemists_1426',
	'https://pharmacy.cybo.com/AU-biz/carlingford-day-&-night-chemist',
	'https://pharmacy.cybo.com/AU-biz/pharmeasy',
	'https://pharmacy.cybo.com/AU-biz/wyeth-australia',
	'https://pharmacy.cybo.com/AU-biz/priceline_151R',
	'https://pharmacy.cybo.com/AU-biz/priceline-pharmacy-north-parramatta',
	'https://pharmacy.cybo.com/AU-biz/practicare',
	'https://pharmacy.cybo.com/AU-biz/my-chemist-parramatta_2N',
	'https://pharmacy.cybo.com/AU-biz/downs-roger',
	"'https://pharmacy.cybo.com/AU-biz/tim-perry's-pharmacy_2H",
	'https://pharmacy.cybo.com/AU-biz/a.p.i.-health-care-chemists',
	'https://pharmacy.cybo.com/AU-biz/vitaminking.com.au_2I',
	'https://pharmacy.cybo.com/AU-biz/coopers-greystanes-soul-pattinson_5u',
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemists_1565',
	'https://pharmacy.cybo.com/AU-biz/practical-first-aid_14',
	"https://pharmacy.cybo.com/AU-biz/paul's-pharmacy-plus_2G",
	'https://pharmacy.cybo.com/AU-biz/pharmacist-advice_3b',
	'https://pharmacy.cybo.com/AU-biz/chemsave-pharmacy-parramatta',
	'https://pharmacy.cybo.com/AU-biz/panos-peter-amcal-chemist',
	'https://pharmacy.cybo.com/AU-biz/shop-smart-wholesale-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/lakes-pharmacy',
	"https://pharmacy.cybo.com/AU-biz/john's-day-&-night-chemist",
	'https://pharmacy.cybo.com/AU-biz/aps_26h',
	'https://pharmacy.cybo.com/AU-biz/priceline-pharmacy-merrylands_1e',
	'https://pharmacy.cybo.com/AU-biz/bungaree-road-community-pharmacy',
	'https://pharmacy.cybo.com/AU-biz/terry-white-chemists_54F',
	'https://pharmacy.cybo.com/AU-biz/guardian-distributors-pty-ltd',
	'https://pharmacy.cybo.com/AU-biz/the-edge-parramatta',
	'https://pharmacy.cybo.com/AU-biz/mass-nutrition-burwood_1g',
	'https://pharmacy.cybo.com/AU-biz/mr-manufacturing-&-packaging-pty-ltd_3q',
	'https://pharmacy.cybo.com/AU-biz/chemmart_29l',
	'https://pharmacy.cybo.com/AU-biz/michael-tolar-soul-pattinson',
	'https://pharmacy.cybo.com/AU-biz/drug-information-centre-of-western_10',
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemists_99x',
	'https://pharmacy.cybo.com/AU-biz/dubpos-noel-chemist',
	'https://pharmacy.cybo.com/AU-biz/aroma-de-cupid',
	'https://pharmacy.cybo.com/AU-biz/allan-lee-chemist_3I',

	'https://pharmacy.cybo.com/AU-biz/family-care-chemist_1q',
	'https://pharmacy.cybo.com/AU-biz/shahnaz-herbals-australia',
	'https://pharmacy.cybo.com/AU-biz/dellwood-medical-centre',
	'https://pharmacy.cybo.com/AU-biz/seven-hills-pharmacist',
	'https://pharmacy.cybo.com/AU-biz/chiropractor-baulkham-hills',
	'https://pharmacy.cybo.com/AU-biz/pharmacist-advice_69s',
	'https://pharmacy.cybo.com/AU-biz/api-health-care-head-office_2J',
	'https://pharmacy.cybo.com/AU-biz/rayvue-equipment_1C',
	'https://pharmacy.cybo.com/AU-biz/xtreme-chemist-toongabbie_1M',
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemists_108i',

	'https://pharmacy.cybo.com/AU-biz/merck-sharp-&-dohme_2q',
	'https://pharmacy.cybo.com/AU-biz/cincotta-discount-chemist_6f',
	'https://pharmacy.cybo.com/AU-biz/homart-pharmaceuticals_2b',
	'https://pharmacy.cybo.com/AU-biz/chiropractor-parramatta',
	'https://pharmacy.cybo.com/AU-biz/medicines-plus',
	'https://pharmacy.cybo.com/AU-biz/soul-pattinson-chemist_194T',
	'https://pharmacy.cybo.com/AU-biz/star-combo-australia-pty-ltd',
	'https://pharmacy.cybo.com/AU-biz/procter-&-gamble-australia-pty-ltd',
	'https://pharmacy.cybo.com/AU-biz/pharmacist-advice_63c',
	'https://pharmacy.cybo.com/AU-biz/behan-michael_19',
	'https://pharmacy.cybo.com/m/AU-biz/chemist-outlet_3K',
	'https://pharmacy.cybo.com/m/AU-biz/black-magic-spray-tanning',
	'https://pharmacy.cybo.com/m/AU-biz/salon-first_9M',
	'https://pharmacy.cybo.com/m/AU-biz/gmp-pharmaceuticals_1V',
	'https://pharmacy.cybo.com/m/AU-biz/chemsave-day-&-night-chemist',
	'https://pharmacy.cybo.com/m/AU-biz/australian-blister-sealing_2i',
	'https://pharmacy.cybo.com/m/AU-biz/weston-imports',
	'https://pharmacy.cybo.com/m/AU-biz/terry-white-chemists_283W',
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemist_55z',
	'https://pharmacy.cybo.com/m/AU-biz/chemist-direct-plus',
	'https://pharmacy.cybo.com/AU-biz/kids-plus-chemist_3g',
	'https://pharmacy.cybo.com/AU-biz/denis-green-pharmacist-advice_29',
	'https://pharmacy.cybo.com/AU-biz/mcbeath-peter_2r',
	'https://pharmacy.cybo.com/AU-biz/cincotta-discount-chemist-merrylands',
	"https://pharmacy.cybo.com/AU-biz/mcbeath's-pharmacy-westmead',"
	'https://pharmacy.cybo.com/AU-biz/high-quality-life',
	'https://pharmacy.cybo.com/AU-biz/herbalife_259h',
	"'https://pharmacy.cybo.com/AU-biz/dr-david-o'dowling_2c",
	'https://pharmacy.cybo.com/AU-biz/chemist-warehouse-parramatta',
	'https://pharmacy.cybo.com/AU-biz/argyle-street-medical-centre',
	'https://pharmacy.cybo.com/m/AU-biz/survival-emergency-products',
	"https://pharmacy.cybo.com/m/AU-biz/mcbeath's-chemist',"
	'https://pharmacy.cybo.com/m/AU-biz/gardiners-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/macquarie-st-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/pharmasave_7e',
	'https://pharmacy.cybo.com/m/AU-biz/arcade-pharmacy-wentworthville_23',
	'https://pharmacy.cybo.com/m/AU-biz/terry-white-chemist_35X',
	'https://pharmacy.cybo.com/m/AU-biz/ingenius-search-marketing',
	"https://pharmacy.cybo.com/m/AU-biz/bickle's-pharmacy-merrylands",
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemist_196t',
	'https://pharmacy.cybo.com/m/AU-biz/bpp',
	'https://pharmacy.cybo.com/m/AU-biz/merrylands-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/dr-luke-nitschke',
	'https://pharmacy.cybo.com/m/AU-biz/cincotta-chemist-auburn',
	'https://pharmacy.cybo.com/m/AU-biz/tolar-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/emma-crescent-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/priceline-centro',
	"https://pharmacy.cybo.com/m/AU-biz/paul's-pharmacy",
	'https://pharmacy.cybo.com/m/AU-biz/pnw-pharmacy-nutrition-warehouse',
	'https://pharmacy.cybo.com/m/AU-biz/pulse-pharmacy_31F',
	'https://pharmacy.cybo.com/m/AU-biz/merck-sharp-&-dohme_2q',
	'https://pharmacy.cybo.com/m/AU-biz/cincotta-discount-chemist_6f',
	'https://pharmacy.cybo.com/m/AU-biz/homart-pharmaceuticals_2b',
	'https://pharmacy.cybo.com/m/AU-biz/chiropractor-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/medicines-plus',
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemist_194T',
	'https://pharmacy.cybo.com/m/AU-biz/star-combo-australia-pty-ltd',
	'https://pharmacy.cybo.com/m/AU-biz/procter-&-gamble-australia-pty-ltd',
	'https://pharmacy.cybo.com/m/AU-biz/pharmacist-advice_63c',
	'https://pharmacy.cybo.com/m/AU-biz/behan-michael_19',
	'https://pharmacy.cybo.com/m/AU-biz/family-care-chemist_1q',
	'https://pharmacy.cybo.com/m/AU-biz/shahnaz-herbals-australia',
	'https://pharmacy.cybo.com/m/AU-biz/dellwood-medical-centre',
	'https://pharmacy.cybo.com/m/AU-biz/seven-hills-pharmacist',
	'https://pharmacy.cybo.com/m/AU-biz/chiropractor-baulkham-hills',
	'https://pharmacy.cybo.com/m/AU-biz/pharmacist-advice_69s',
	'https://pharmacy.cybo.com/m/AU-biz/api-health-care-head-office_2J',
	'https://pharmacy.cybo.com/m/AU-biz/rayvue-equipment_1C',
	'https://pharmacy.cybo.com/m/AU-biz/xtreme-chemist-toongabbie_1M',
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemists_108i',
	'https://pharmacy.cybo.com/m/AU-biz/the-edge-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/mass-nutrition-burwood_1g',
	'https://pharmacy.cybo.com/m/AU-biz/mr-manufacturing-&-packaging-pty-ltd_3q',
	'https://pharmacy.cybo.com/m/AU-biz/chemmart_29l',
	'https://pharmacy.cybo.com/m/AU-biz/michael-tolar-soul-pattinson',
	'https://pharmacy.cybo.com/m/AU-biz/drug-information-centre-of-western_10',
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemists_99x',
	'https://pharmacy.cybo.com/m/AU-biz/dubpos-noel-chemist',
	'https://pharmacy.cybo.com/m/AU-biz/aroma-de-cupid',
	'https://pharmacy.cybo.com/m/AU-biz/allan-lee-chemist_3I',
	'https://pharmacy.cybo.com/m/AU-biz/chemsave-pharmacy-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/panos-peter-amcal-chemist',
	'https://pharmacy.cybo.com/m/AU-biz/shop-smart-wholesale-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/lakes-pharmacy',
	"'https://pharmacy.cybo.com/m/AU-biz/john's-day-&-night-chemist",
	'https://pharmacy.cybo.com/m/AU-biz/aps_26h',
	'https://pharmacy.cybo.com/m/AU-biz/priceline-pharmacy-merrylands_1e',
	'https://pharmacy.cybo.com/m/AU-biz/bungaree-road-community-pharmacy',
	'https://pharmacy.cybo.com/m/AU-biz/terry-white-chemists_54F',
	'https://pharmacy.cybo.com/m/AU-biz/guardian-distributors-pty-ltd',
	'https://pharmacy.cybo.com/m/AU-biz/my-chemist-parramatta_2N',
	"https://pharmacy.cybo.com/m/AU-biz/downs-roger",
	"https://pharmacy.cybo.com/m/AU-biz/tim-perry's-pharmacy_2H",
	'https://pharmacy.cybo.com/m/AU-biz/a.p.i.-health-care-chemists',
	'https://pharmacy.cybo.com/m/AU-biz/vitaminking.com.au_2I',
	'https://pharmacy.cybo.com/m/AU-biz/coopers-greystanes-soul-pattinson_5u',
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemists_1565',
	'https://pharmacy.cybo.com/m/AU-biz/practical-first-aid_14',
	"https://pharmacy.cybo.com/m/AU-biz/paul's-pharmacy-plus_2G",
	'https://pharmacy.cybo.com/m/AU-biz/pharmacist-advice_3b',
	'https://pharmacy.cybo.com/m/AU-biz/auburn-&-lidcombe-u.f.s.-pharmacy-board_1G',
	'https://pharmacy.cybo.com/m/AU-biz/oatlands-house_3X',
	"https://pharmacy.cybo.com/m/AU-biz/darin's-pharmacy_7I",
	'https://pharmacy.cybo.com/m/AU-biz/soul-pattinson-chemists_1426',
	'https://pharmacy.cybo.com/m/AU-biz/carlingford-day-&-night-chemist',
	'https://pharmacy.cybo.com/m/AU-biz/pharmeasy',
	'https://pharmacy.cybo.com/m/AU-biz/wyeth-australia',
	'https://pharmacy.cybo.com/m/AU-biz/priceline_151R',
	'https://pharmacy.cybo.com/m/AU-biz/priceline-pharmacy-north-parramatta',
	'https://pharmacy.cybo.com/m/AU-biz/practicare',
	]
    # with open('urls_final.txt') as f:
    # 	start_urls = f.readlines()
    # # with open('/utils_drug_store_au/urls_final.txt', 'r') as f:
    # f = open('urls_final.txt')
    # start_urls = [url.strip() for url in f.readlines()]
    # f.close()
    # start_urls = (
    #     'http://www.pharmacy.cybo.com/',
    #     'https://pharmacy.cybo.com/AU/westmead,_new_south_wales/pharmacies-and-drug-stores/?p=1',
    # )
    #regex:    (/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))
    # rules = (
    #     Rule(
    #         #\/pub\/\w.+
    #         # LinkExtractor(allow=('(/pub/(\w+\-\w+\-\w+))|(/pub/(\w+\-\w+))')),
    #         # LinkExtractor(allow=(r'/pub/\w.+$')),
    #         LinkExtractor(allow=(r'/pharmacies-and-drug-stores/\?p=\d+$')),
    #         process_links='process_links',
    #         callback='parse_links',
    #         follow=True, 
    #         # max_pages=5
    #         ),
    #     )

    def parse(self, response):
    	item = DrugStoreItem()
    	sel = Selector(response)
    	# /html/body/div[1]/div/div[3]/div/div/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/div/table[1]/tbody/tr/td[1]/strong/a/h2
    	# <h2 class="inline-block resultpg-bname ellipsis" style="font-weight:bold; margin:0;" itemprop="name">Kids Plus Chemist</h2>
    	#//*[@id="results"]/table/tbody/tr[2]/td/a/div/table[1]/tbody/tr/td[1]/strong/a/h2
    	source_urls = response.url 
    	item['source_url'] = source_urls
    	#response.xpath('//table[@class="result-table-wrapper"]//a[@class="bname-link-res"]/@href'
    	drug_sources = sel.xpath('//table[@class="result-table-wrapper"]//a[@class="bname-link-res"]/@href').extract()
    	#city: response.xpath('//span[@itemprop="addressLocality"]/text()').extract()
    	store_name_data = sel.xpath('//span[@itemprop="addressLocality"]/text()').extract()
    	city_data = sel.xpath('//span[@itemprop="addressLocality"]/text()').extract()
    	administrative_region_data = sel.xpath ('//span[@itemprop="addressRegion"]/text()').extract()
    	country_data = sel.xpath('//span[@itemprop="addressCountry"]/text()').extract()
    	phone_no_data = sel.xpath('.//span[@itemprop="telephone"]/text()').extract()
    	
    	item['store_name'] = store_name_data
    	item['city'] = city_data
    	item['administrative_region'] = administrative_region_data
    	item['country']  = country_data
    	item['phone_no'] = phone_no_data
    	item['store_url'] = drug_sources
    	return item 
