# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class CollectipItem(Item):
    # define the fields for your item here like:
    ipAddress = Field()  # 代理ip里面带上了端口
    position = Field()  # 代理位置
    httpType = Field()  # http 连接类型
    speed = Field()     # 速度
    connectTime = Field()  # 连接时间
    aliveTime = Field()  # 存活时间
    authTime = Field()  # 验证时间
