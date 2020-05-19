# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):

    ranking = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    director = scrapy.Field()
    casts = scrapy.Field()
    score = scrapy.Field()
    num = scrapy.Field()
    comment = scrapy.Field()

