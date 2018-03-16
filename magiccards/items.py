# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class LanguageItem(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()


class LanguageItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class CardSetItem(scrapy.Item):
    name = scrapy.Field()


class CardSetItemLoader(ItemLoader):
    name_in = MapCompose(str.strip)
    name_out = TakeFirst()
