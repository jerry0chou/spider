# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from peewee import *

db = SqliteDatabase('proxy.db')


class Proxy(Model):
    ipAddress = CharField()
    position = CharField()
    httpType = CharField()
    speed = IntegerField()
    connectTime = IntegerField()
    aliveTime = IntegerField()
    authTime = DateTimeField()

    class Meta:
        database = db


class CollectipPipeline(object):
    def __init__(self):
        db.connect()
        if len(db.get_tables()) == 0:
            db.create_table(Proxy)

    def process_item(self, item, spider):
        pro = Proxy()
        pro.ipAddress = item['ipAddress']
        pro.position = item['position']
        pro.httpType = item['httpType']
        pro.speed = item['speed']
        pro.connectTime=item['connectTime']
        pro.aliveTime=item['aliveTime']
        pro.authTime=item['authTime']
        pro.save()
        return item
