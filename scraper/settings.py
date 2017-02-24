# -*- coding: utf-8 -*-
import os

LOG_LEVEL ='INFO'
BOT_NAME = 'wallapop-users-scraper'
SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
DOWNLOAD_HANDLERS = { 's3': None }
USER_AGENT = 'okhttp/2.3.0'
ITEM_PIPELINES = {
   'scraper.pipelines.JsonWriterPipeline': 300,
}
# speed
AUTOTHROTTLE_ENABLED=False
DOWNLOAD_DELAY=0.05
COOKIES_ENABLED=False
# scrapy-proxies
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_proxies.RandomProxy': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}
PROXY_LIST = 'config/proxies.txt'
# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0
