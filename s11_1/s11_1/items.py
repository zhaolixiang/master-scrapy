# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import *

class S111Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class BookItem(scrapy.Item):
    name=Field()
    price=Field()
    authors=Field(serializer=lambda x: '|'.join(x))
