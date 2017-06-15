# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from news.items import NewsItem

class ChinadailySpider(scrapy.Spider):
    name = "chinaDaily"
    allowed_domains = ["cn.chinadaily.com.cn"]
    start_urls = ['http://cn.chinadaily.com.cn/']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')

        with open('a.html', 'wb') as f:
            for link in soup.find_all(name='a', attrs={'target': "_blank"}):
                href = link.get('href')
                if 'content' in href and href.startswith('http://'):
                    f.write(str.encode(href + '\n' + link.text + '\n'))
                    yield scrapy.Request(href, callback=self.parse_content)


    def parse_content(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        Item=NewsItem()
        Item['title']=soup.title.text
        Item['source']=soup.find(id='source').text
        Item['pubtime']=soup.find(id='pubtime').text
        Item['content']=soup.find(id="Content").text
        yield Item
