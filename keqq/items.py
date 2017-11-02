# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KeqqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course_name = scrapy.Field()
    sold_count = scrapy.Field()
    price = scrapy.Field()
    sold_by = scrapy.Field()
    link = scrapy.Field()
