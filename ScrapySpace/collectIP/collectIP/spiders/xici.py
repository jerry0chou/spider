# -*- coding: utf-8 -*-
import scrapy
import logging
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from collectIP.items import CollectipItem
class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["www.xicidaili.com"]
    start_urls = ['http://www.xicidaili.com/nn/1']

    def parse(self, response):
        print('当前页:', response.url)
        item=CollectipItem()
        d=pq(response.body_as_unicode())
        for each in d('tr:gt(0)').items():
            item['ipAddress']= each('td:eq(1)').text()+':'+each('td:eq(2)').text()
            item['position']=each('td:eq(3)').text()
            item['httpType'] = each('td:eq(5)').text()
            item['speed'] = each('td:eq(6)')('div').attr('title')[0:-1]
            item['connectTime'] = each('td:eq(7)')('div').attr('title')[0:-1]
            item['aliveTime'] = each('td:eq(8)').text()
            item['authTime'] = each('td:eq(9)').text()
            yield item
        tail=d(".next_page").attr('href')
        next_page='http://www.xicidaili.com'+tail
        if tail:
            print('下一页:', next_page)
            yield scrapy.Request(next_page, callback=self.parse)