# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class NovelItem(Item):
    title = Field()
    desc = Field()
    chapterUrl = Field()
    chapterName = Field()
    content = Field()
