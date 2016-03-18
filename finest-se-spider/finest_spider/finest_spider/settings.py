# -*- coding: utf-8 -*-

# Scrapy settings for finest_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'finest_spider'

SPIDER_MODULES = ['finest_spider.spiders']
NEWSPIDER_MODULE = 'finest_spider.spiders'
DOWNLOAD_DELAY=5
###{{{ProxyMiddleware(privoxy)
#HTTP_PROXY = 'http://127.0.0.1:8123'
###Popilo Proxy Config###
# HTTP_PROXY = 'http://127.0.0.1:8118'
#{Privoxy Proxy Config}###
DOWNLOADER_MIDDLEWARES = {
     # 'angel_spider.middlewares.RandomUserAgentMiddleware': 400,
     'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
     # 'finest_spider.middlewares.ProxyMiddleware': 410,
     # 'finest_spider.middlewares.RetryChangeProxyMiddleware': 420
     # 'angel_spider.middlewares.PhantomjsMiddleware': 543,
     # 'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
     }
###}}}

# DOWNLOADER_MIDDLEWARES = {
#    'angel_spider.middlewares.PhantomjsMiddleware': 543,
# }

###{{{Feed Exporters to force CSV in ordered
FEED_EXPORTERS = {
    'csv': 'finest_spider.exporters.CSVItemExporter'
}
###}}}
# JS_PATTERN = []
JS_BIN = '/usr/local/bin/phantomjs'
# JS_WAIT = 2
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'finest_spider.pipelines.DuplicatePipeline': 300,
# }
###{{{ Item Pipelines
# ITEM_PIPELINES = { 'vessels_dispatch_spider.pipelines.CSVPipeline': 600
# }
###}}

# ITEM_PIPELINES = {
# 	'lycamobile_spider.pipelines.Pipeline':600,
# 	}
###}}}

FIELDS_TO_EXPORT = ['Blogger_Urls', 'Blogger_Name', 'Profile_Info', 'Blogger_Email']

HTTPCACHE_ENABLED=True
HTTPCACHE_EXPIRATION_SECS=865000
HTTPCACHE_DIR='httpcache'

	# 'Data_Bundle_Name', 
	# 'Data_Bundle_Price', 
	# 'Data_Bundle_Validity', 
	# 'Data_Bundle_National_data', 
	# ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vessels_dispatch_spider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'vessels_dispatch_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'vessels_dispatch_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
