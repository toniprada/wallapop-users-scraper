# -*- coding: utf-8 -*-
import scrapy

class UserItem(scrapy.Item):
    created_at        = scrapy.Field()
    profile           = scrapy.Field()
    reviews_received  = scrapy.Field()
    reviews_sent      = scrapy.Field()
    items_published   = scrapy.Field()
    items_sold        = scrapy.Field()
    pass
