# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SrealityItem(Item):
    title = Field()
    imgs = Field()
    detail_url = Field()
    price = Field()

