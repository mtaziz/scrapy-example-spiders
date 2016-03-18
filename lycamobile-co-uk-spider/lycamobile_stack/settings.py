# -*- coding: utf-8 -*-

# Scrapy settings for lycamobile_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lycamobile_spider'

SPIDER_MODULES = ['lycamobile_spider.spiders']
NEWSPIDER_MODULE = 'lycamobile_spider.spiders'

DOWNLOAD_DELAY= 20

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
###{{{ProxyMiddleware(privoxy)
# HTTP_PROXY = 'https://127.0.0.1:8123' ###Popilo Proxy Config###
# HTTP_PROXY = 'https://127.0.0.1:8118'	###{Privoxy Proxy Config}###
DOWNLOADER_MIDDLEWARES = {
     'lycamobile_spider.middlewares.RandomUserAgentMiddleware': 400,
     'lycamobile_spider.middlewares.ProxyMiddleware': 410,
     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
    }
###}}}


###{{{Feed Exporters to force CSV in ordered
# FEED_EXPORTERS = {
#     'csv': 'lycamobile_spider.exporters.LycamobileItemExporter'
# }
###}}}


###{{{ Item Pipelines
# ITEM_PIPELINES = { 
#     'lycamobile_spider.pipelines.CSVPipeline': 600 
#     }
###}}

# ITEM_PIPELINES = {
# 	'lycamobile_spider.pipelines.Pipeline':600,
# 	}
###}}}

# FIELDS_TO_EXPORT = [ 'Source_Urls', 'UK_Plan_Name','UKPlan_Bundle_Price','Plan_Validity','National_Mins', 'National_Text', 'National_Data',]
	# 'Data_Bundle_Name', 
	# 'Data_Bundle_Price', 
	# 'Data_Bundle_Validity', 
	# 'Data_Bundle_National_data', 
	# ]

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lycamobile_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lycamobile_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lycamobile_spider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED=True
HTTPCACHE_EXPIRATION_SECS=86400
HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage