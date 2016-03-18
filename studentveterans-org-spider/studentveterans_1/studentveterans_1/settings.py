# -*- coding: utf-8 -*-

# Scrapy settings for studentveterans_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'studentveterans_1'

SPIDER_MODULES = ['studentveterans_1.spiders']
NEWSPIDER_MODULE = 'studentveterans_1.spiders'

# SPIDER_MODULES = ['studentveterans_spider.spiders']
# NEWSPIDER_MODULE = 'studentveterans_spider.spiders'
HTTP_PROXY = 'https://127.0.0.1:8123'	###{Privoxy Proxy Config}###
# HTTP_PROXY = 'https://127.0.0.1:8118'	###{Privoxy Proxy Config}###
DOWNLOADER_MIDDLEWARES = {
	'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    # 'stadlistan_sweden.middlewares.RandomUserAgentMiddleware': 400,
    'studentveterans_1.middlewares.ProxyMiddleware': 410,
     # 'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
}
###}}}


###{{{Feed Exporters to force CSV in ordered
FEED_EXPORTERS = {
    'csv': 'studentveterans_1.exporters.CSVItemExporter'
}

FIELDS_TO_EXPORT = ['ChapterName', 'StudentLeaderFirstName', 'StudentLeaderLastName', 'Address', 'Website', 'StudentLeaderFirstName', 'StudentLeaderLastName', 'StudentLeaderEmail', 'ChapterAdvisorFirstName', 'ChapterAdvisorLastName', 'ChapterAdvisorEmail', 'ChapterLeaderPhone', 'ChapterAdvisorPhone', 'SchoolType', 'ChapterEmail', 'ChapterPhone', 'OPEID', 'IPEDSID']

# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=86400
# HTTPCACHE_DIR='httpcache'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'studentveterans_1 (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=10
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
#    'studentveterans_1.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'studentveterans_1.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'studentveterans_1.pipelines.SomePipeline': 300,
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
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
