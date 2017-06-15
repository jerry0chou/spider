# coding=utf-8
from scrapy import Request
from scrapy.spiders import CrawlSpider
from novel.items import NovelItem
from bs4 import BeautifulSoup

class novSpider(CrawlSpider):
    name = "novelspider"
    redis_key = "novelspider:start_urls"
    start_urls = ['http://www.daomubiji.com']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        article_href = soup.select('article a')
        for a in article_href:
            yield Request(a.get('href'), callback=self.parse_item)

    def parse_item(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        title = soup.find('h1', class_='focusbox-title').text
        desc = soup.find('div', class_='focusbox-text').text
        sites = soup.select('article a')
        item = NovelItem()
        for site in sites:
            item['title'] = title
            item['desc'] = desc
            item['chapterUrl'] = site.get('href')
            item['chapterName'] = site.text
            # 将下一层URL和本函数的字典参数传递给parse_item_content函数
            yield Request(item['chapterUrl'], meta={'item': item}, callback=self.parse_item_content)

    def parse_item_content(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        item = response.meta['item']
        item['content'] = soup.find('article').text
        yield item
