# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from peewee import *

db = SqliteDatabase('news.db')

class News(Model):
    title = CharField()
    source = CharField()
    pubtime = DateTimeField()
    content = TextField()

    class Meta:
        database = db


class NewsPipeline(object):
    def __init__(self):
        db.connect()
        if len(db.get_tables()) == 0:
            db.create_table(News)

    def process_item(self, item, spider):
        news=News()
        news.title = item['title']
        news.source = item['source']
        news.pubtime = item['pubtime']
        news.content = item['content']
        news.save()
        return item
