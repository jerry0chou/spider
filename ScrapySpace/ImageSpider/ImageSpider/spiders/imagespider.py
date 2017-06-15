# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem
from bs4 import BeautifulSoup
import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

class ImagespiderSpider(scrapy.Spider):
    name = "imagespider"
    start_urls = ['http://www.jiandan.net/ooxx/page-1#comments']

    def parse(self, response):
        print('当前页:', response.url, )
        soup=BeautifulSoup(response.body,'xml')
        images = soup.select('li img')
        for each in images:
            item = ImagespiderItem()
            item['image_urls'] = ['https:%s' % each.get('src')]  # 一定记得加 []
            yield item
        next_page = soup.find('a', class_='next-comment-page').get('href')
        if next_page:
            print('下一页：', next_page)
            yield scrapy.Request(next_page, callback=self.parse)
