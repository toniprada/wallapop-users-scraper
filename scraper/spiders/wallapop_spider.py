import scrapy
import json
import time
import csv
from wallapopy import WallapopRequestBuilder
from scraper.items import UserItem
from scraper import settings

class WallapopSpider(scrapy.Spider):
    name = "wallapop"
    allowed_domains = ["wallapop.com"]

    def __init__(self, *args, **kwargs):
        super(WallapopSpider, self).__init__(*args, **kwargs)
        self.wallapop = WallapopRequestBuilder()
        self.start_urls = [self.wallapop.user(user_id)['url'] for user_id in self.user_ids_to_download()]

    def user_ids_to_download(self):
        return [40000000]

    def parse(self, response):
        profile = json.loads(response.body)
        reviews_received_url = self.wallapop.user_reviews_received(profile['userId'])['url']
        request = scrapy.Request(reviews_received_url, callback=self.parse_reviews_received)
        request.meta['data'] = json.dumps({'profile' : profile})
        yield request

    def parse_reviews_received(self, response):
        reviews_received = json.loads(response.body)
        data = json.loads(response.meta['data'])
        data.update({'reviews_received': reviews_received})
        reviews_sent_url = self.wallapop.user_reviews_sent(data['profile']['userId'])['url']
        request = scrapy.Request(reviews_sent_url, callback=self.parse_reviews_sent)
        request.meta['data'] = json.dumps(data)
        yield request

    def parse_reviews_sent(self, response):
        reviews_sent = json.loads(response.body)
        data = json.loads(response.meta['data'])
        data.update({'reviews_sent': reviews_sent})
        items_published_url = self.wallapop.user_items_published(data['profile']['userId'])['url']
        request = scrapy.Request(items_published_url, callback=self.parse_items_published)
        request.meta['data'] = json.dumps(data)
        yield request

    def parse_items_published(self, response):
        items_published = json.loads(response.body)
        data = json.loads(response.meta['data'])
        data.update({'items_published': items_published})
        items_sold_url = self.wallapop.user_items_sold(data['profile']['userId'])['url']
        request = scrapy.Request(items_sold_url, callback=self.parse_items_sold)
        request.meta['data'] = json.dumps(data)
        yield request

    def parse_items_sold(self, response):
        items_sold = json.loads(response.body)
        data = json.loads(response.meta['data'])
        data.update({'items_sold': items_sold})
        item = UserItem()
        item['created_at'] = int(time.time()*1000)
        for key in data.keys():
            item[key] = data[key]
        yield item

